#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bson import ObjectId

from src.models.mongo import BaseModel


class InvoiceModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.collection = self.db["invoice"]

    async def update_invoice(self, invoice_id: str, data_update: dict):
        return await self.collection.update_one(
            {
                "_id": ObjectId(invoice_id)
            },
            {
                "$set": data_update
            }
        )

    async def total_invoice_account(self, filter_option):
        return self.collection.aggregate([
            {"$match": filter_option},
            {"$group": {"_id": None, "total": {"$sum": "$payee"}}},
            {"$project": {
                "_id": 0,
                "total": 1
            }}
        ])

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