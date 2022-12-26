#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import math

from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.api import build_message_susccess
from src.common import StatusSeenLinkTutorial, AccountID, CommonCategoryIDDefault, PermissionAccount, FileConstant
from src.common.exception import CustomError
from src.common.utils import convert_string_to_date
from src.controllers import BaseController
from src.helper.auth.handle_token import HandleToken
from src.models.mongo.category_model import CategoryModel
from src.models.mongo.file_model import FileModel
from src.models.mongo.photography_style_model import PhotographyStyleModel
from src.models.mongo.type_category_model import TypeCategoryModel


class CategoryController(BaseController):

    @staticmethod
    async def insert_default():
        lst_category_id = await CategoryModel().insert_data_default()
        if lst_category_id:
            return build_message_susccess()
        raise CustomError("Insert category default fail")

    @staticmethod
    async def list_category_default(field_keys):
        mapping_show = {}
        if field_keys:
            mapping_show = {key.strip(): 1 for key in field_keys.split(",")}
        lst_category = await CategoryModel().get_list_category_default(mapping_show)
        results = []
        async for category in lst_category:
            results.append(
                jsonable_encoder(category, custom_encoder={ObjectId: str}))
        return build_message_susccess({
            "data": results
        })

    @staticmethod
    async def add_category(request_body, access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        name = request_body.name
        root_category_id = request_body.root_category_id
        type_category_id = request_body.type_category_id

        lst_insert = []

        number_next_step = request_body.number_next_step - 1 if request_body.number_next_step > 1 else 0

        filter_exit = {
            "root_category_id": ObjectId(root_category_id) if root_category_id else None,
            "number_next_step": number_next_step,
            "account_id": account_id,
            "name": name
        }
        check_exit_by_filter = await CategoryModel().check_category_exit_by_filter(filter_exit)
        if check_exit_by_filter:
            raise CustomError("Category name {} existed".format(name))

        category_id = ObjectId()
        data_insert = {
            "_id": category_id,
            "account_id": account_id,
            "code": "",
            "name": name,
            "description": "",
            "source": "custom",
            "parent_id": ObjectId(request_body.parent_id) if request_body.parent_id else root_category_id,
            "type_category_id": ObjectId(type_category_id) if type_category_id else ObjectId(root_category_id),
            "root_category_id": ObjectId(root_category_id) if root_category_id else None,
            "number_next_step": number_next_step,
            "photography_style_id": category_id,
            "rule_required": False,
            "accuracy": request_body.accuracy if request_body.accuracy else 0,
            "action_time": datetime.datetime.utcnow().timestamp()
        }
        if request_body.coordinates:
            data_insert.update({
                "location": {"type": "Point", "coordinates": request_body.coordinates}
            })
        if request_body.link_video_tutorial:
            data_insert["video_tutorial"] = {
                "seen": StatusSeenLinkTutorial.NOT_SEEN,
                "link": request_body.link_video_tutorial
            }
        lst_insert.append(data_insert)
        if number_next_step == 1 and type_category_id:
            lst_photography_style = await PhotographyStyleModel().get_photography_style(
                root_category_id,
                type_category_id
            )
            async for photography_style in lst_photography_style:
                data = {
                    "account_id": account_id,
                    "description": request_body.description,
                    "type_category_id": ObjectId(type_category_id),
                    "root_category_id": ObjectId(root_category_id),
                    "parent_id": ObjectId(category_id),
                    "action_time": datetime.datetime.utcnow(),
                    "number_next_step": number_next_step - 1,
                    "photography_style_id": photography_style["_id"]
                }
                photography_style.pop("_id")
                data.update(photography_style)
                lst_insert.append(data)
        if number_next_step == 1 and not type_category_id and root_category_id:
            lst_photography_style = await PhotographyStyleModel().get_photography_style_by_root_id(
                root_category_id
            )
            async for photography_style in lst_photography_style:
                data = {
                    "account_id": account_id,
                    "description": request_body.description,
                    "root_category_id": ObjectId(root_category_id),
                    "parent_id": ObjectId(category_id),
                    "action_time": datetime.datetime.utcnow(),
                    "number_next_step": number_next_step - 1,
                    "photography_style_id": photography_style["_id"]
                }
                photography_style.pop("_id")
                data.update(photography_style)
                lst_insert.append(data)

        category_ids = await CategoryModel().add_many_category(lst_insert)
        if category_ids:
            return build_message_susccess({"data": jsonable_encoder(data_insert, custom_encoder={ObjectId: str})})
        raise CustomError("Add category fail.")

    @staticmethod
    async def filter_category(field_keys, request_body, access_token):
        mapping_show = {}
        if field_keys:
            mapping_show = {key.strip(): 1 for key in field_keys.split(",")}
        number_next_step = request_body.number_next_step
        root_category_id = request_body.root_category_id
        code_root_category = request_body.code_root_category
        search = request_body.search

        account_id = HandleToken.get_param_by_token("_id", access_token)

        lst_root_category_id = []

        filter_option = {
            "account_id": {"$in": [account_id, AccountID.DEFAULT]},
            "number_next_step": number_next_step - 1 if number_next_step > 0 else 0,
        }
        if root_category_id == str(CommonCategoryIDDefault.TAKE_PHOTO_OF_FOOD_ID) and number_next_step == 2:
            filter_option["number_next_step"] = {
                "$in": [0, 1]
            }

        if root_category_id:
            lst_root_category_id.append(ObjectId(root_category_id))
        if code_root_category:
            root_category = await CategoryModel().collection.find_one({"code": code_root_category})
            if root_category:
                lst_root_category_id.append(root_category["_id"])
        if not lst_root_category_id:
            raise CustomError("Root category is required")
        filter_option["root_category_id"] = {"$in": lst_root_category_id}
        if request_body.parent_id:
            filter_option["parent_id"] = ObjectId(request_body.parent_id)
        if search:
            filter_option["name"] = {'$regex': search, '$options': 'i'}

        lst_category = await CategoryModel().get_list_category_by_filter(filter_option, mapping_show)
        results = []
        async for category in lst_category:
            results.append(jsonable_encoder(category, custom_encoder={ObjectId: str}))
        return build_message_susccess({
            "data": results
        })

    @staticmethod
    async def update_category(category_id, request_body):
        data_update = request_body.dict(exclude_unset=True)
        if "link_video_tutorial" in data_update:
            data_update["video_tutorial"] = {
                "seen": StatusSeenLinkTutorial.NOT_SEEN,
                "link": data_update["link_video_tutorial"]
            }
            del data_update["link_video_tutorial"]
        if "root_category_id" in data_update:
            data_update["root_category_id"] = ObjectId(data_update["root_category_id"])
        if "parent_id" in data_update:
            data_update["parent_id"] = ObjectId(data_update["parent_id"])

        if request_body.coordinates:
            del data_update["coordinates"]
            data_update.update({
                "location": {"type": "Point", "coordinates": request_body.coordinates}
            })
        if request_body.accuracy:
            data_update["accuracy"] = request_body.accuracy if request_body.accuracy else 0,

        status_update = await CategoryModel().update_one_category(category_id, data_update)
        if status_update.matched_count > 0:
            return build_message_susccess()
        raise CustomError("Update category fail")

    @staticmethod
    async def delete_category(category_id):
        status_delete = await CategoryModel().delete_category(category_id)
        if status_delete.deleted_count > 0:
            return build_message_susccess()
        raise CustomError("Delete category {} fail".format(category_id))

    @staticmethod
    async def seen_tutorial_category(category_id, access_token):
        account_id = HandleToken.get_param_by_token("_id", access_token)
        status_update = await CategoryModel().seen_tutorial_category(account_id=account_id, category_id=category_id)
        if status_update.matched_count > 0:
            return build_message_susccess()
        raise CustomError("Update seen tutorial category {} fail".format(category_id))

    @staticmethod
    async def lst_sub_child_category(root_category_id, access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        permission = HandleToken().get_param_by_token("permission", access_token)
        type_categories = await TypeCategoryModel().get_type_category_by_root_category_id(
            account_id=account_id,
            root_category_id=root_category_id,
            permission=permission
        )

        type_category_data = {type_category['_id']: type_category["name"] async for type_category in type_categories}
        if not type_category_data:
            name_root_category = await CategoryModel().get_name_by_id(root_category_id)
            type_category_data = {ObjectId(root_category_id): name_root_category}
        type_category_ids = list(type_category_data.keys())
        child_categories = await CategoryModel().aggregate_child_category(
            root_category_id=root_category_id,
            type_category_ids=type_category_ids,
            account_id=account_id,
            permission=permission
        )
        results = []
        convert_child_category = {}
        async for child in child_categories:
            child_type_category_id = child["type_category_id"][0] if child["type_category_id"] and len(
                child["type_category_id"]) > 0 else None
            if not child_type_category_id:
                continue
            if convert_child_category.get(child_type_category_id):
                convert_child_category[child_type_category_id].append({
                    "id": str(child["_id"]),
                    "name": child["name"]
                })
            else:
                convert_child_category[child_type_category_id] = [{
                    "id": str(child["_id"]),
                    "name": child["name"]
                }]
        for key, value in type_category_data.items():
            data = {
                "id": str(key),
                "name": value,
                "child_categories": convert_child_category.get(key) if convert_child_category.get(key) else []
            }
            results.append(data)
        if not results:
            results.append({
                "id": str(root_category_id),
                "name": await CategoryModel().get_name_by_id(root_category_id),
                "child_categories": []
            })
        return build_message_susccess(data=results)

    @staticmethod
    async def child_filter_image(root_category_id, request_body, page, per_page, access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        permission = HandleToken().get_param_by_token("permission", access_token)
        root_category_id = ObjectId(root_category_id)
        child_id = request_body.child_id
        type_query = request_body.type_query
        filter_option = {
        }
        
        if permission == PermissionAccount.USER:
            filter_option.update({"account_id": {"$in": [account_id, "default"]}})
        # if child_id and type_query != "all":
        #     filter_option["photography_style_id"] = ObjectId(child_id)
        # lst_category_ids = await CategoryModel().collection.distinct("_id", filter_option)
        lst_category_ids = []
        categories = CategoryModel().collection.find(filter_option)
        
        async for category in categories:
            
            if category.get("root_category_id") and category.get("root_category_id") != root_category_id:
                continue
            if (category.get("photography_style_id") and type_query != "all" and child_id and category.get(
                    "photography_style_id") != ObjectId(child_id)):
                continue
            if (category.get("type_category_id") and type_query == "all" and child_id and category.get(
                    "type_category_id") != ObjectId(child_id)):
                continue
            lst_category_ids.append(category["_id"])
        filter_option_image = {
            "type": "image",
            "category_id": {
                "$in": lst_category_ids
            },
            "root_category_id": root_category_id
        }
        

        if permission == PermissionAccount.USER:
            filter_option_image.update({"account_id": account_id})
        if permission == PermissionAccount.ADMIN:
            account_ids = request_body.account_ids
            start_time = request_body.start_time
            end_time = request_body.end_time
            try:
                start_time = convert_string_to_date(start_time, "%Y-%m-%dT%H:%M:%S.%fZ")
                end_time = convert_string_to_date(end_time, "%Y-%m-%dT%H:%M:%S.%fZ") + datetime.timedelta(days=1)
            except Exception as e:
                raise CustomError(str(e))
            filter_option_image.update({
                "status_request": FileConstant.StatusRequest.PENDING,
                "$and": [
                    {
                        "action_time": {"$gte": start_time}
                    },
                    {
                        "action_time": {"$lte": end_time}
                    }
                ]
            })
            if account_ids:
                filter_option_image.update({
                    "account_id": {
                        "$in": account_ids
                    }
                })
        
        count = await FileModel().collection.count_documents(filter_option_image)
        total_page = math.ceil(count / per_page)
        files = await FileModel().find_paginate(filter_option_image, page, per_page, sort_option=[("action_time", -1)])
        result = []
        page_data = {
            "total_count": count,
            "total_page": total_page,
            "page": page,
            "per_page": per_page
        }
        async for file in files:
            result.append(jsonable_encoder(file, custom_encoder={ObjectId: str}))
        return build_message_susccess(
            data=result,
            page=page_data
        )
