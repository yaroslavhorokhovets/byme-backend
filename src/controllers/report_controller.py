#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from datetime import timedelta

from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.api import build_message_susccess
from src.common import FileConstant, PermissionAccount
from src.common.exception import CustomError
from src.common.utils import convert_string_to_date
from src.controllers import BaseController
from src.helper.auth.handle_token import HandleToken
from src.models.mongo.account_model import AccountModel
from src.models.mongo.file_model import FileModel


class ReportController(BaseController):

    @staticmethod
    async def report_home(start_time, end_time, access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        permission = HandleToken().get_param_by_token("permission", access_token)
        try:
            start_time = convert_string_to_date(start_time)
            end_time = convert_string_to_date(end_time) + timedelta(days=1)
        except Exception as e:
            raise CustomError(str(e))

        image_upload_start_time = datetime.datetime.utcnow().replace(hour=0, minute=0, second=1)
        image_upload_end_time = datetime.datetime.utcnow() + timedelta(days=1)

        filter_count_image_upload = {
            "type": FileConstant.TypeFile.IMAGE,
            "$and": [
                {"action_time": {"$gte": image_upload_start_time}},
                {"action_time": {"$lte": image_upload_end_time}},
            ],
        }
        if permission == PermissionAccount.USER:
            filter_count_image_upload.update({"account_id": account_id})
        number_image_upload = await FileModel().collection.count_documents(filter_count_image_upload)

        filter_image_edited = {
            "$and": [
                {"action_time": {"$gte": start_time}},
                {"action_time": {"$lte": end_time}},
            ],
            "edit_url": {"$ne": ""},
            "type": FileConstant.TypeFile.IMAGE,
            "status_request": FileConstant.StatusRequest.EDIT
        }

        if permission == PermissionAccount.USER:
            filter_image_edited["account_id"] = account_id

        number_image_edited = await FileModel().collection.count_documents(filter_image_edited)

        filter_image_request_edit = {
            "$and": [
                {"action_time": {"$gte": start_time}},
                {"action_time": {"$lte": end_time}},
            ],
            "edit_url": "",
            "status_request": FileConstant.StatusRequest.EDIT
        }

        if permission == PermissionAccount.USER:
            filter_image_request_edit["account_id"] = account_id

        number_image_request_edit = await FileModel().collection.count_documents(filter_image_request_edit)

        filter_image_delete = {
            "account_id": account_id,
            "type": FileConstant.TypeFile.IMAGE,
            "$and": [
                {"action_time": {"$gte": start_time}},
                {"action_time": {"$lte": end_time}},
            ],
            "status": FileConstant.StatusFile.DELETE
        }
        if permission == PermissionAccount.USER:
            filter_image_delete["account_id"] = account_id
        number_image_delete = await FileModel().collection.count_documents(filter_image_delete)
        result = {
            "number_image_upload": number_image_upload,
            "number_image_edited": number_image_edited,
            "number_image_request_edit": number_image_request_edit,
            "number_image_delete": number_image_delete
        }
        if permission == PermissionAccount.ADMIN:
            filter_account = {
                "$and": [
                    {"created_time": {"$gte": start_time}},
                    {"created_time": {"$lte": end_time}},
                ]
            }
            number_account_range_time = await AccountModel().collection.count_documents(filter_account)
            lst_account_range_time = AccountModel().collection.find(filter_account)
            result["account_range_time"] = {
                "number": number_account_range_time,
                "list": [
                    jsonable_encoder(account, custom_encoder={ObjectId: str}) async for account in
                    lst_account_range_time
                ]
            }
        return build_message_susccess(
            {
                "data": result
            }
        )

    @staticmethod
    async def report_admin(start_time, end_time, access_token):
        try:
            start_time = convert_string_to_date(start_time)
            end_time = convert_string_to_date(end_time) + timedelta(days=1)
        except Exception as e:
            raise CustomError(str(e))

        image_upload_start_time = datetime.datetime.utcnow().replace(hour=0, minute=0, second=1)
        image_upload_end_time = datetime.datetime.utcnow() + timedelta(days=1)

        filter_count_image_upload = {
            "type": FileConstant.TypeFile.IMAGE,
            "$and": [
                {"action_time": {"$gte": image_upload_start_time}},
                {"action_time": {"$lte": image_upload_end_time}},
            ],
        }
        number_image_take_today = await FileModel().collection.count_documents(filter_count_image_upload)

        filter_image_edited = {
            "type": "image",
            "$and": [
                {"action_time": {"$gte": start_time}},
                {"action_time": {"$lte": end_time}},
            ],
            "edit_url": {"$ne": ""},
            "status_request": FileConstant.StatusRequest.EDIT
        }

        number_image_edited = await FileModel().collection.count_documents(filter_image_edited)

        filter_image_request_edit = {
            "type": "image",
            "$and": [
                {"action_time": {"$gte": start_time}},
                {"action_time": {"$lte": end_time}},
            ],
            "edit_url": "",
            "status_request": FileConstant.StatusRequest.EDIT
        }

        number_image_request_edit = await FileModel().collection.count_documents(filter_image_request_edit)
        result = {
            "number_image_take_today": number_image_take_today,
            "number_image_edited": number_image_edited,
            "number_image_request_edit": number_image_request_edit
        }
        filter_account = {
            "$and": [
                {"created_time": {"$gte": start_time}},
                {"created_time": {"$lte": end_time}},
            ]
        }
        number_account_range_time = await AccountModel().collection.count_documents(filter_account)
        lst_account_range_time = AccountModel().collection.find(filter_account)
        result["account_range_time"] = {
            "number": number_account_range_time,
            "list": [
                jsonable_encoder(account, custom_encoder={ObjectId: str}) async for account in
                lst_account_range_time
            ]
        }
        return build_message_susccess(
            {
                "data": result
            }
        )
