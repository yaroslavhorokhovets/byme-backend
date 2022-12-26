#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 25/03/2022
"""
from bson import ObjectId

from src.common import CommonCategoryIDDefault, TypeCategoryAddIDDefault, AccountID, PermissionAccount
from src.models.mongo import BaseModel


class TypeCategoryModel(BaseModel):
    ACCOUNT_ID = "account_id"
    ROOT_CATEGORY_ID = "root_category_id"

    def __init__(self):
        super().__init__()
        self.collection = self.db["type_category"]

    async def insert_data_default(self):
        print("Start insert data default")
        self.collection.delete_many({"account_id": AccountID.DEFAULT})
        data_inserts = [
            {
                "_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_JAPAN_ID,
                "account_id": AccountID.DEFAULT,
                "name": "和室",
                "order": 1,
                "description": "和室",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID
            },
            {
                "_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_ID,
                "account_id": AccountID.DEFAULT,
                "name": "洋室",
                "order": 2,
                "description": "洋室",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID
            },
            {
                "_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_JAPAN_ID,
                "account_id": AccountID.DEFAULT,
                "name": "和洋室",
                "order": 3,
                "description": "和洋室",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID
            },
            {
                "_id": TypeCategoryAddIDDefault.Room.LITTLE_HOUSE_ID,
                "account_id": AccountID.DEFAULT,
                "name": "メゾネット",
                "order": 5,
                "description": "メゾネット",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID
            },
            {
                "_id": TypeCategoryAddIDDefault.Room.JAPAN_BED_ID,
                "account_id": AccountID.DEFAULT,
                "name": "和ベッド",
                "order": 4,
                "description": "和ベッド",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID
            },
            {
                "_id": TypeCategoryAddIDDefault.Room.CAPSULE_ID,
                "account_id": AccountID.DEFAULT,
                "name": "カプセル",
                "order": 7,
                "description": "カプセル",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID
            },
            {
                "_id": TypeCategoryAddIDDefault.Room.DORMITORY_ID,
                "account_id": AccountID.DEFAULT,
                "name": "ドミトリー",
                "order": 6,
                "description": "ドミトリー",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID
            },

        ]
        return await self.collection.insert_many(data_inserts)

    async def get_type_category_by_root_category_id(self, account_id, root_category_id, permission):
        filter_option = {
            self.ROOT_CATEGORY_ID: ObjectId(root_category_id)
        }
        if permission == PermissionAccount.USER:
            filter_option[self.ACCOUNT_ID] = {"$in": [account_id, AccountID.DEFAULT]}
        return self.collection.find(filter_option)
