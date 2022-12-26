#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.models.mongo import BaseModel


class HistoryModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.collection = self.db["history"]

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
