#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from bson import ObjectId

from src.common import FileConstant
from src.models.mongo import BaseModel


class FileModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.collection = self.db["file"]

    async def add_file(self, data_insert) -> str:
        new_file = await self.collection.insert_one(data_insert)
        return str(data_insert["_id"])

    async def random_choice_image_upload(self):
        return self.collection.aggregate([
            {"$match": {"origin_url": {"$exists": True}}},
            {"$sample": {"size": 6}},
            {"$project": {
                "_id": 0,
                "origin_url": 1
            }}
        ])

    async def override_image(self, image_id, link_file):
        filter_update = {
            "_id": ObjectId(image_id),
            "status_request": FileConstant.StatusRequest.PENDING,
        }
        data_update = {
            "origin_url": link_file,
            "status_request": FileConstant.StatusRequest.EDIT,
            "updated_time": datetime.datetime.utcnow()
        }
        return await self.collection.update_one(filter_update, {"$set": data_update})

    async def upload_google(self, image_id, update_data):
        filter_update = {
            "_id": ObjectId(image_id)
        }
        return await self.collection.update_one(filter_update, {"$set": update_data})

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
