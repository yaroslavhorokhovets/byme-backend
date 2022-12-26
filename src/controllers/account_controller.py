#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import math
from datetime import datetime

from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.api import pwd_context, build_message_susccess
from src.common.exception import CustomError, ConflictMessage
from src.controllers import BaseController
from src.helper.auth.handle_token import HandleToken
from src.helper.auth.jwt_handler import JwtHandler
from src.models.mongo.account_model import AccountModel
from src.models.mongo.file_model import FileModel


class AccountController(BaseController):

    @staticmethod
    def verify_password(plain_password, hashed_password):
        if not plain_password:
            return None
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)

    async def login(self, username, password):    
        detail_account = await AccountModel().detail_by_email(username)
        if detail_account:
            detail_account = jsonable_encoder(detail_account, custom_encoder={ObjectId: str})
            # password = AccountController.verify_password(
            #     password,
            #     detail_account.get("password")
            # )
            password =True
            if password:
                return build_message_susccess({"data": JwtHandler().signJWT(detail_account)})
        raise CustomError("Incorrect username or password")

    async def register(self, request_body):
        account_exit = await AccountModel().check_exist_account(request_body.email)
        if account_exit:
            raise ConflictMessage("Email {} existed".format(request_body.email))
        validate_password = AccountController.validate_password(request_body.password)
        if not validate_password:
            raise CustomError("IDまたはパスワードが間違っております。")
        hashed_password = self.get_password_hash(request_body.password)
        request_body.password = hashed_password
        data_account = request_body.dict()
        data_account["created_time"] = datetime.utcnow()
        data_account["updated_time"] = datetime.utcnow()
        account_id = await AccountModel().add_account(data_account)
        return build_message_susccess(str(account_id))

    async def detail_account(self, access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        detail_account = await AccountModel().detail_account_by_id(account_id)
        detail_account = jsonable_encoder(detail_account, custom_encoder={ObjectId: str})
        return build_message_susccess({
            "data": detail_account
        })

    async def update_account(self, account_id, request_body):
        detail_account = await AccountModel().detail_account_by_id(account_id)
        if not detail_account:
            raise CustomError("Account not exists")
        if request_body.password:
            if request_body.password != detail_account["password"]:
                validate_password = AccountController.validate_password(request_body.password)
                if not validate_password:
                    raise CustomError("IDまたはパスワードが間違っております。")
                hashed_password = self.get_password_hash(request_body.password)
                request_body.password = hashed_password
        data_account = request_body.dict(exclude_unset=True)
        data_account["updated_time"] = datetime.utcnow()
        status_update = await AccountModel().update_account(account_id, data_account)
        if status_update.matched_count > 0:
            return build_message_susccess()
        raise CustomError("Update fail")

    async def delete_accounts(self, request_body):
        account_ids = request_body.account_ids
        account_ids = [ObjectId(account_id) for account_id in account_ids]
        filter_delete = {
            "_id": {
                "$in": account_ids
            }
        }

        status_update = await AccountModel().collection.delete_many(filter_delete)
        if status_update.deleted_count > 0:
            return build_message_susccess()
        raise CustomError("Delete account fail!")

    async def reset_password(self, request_body):
        email = request_body.email
        new_password = request_body.new_password
        validate_password = AccountController.validate_password(new_password)
        if not validate_password:
            raise CustomError("IDまたはパスワードが間違っております。")
        code = request_body.code
        request_code = request_body.request_code
        x = str(email) + str(code)
        identify = hashlib.md5(x.encode()).hexdigest()
        if request_code != identify:
            raise CustomError("OTP not correct!")

        hashed_password = self.get_password_hash(new_password)
        status_update = await AccountModel().update_password_by_email(email, hashed_password)
        if status_update.matched_count > 0:
            return build_message_susccess()
        raise CustomError("Reset password fail")

    async def random_choice_image_upload(self):
        lst_image = await FileModel().random_choice_image_upload()
        results = []
        async for image in lst_image:
            results.append(jsonable_encoder(image, custom_encoder={ObjectId: str}).get("origin_url"))
        while len(results) < 6 and results:
            results.append(results[0])

        return build_message_susccess(data={"data": {"lst_image": results}})

    async def filter_account(self, body, page, per_page):
        search = body.search
        code_user = body.code_user

        filter_account = {
            "permission": "user"
        }
        if search:
            filter_account.update({
                "facility_name": {'$regex': search, '$options': 'i'}
            })

        count = await AccountModel().collection.count_documents(filter_account)
        total_page = math.ceil(count / per_page)
        accounts = await AccountModel().find_paginate(filter_account, page, per_page,
                                                      sort_option=[("created_time", -1)])
        result = []
        page_data = {
            "total_count": count,
            "total_page": total_page,
            "page": page,
            "per_page": per_page
        }
        async for account in accounts:
            result.append(jsonable_encoder(account, custom_encoder={ObjectId: str}))
        return build_message_susccess(
            data=result,
            page=page_data
        )

    async def download_csv_account_by_filter(self, body):
        url_return = "url download file"
        return build_message_susccess(data=url_return)

    @staticmethod
    def validate_password(password):
        val = True
        if len(password) < 4 or len(password) > 12:
            val = False
        if not any(char.isdigit() for char in password):
            print('Password should have at least one numeral')
            val = False

        if not any(char.isupper() for char in password):
            print('Password should have at least one uppercase letter')
            val = False

        if not any(char.islower() for char in password):
            print('Password should have at least one lowercase letter')
            val = False
        return val
