#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from bson import ObjectId

from src.models.mongo import BaseModel


class BusinessAccountModel(BaseModel):
    ID = "id"
    EMAIL = "email"
    STATUS = "status"
    NAME = "name"
    FAMILY_NAME = "family_name"
    GIVEN_NAME = "given_name"
    EMAIL_VERIFIED = "email_verified"
    IAT = "iat"
    SUB = "sub"
    EXP = "exp"
    AUD = "aud"
    AZP = "azp"
    JTI = "jti"
    NBF = "nbf"
    ISS = "iss"
    PICTURE = "picture"
    STARTED_DATE = "started_date"
    ACCOUNT_ID = "account_id"
    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"

    def __init__(self):
        super().__init__()
        self.collection = self.db["business_account"]

    async def check_exist_business_account(self, filter):
        return await self.collection.find_one(
            {self.EMAIL: filter['email'], self.ACCOUNT_ID: filter['account_id'], self.STATUS: filter['status']})

    async def detail_by_email(self, email: str) -> dict:
        return await self.collection.find_one({"email": email})

    async def add_business_account(self, data_insert) -> str:
        new_account = await self.collection.insert_one(data_insert)
        return str(data_insert["_id"])

    async def detail_business_account_by_id(self, account_id: str) -> dict:  
        account = await self.collection.find_one({"account_id":account_id})
        if account:
            del account['_id']
        return account

    async def delete_business_account_by_id(self, account_id: str) -> int:  
        result = await self.collection.delete_one({"account_id":account_id})
        return result.deleted_count

    async def update_business_account(self, account_id: str, data_insert: dict):
        return await self.collection.update_one(
            {
                "account_id": str(account_id)
            },
            {
                "$set": data_insert
            }
        )
