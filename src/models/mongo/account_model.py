#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from bson import ObjectId

from src.models.mongo import BaseModel


class AccountModel(BaseModel):
    ID = "id"
    FACILITY_OWNER_NAME = "facility_owner_name"
    EMAIL = "email"
    POSTAL_CODE = "postal_code"
    ADDRESS = "address"
    REPRESENTATIVE_NAME = "representative_name"
    TYPE_BASE = "type_base"
    PHONE_NUMBER = "phone_number"
    USERNAME = "username"
    PASSWORD = "password"
    PERMISSION = "permission"

    def __init__(self):
        super().__init__()
        self.collection = self.db["account"]

    async def check_exist_account(self, email):
        return await self.collection.find_one(
            {self.EMAIL: email})

    async def detail_by_email(self, email: str) -> dict:
        return await self.collection.find_one({"email": email})

    async def add_account(self, data_insert) -> str:
        new_account = await self.collection.insert_one(data_insert)
        return str(data_insert["_id"])

    async def detail_account_by_id(self, account_id: str) -> dict:
        return await self.collection.find_one({"_id": ObjectId(account_id)})

    async def update_account(self, account_id: str, data_update: dict):
        return await self.collection.update_one(
            {
                "_id": ObjectId(account_id)
            },
            {
                "$set": data_update
            }
        )

    async def update_password_by_email(self, email, password):
        return await self.collection.update_one(
            {
                self.EMAIL: email
            },
            {
                "$set": {
                    self.PASSWORD: password,
                    "updated_time": datetime.datetime.utcnow()
                }
            }
        )

    async def get_emails_admin(self):
        return self.collection.find({"permission": "admin"}, {"email": 1})

    async def find_paginate(self, search_option, page=0, per_page=None, sort_option=None, projection=None):
        collection = self.collection.find(search_option, projection)
        if sort_option:
            collection = collection.sort(sort_option)

        if page != -1:
            if per_page:
                collection = collection.limit(per_page)
            if page > 0:
                page -= 1
                offset = int(page) * int(per_page)
                collection = collection.skip(offset)

        return collection
