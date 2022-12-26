#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 31/05/2022
"""
from bson import ObjectId

from src.models.mongo import BaseModel


class PushNotificationModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.collection = self.db["push_notification"]

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

    async def detail_push_notification_by_filter(self, filter_option: dict) -> dict:
        return await self.collection.find_one(filter_option)

    async def update_push_notification_by_id(self, push_id: str, data_update: dict):
        return await self.collection.update_one(
            {
                "_id": ObjectId(push_id)
            },
            {
                "$set": data_update
            }
        )

    async def filter_by_option(self, filter_option):
        return self.collection.find(filter_option)