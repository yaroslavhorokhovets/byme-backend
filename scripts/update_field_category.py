#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 17/05/2022
"""
from src.models.mongo.category_model import CategoryModel

async def update():
    lst_category = await CategoryModel().find_paginate({"rule_required": {"$exists": False}}, page=-1)
    for category in lst_category:
        print(category)

if __name__ == '__main__':
    update()

