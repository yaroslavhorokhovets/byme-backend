#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.api import build_message_susccess
from src.common.exception import CustomError
from src.controllers import BaseController
from src.helper.auth.handle_token import HandleToken
from src.models.mongo.category_model import CategoryModel
from src.models.mongo.type_category_model import TypeCategoryModel


class TypeCategoryController(BaseController):

    @staticmethod
    async def insert_default():
        lst_type_category_id = await TypeCategoryModel().insert_data_default()
        if lst_type_category_id:
            return build_message_susccess()
        raise CustomError("Type category default fail")

    @staticmethod
    async def get_root_cat_id(category_id):
        detail_category = await CategoryModel().collection.find_one({"_id": ObjectId(category_id)})
        return detail_category.get("root_category_id") if detail_category.get("root_category_id") else category_id

    @staticmethod
    async def get_type_category_by_root_category_id(root_category_id, access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        permission = HandleToken().get_param_by_token("permission", access_token)
        root_category_id = await TypeCategoryController.get_root_cat_id(root_category_id)
        lst_type_category = await TypeCategoryModel().get_type_category_by_root_category_id(
            account_id=account_id,
            root_category_id=root_category_id,
            permission=permission
        )
        results = []
        async for category in lst_type_category:
            results.append(jsonable_encoder(category, custom_encoder={ObjectId: str}))
        results = sorted(results, key=lambda x: x["order"])
        return build_message_susccess({"data": results})
