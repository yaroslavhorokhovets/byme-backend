#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import math
import mimetypes
import os

import pandas as pd
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from starlette.background import BackgroundTasks

from src.api import build_message_susccess
from src.common import SHARE_FOLDER_STATIC, PermissionAccount
from src.common.exception import CustomError
from src.controllers import BaseController
from src.controllers.account_controller import AccountController
from src.controllers.send_mail_controller import SendMailController
from src.helper.auth.handle_token import HandleToken
from src.helper.excel.gen_invoice import gen_invoice
from src.helper.s3 import S3Service
from src.models.mongo.account_model import AccountModel
from src.models.mongo.file_model import FileModel
from src.models.mongo.invoice_model import InvoiceModel

MAPPING_FIELD_INVOICE = {
    "施設コード": "code_user",
    "施設名": "username",
    "請求月日": "day_request",
    "振込期日": "day_transfer",
    "大項目": "big_project",
    "小項目": "small_project",
    "数量": "quantity",
    "銀行": "account_bank",
    "支店": "branch",
    "金額": "payee"
}


class InvoiceController(BaseController):

    @staticmethod
    def build_html_upload_invoice(data):
        HTML_STR = """
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>【重要】請求書が発行されました（<span style='font-family:"Times New Roman",serif;'>Byme</span>）</p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><a href="mailto:info@app-byme.com"><span style='font-family:"Times New Roman",serif;'>info@app-byme.com</span></a></p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>[</span>施設名<span style='font-family:"Times New Roman",serif;'>]</span></p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>ご担当者様</p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>いつも<span style='font-family:"Times New Roman",serif;'>Byme</span>をご利用いただきありがとうございます。</p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>20yy</span>年<span style='font-family:"Times New Roman",serif;'>mm</span>月の請求書が発行されました。</p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>ご確認の上指定日までにお支払いください。</p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>請求書はこちらからダウンロード可能です。</p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>（<span style='font-family:"Times New Roman",serif;'>URL</span>）</p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>今後とも<span style='font-family:"Times New Roman",serif;'>Byme</span>をよろしくお願いいたします。</p>
        <div style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;'>
            <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;border:none;padding:0cm;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
        </div>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>宿泊施設向け写真撮影アプリ「<span style='font-family:"Times New Roman",serif;'>Byme</span>（バイミ）」</p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>お問い合わせ先</p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><a href="mailto:info@app-byme.com"><span style='font-family:"Times New Roman",serif;'>info@app-byme.com</span></a></p>
        <div style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;'>
            <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;border:none;padding:0cm;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
        </div>
        <p><span style='font-size:14px;font-family:"Times New Roman",serif;'><br>&nbsp;</span></p>
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
        """
        return HTML_STR

    async def upload_invoice(self, file, back_ground_tasks, access_token):
        if not file:
            raise CustomError("File not exit")
        lst_account = AccountModel().collection.find({"permission": "user", "ID_use": {"$exists": True}})
        mapping_id_use_email = {account["ID_use"]: account["email"] async for account in lst_account}
        mime_type = file.content_type
        extension_file = mimetypes.guess_extension(mime_type)
        filename = str(ObjectId()) + extension_file
        if extension_file not in [".xlsx", ".xls", ".csv"]:
            raise CustomError("Upload file format wrong!")
        folder_save_file = os.path.join(SHARE_FOLDER_STATIC, filename)
        with open(folder_save_file, "wb+") as file_object:
            file_object.write(file.file.read())
        if extension_file in [".xlsx", ".xls"]:
            data_upload_invoice = pd.read_excel(folder_save_file, engine="openpyxl")
        else:
            data_upload_invoice = pd.read_csv(folder_save_file)
        data_upload = data_upload_invoice.to_json(orient='records', force_ascii=False)
        data_upload = json.loads(data_upload)
        if len(data_upload) > 400:
            raise CustomError("Max length invoice upload!")
        data_inserts = []
        for data in data_upload:
            if len(data_inserts) >= 100:
                invoice_ids = await InvoiceModel().collection.insert_many(data_inserts)
                data_inserts = []
            data_invoice = {}
            for k, v in data.items():
                if not MAPPING_FIELD_INVOICE.get(k) or not v:
                    continue
                if MAPPING_FIELD_INVOICE.get(k) in ["day_request", "day_transfer"]:
                    try:
                        v /= 1000
                        v = datetime.datetime.fromtimestamp(v)
                        v = v.strftime("%Y-%m-%d")
                    except:
                        v = None
                if not v:
                    continue
                data_invoice[MAPPING_FIELD_INVOICE.get(k)] = v
            code_user = data_invoice.get("code_user")
            if not code_user or not mapping_id_use_email.get(code_user):
                continue
            html = InvoiceController.build_html_upload_invoice({})
            await SendMailController().send_to_emails(
                [mapping_id_use_email.get(code_user)],
                html,
                "請求書発行メール",
                back_ground_tasks
            )
            if len(data_invoice.values()) != len(MAPPING_FIELD_INVOICE.values()):
                continue
            data_invoice["account_id"] = code_user
            data_invoice["payee"] = int(data_invoice["payee"])
            data_invoice["created_time"] = datetime.datetime.utcnow()
            data_invoice["updated_time"] = datetime.datetime.utcnow()
            data_invoice["action_time"] = datetime.datetime.utcnow().strftime("%Y-%m")
            data_inserts.append(data_invoice)
        if data_inserts:
            invoice_ids = await InvoiceModel().collection.insert_many(data_inserts)
        os.remove(folder_save_file)
        return build_message_susccess({})

    async def update_invoice(self, invoice_id, request_body):
        detail_invoice = await InvoiceModel().collection.find_one({"_id": ObjectId(invoice_id)})
        if not detail_invoice:
            raise CustomError("Invoice not exists")
        data_invoice = request_body.dict(exclude_unset=True)
        data_invoice["updated_time"] = datetime.datetime.utcnow()
        data_invoice["action_time"] = datetime.datetime.utcnow().strftime("%Y-%m")
        status_update = await InvoiceModel().update_invoice(invoice_id, data_invoice)
        if status_update.matched_count > 0:
            return build_message_susccess()
        raise CustomError("Update fail")

    async def delete_invoice(self, invoice_ids):
        invoice_ids = [ObjectId(invoice_id) for invoice_id in invoice_ids.split(",") if invoice_id]
        status_delete = await InvoiceModel().collection.delete_many({"_id": {"$in": invoice_ids}})
        if status_delete.deleted_count > 0:
            return build_message_susccess()
        raise CustomError("Delete fail")

    async def lst_invoices(self, action_time, page, per_page, access_token):
        page = int(page)
        per_page = int(per_page)
        account_id = HandleToken.get_param_by_token("_id", access_token)
        permission = HandleToken.get_param_by_token("permission", access_token)
        filter_option = {

        }
        if action_time:
            filter_option.update({"action_time": action_time})
        if permission == PermissionAccount.USER:
            filter_option.update({
                "account_id": ObjectId(account_id)
            })

        count = await InvoiceModel().collection.count_documents(filter_option)
        total_page = math.ceil(count / per_page)
        lst_invoices = await InvoiceModel().find_paginate(filter_option, page, per_page,
                                                          sort_option=[("action_time", -1)])
        result = []
        page_data = {
            "total_count": count,
            "total_page": total_page,
            "page": page,
            "per_page": per_page
        }
        async for invoice_id in lst_invoices:
            result.append(jsonable_encoder(invoice_id, custom_encoder={ObjectId: str}))
        total_invoice_account = 0
        if permission == PermissionAccount.USER:
            agg_invoice_account = await InvoiceModel().total_invoice_account(filter_option)
            async for invoice in agg_invoice_account:
                total_invoice_account = invoice.get("total", 0)
        data = {
            "list": result,
            "total": total_invoice_account
        }

        return build_message_susccess(
            data={"data": data},
            page=page_data
        )

    async def download_invoices(self, request_body):
        new_column = {y: x for x, y in MAPPING_FIELD_INVOICE.items()}
        invoice_ids = request_body.invoice_ids
        invoice_ids = [ObjectId(invoice_id) for invoice_id in invoice_ids]
        filename = "ExportingInvoices{}.xlsx".format(str(ObjectId()))
        lst_invoice = InvoiceModel().collection.find(
            {"_id": {"$in": invoice_ids}},
            {
                "_id": 0,
                "code_user": 1,
                "username": 1,
                "day_request": 1,
                "day_transfer": 1,
                "big_project": 1,
                "small_project": 1,
                "quantity": 1,
                "account_bank": 1,
                "branch": 1,
                "payee": 1,
            }
        )
        data_frame = pd.DataFrame([invoice async for invoice in lst_invoice])
        data_frame = data_frame.rename(columns=new_column)
        folder_save_file = os.path.join(SHARE_FOLDER_STATIC, filename)
        data_frame.to_excel(folder_save_file, index=False)
        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        request_metadata = {
            "Content-Type": mime_type
        }
        with open(folder_save_file, "rb") as f:
            result = S3Service().upload_file(f, "export_invoice",
                                             filename, request_metadata,
                                             mime_type)
        return build_message_susccess({
            "data": result
        })

    async def download_invoices_user(self, access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        account_detail = await AccountModel().detail_account_by_id(account_id)
        ID_use = account_detail.get("ID_use")
        time_download = datetime.datetime.utcnow().strftime("%Y-%m")
        data_filters = [
            {
                "name": "年間利用料",
                "number": 1,
                "unit": "間",
                "price": account_detail.get("annual_usage_fee", 0),
                "money": account_detail.get("annual_usage_fee", 0),
            }
        ]
        invoices = InvoiceModel().collection.find({"code_user": ID_use, "action_time": time_download})
        tax = 4830
        subtotal = 0
        date_upload_invoice = None
        async for invoice in invoices:
            quantity = invoice["quantity"]
            number = ""
            unit = ""
            for i in quantity:
                if i.isdigit():
                    number += i
                else:
                    unit += i
            price = invoice["payee"]
            money = price * int(number)
            data = {
                "name": invoice["small_project"],
                "number": number,
                "unit": unit,
                "price": price,
                "money": money
            }
            data_filters.append(data)
            subtotal += money
            date_upload_invoice = invoice["day_transfer"]
        total = subtotal + tax
        # if not subtotal:
        #     return build_message_susccess(
        #         {
        #             "data": ""
        #         }
        #     )
        filter_option_release = {
            "type": "image",
            "status": 1
        }
        number_released = await FileModel().collection.count_documents(filter_option_release)
        data = {
            "facility_name": account_detail.get("facility_name"),
            "number_released": number_released,
            "sales_staff": account_detail.get("sales_staff"),
            "invoice_month": time_download,
            "date_upload_invoice": date_upload_invoice,
            "total": total,
            "tax": tax,
            "subtotal": subtotal,
            "filters": data_filters
        }

        filename = "DownloadInvoicesUser{}.xlsx".format(str(ObjectId()))
        folder_save_file = os.path.join(SHARE_FOLDER_STATIC, filename)
        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        gen_invoice(folder_save_file, data)
        request_metadata = {
            "Content-Type": mime_type
        }
        with open(folder_save_file, "rb") as f:
            result = S3Service().upload_file(f, "export_invoice_user",
                                             filename, request_metadata,
                                             mime_type)
        return build_message_susccess(
            {
                "data": result
            }
        )
