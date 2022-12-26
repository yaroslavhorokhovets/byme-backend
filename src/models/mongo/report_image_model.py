#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 24/04/2022
"""
from src.models.mongo import BaseModel


class ReportImageModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.collection = self.db["report_image"]

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

    async def add_data(self, data_insert) -> str:
        new_file = await self.collection.insert_one(data_insert)
        return str(data_insert["_id"])

