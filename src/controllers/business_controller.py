#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import math

from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.api import build_message_susccess
from src.common.exception import CustomError
from src.controllers import BaseController
from src.helper.auth.handle_token import HandleToken
from src.models.mongo.business_account_model import BusinessAccountModel


class BusinessController(BaseController):
   
    @staticmethod
    async def add_account(request_body, access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        email = request_body.email

        business_account_id = ObjectId()
        data_insert = {
            "_id": business_account_id,
            "account_id": account_id,
            "email": email,
            "name": request_body.name,
            "family_name": request_body.family_name,
            "given_name": request_body.given_name,
            "email_verified": request_body.email_verified,            
            "iat": request_body.iat,            
            "sub": request_body.sub,            
            "exp": request_body.exp,            
            "aud": request_body.aud,            
            "azp": request_body.azp,            
            "jti": request_body.jti,         
            "nbf": request_body.nbf,         
            "iss": request_body.iss,         
            "picture": request_body.picture, 
            "access_token": request_body.access_token, 
            "refresh_token": request_body.refresh_token, 
            "started_date": datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"),
            "status": 1
        }

        filter_exit = {
            "status": 1,
            "account_id": account_id,
            "email": email
        }

        check_exit_by_filter = await BusinessAccountModel().check_exist_business_account(filter_exit)

        if check_exit_by_filter:
            business_account_id = await BusinessAccountModel().update_business_account(account_id, data_insert)
        else:
            business_account_id = await BusinessAccountModel().add_business_account(data_insert)

        if business_account_id:
            return build_message_susccess({"data": jsonable_encoder(data_insert, custom_encoder={ObjectId: str})})
        raise CustomError("Add business account fail.")

    @staticmethod
    async def get_business_account(access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        detail_account = await BusinessAccountModel().detail_business_account_by_id(account_id)
        detail_account = jsonable_encoder(detail_account, custom_encoder={ObjectId: str})
        return build_message_susccess({
            "data": detail_account
        })

    @staticmethod
    async def update_account(access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        detail_account = await BusinessAccountModel().detail_business_account_by_id(account_id)
        if not detail_account:
            raise CustomError("Account not exists")

        data_insert = {
            'status': 0
        }

        status_update = await BusinessAccountModel().update_business_account(account_id, data_insert)
        if status_update.matched_count > 0:
            return build_message_susccess()
        raise CustomError("Update fail")

    @staticmethod
    async def delete_account(access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        delete_account = await BusinessAccountModel().delete_business_account_by_id(account_id)
        if delete_account == True:
            return build_message_susccess()
        raise CustomError("Delete fail")