#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from bson import ObjectId

from src.common import StatusSeenLinkTutorial, CommonCategoryIDDefault, AccountID, SubCategory, PermissionAccount
from src.models.mongo import BaseModel


class CategoryModel(BaseModel):
    ID = "id"
    NAME = "name"
    CODE = "code"
    DESCRIPTION = "description"
    PARENT_ID = "parent_id"
    NUMBER_NEXT_STEP = "number_next_step"
    ACTION_TIME = "action_time"
    ACCOUNT_ID = "account_id"
    ROOT_CATEGORY_ID = "root_category_id"

    def __init__(self):
        super().__init__()
        self.collection = self.db["category"]

    async def insert_data_default(self):
        print("Start delete data default")
        self.collection.delete_many({"account_id": AccountID.DEFAULT})
        print("Start insert data default")
        data_inserts = [
            {
                "_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "客室を撮影",
                "code": "take_photo_guest_room",
                "description": "Chụp ảnh phòng cho khách",
                "parent_id": None,
                "root_category_id": None,
                "number_next_step": 2,
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": None
                },
                "rule_required": False
            },
            {
                "_id": CommonCategoryIDDefault.TAKE_PHOTO_OUTSIDE_ID,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "外観を撮影",
                "code": "take_photo_outside",
                "description": "Chụp ảnh bên ngoài",
                "parent_id": None,
                "root_category_id": None,
                "number_next_step": 0,
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253c65c1eacc55808d5ffa8.mp4"
                },
                "direction": "横",
                "shooting_height": "",
                "rule_required": True,
                "rule": "車などはすべて移動させる。"
                        "カラーコーンやお客様名の看板は撤去する。"
                        "水平を保ったまま建物全体が映る位置に下がって撮影（垂直はずれても良い）。",
            },
            {
                "_id": CommonCategoryIDDefault.TAKE_PHOTOS_OF_FACILITIES_ID,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "施設を撮影",
                "code": "take_photos_of_facilities",
                "description": "Chụp ảnh cơ sở vật chất",
                "parent_id": None,
                "root_category_id": None,
                "number_next_step": 1,
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": None
                },
                "rule_required": False
            },
            {
                "_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_FOOD_ID,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "料理を撮影",
                "code": "take_photo_of_food",
                "description": "Chụp ảnh món ăn",
                "parent_id": None,
                "root_category_id": None,
                "number_next_step": 2,
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": None
                },
                "rule_required": False
            },
            {
                "_id": SubCategory.FOOD.CATEGORY_1,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "会席・コースを撮影",
                "code": "",
                "description": "Chụp các món ăn, phần ăn nhiều món",
                "parent_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_FOOD_ID,
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_FOOD_ID,
                "number_next_step": 1,
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": None
                },
                "rule_required": False
            },
            {
                "_id": ObjectId("62898ff511a728862388666e"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "parent_id": SubCategory.FOOD.CATEGORY_1,
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_FOOD_ID,
                "number_next_step": 0,
                "name": "料理全体を撮影",
                "name_japan": "",
                "direction": "真上",
                "shooting_height": "",
                "rule_required": True,
                "rule": "スクエアで真上から撮影する。"
                        "黒シートに料理を並べ、間が生じないよう配置する。"
                        "照明とディフューザー、レフ板を用いて光の当たり具合を調整する。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/626179f058fd4035a669cba7.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                },
                "action_time": datetime.datetime.utcnow().timestamp(),
            },
            {
                "_id": ObjectId("62898ffe11a728862388666f"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "parent_id": SubCategory.FOOD.CATEGORY_1,
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_FOOD_ID,
                "number_next_step": 0,
                "name": "一品ずつ撮影",
                "name_japan": "",
                "direction": "自由",
                "shooting_height": "",
                "rule_required": True,
                "rule": "黒シート上で照明を当て、ディフューザー、レフ板を用いて光の当たり具合を調整する。"
                        "対象物が中心となるように意識する。"
                        "近写の場合はマクロレンズを使用する。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/62617a20c12ea4ec06990e86.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                },
                "action_time": datetime.datetime.utcnow().timestamp(),
            },
            {
                "_id": SubCategory.FOOD.CATEGORY_2,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "ブッフェを撮影",
                "code": "",
                "description": "Chụp ảnh Buffet",
                "parent_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_FOOD_ID,
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_FOOD_ID,
                "number_next_step": 0,
                "direction": "横",
                "shooting_height": "",
                "rule_required": True,
                "rule": "・黒シート上で照明を当て、ディフューザー、レフ板を用いて光の当たり具合を調整する"
                        "・対象物が中心となるように意識する"
                        "・近写の場合はマクロレンズを使用する",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/62c59e7a0016a4d6a5c39427.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                },
                "action_time": datetime.datetime.utcnow().timestamp(),
            },
            {
                "_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_COMFORT_ID,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "アメニティを撮影",
                "code": "take_photo_of_comfort",
                "description": "Chụp ảnh sự tiện nghi",
                "parent_id": None,
                "root_category_id": None,
                "number_next_step": 1,
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": None
                },
                "rule_required": False
            },
            {
                "_id": SubCategory.COMFORT.CATEGORY_1,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "アメニティを撮影 (石鹸・化粧品など)",
                "code": "",
                "description": "Chụp ảnh sự tiện nghi",
                "parent_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_COMFORT_ID,
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_COMFORT_ID,
                "number_next_step": 0,
                "direction": "任意",
                "shooting_height": "",
                "rule_required": True,
                "rule": "スクエアまたは４：３で撮影。"
                        "対象物が中心となるように意識する。"
                        "おしゃれな背景で撮影するなど、撮影方は任意 。",
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/62618381fa585b04bff61131.mp4"
                }
            },
            {
                "_id": SubCategory.COMFORT.CATEGORY_2,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "浴衣",
                "code": "",
                "description": "chụp quẩn áo dùng trong phòng, yukata",
                "parent_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_COMFORT_ID,
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_COMFORT_ID,
                "number_next_step": 0,
                "direction": "任意",
                "shooting_height": "",
                "rule_required": True,
                "rule": "・スクエアで撮影"
                        "・畳の上で撮影（作務衣などはベッドや床の上）"
                        "・水平を意識する ",
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/626183f5544b1cd99e247313.mp4"
                }
            },
            {
                "_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_PUBLIC_BATHS_ID,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "大浴場を撮影",
                "code": "take_photo_of_public_baths",
                "description": "Nhà tắm công cộng",
                "parent_id": None,
                "root_category_id": None,
                "number_next_step": 1,
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": None
                }
            },
            {
                "_id": SubCategory.PUBLIC_BATH.CATEGORY_1,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "脱衣所を撮影",
                "code": "",
                "description": "Chụp phòng thay đồ",
                "parent_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_PUBLIC_BATHS_ID,
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_PUBLIC_BATHS_ID,
                "number_next_step": 0,
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/62618615545bf40a2df443b6.mp4"
                },
                "direction": "横",
                "shooting_height": "",
                "rule_required": True,
                "rule": "・洗面台や衣類入れなどの情報がなるべく多く映る場所から撮影する"
            },
            {
                "_id": SubCategory.PUBLIC_BATH.CATEGORY_2,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "浴室",
                "code": "",
                "description": "chụp phòng tắm",
                "parent_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_PUBLIC_BATHS_ID,
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_PUBLIC_BATHS_ID,
                "number_next_step": 0,
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6261867976678ada479e1026.mp4"
                },
                "direction": "横",
                "shooting_height": "",
                "rule_required": True,
                "rule": "・洗い場：浴室＝１：１の割合で映る場所から撮影する"
                        "・シャワーヘッドは壁を向ける"
                        "・アメニティは満タンに"
                        "・床は濡らす"
            },
            {
                "_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_OTHER_ID,
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "name": "その他",
                "code": "take_photo_other",
                "description": "Chụp ảnh những thứ khác",
                "parent_id": None,
                "root_category_id": None,
                "number_next_step": 0,
                "action_time": datetime.datetime.utcnow().timestamp(),
                "video_tutorial": {
                    "seen": StatusSeenLinkTutorial.NOT_SEEN,
                    "link": None
                },
                "direction": "横",
                "shooting_height": "",
                "rule_required": False,
                "rule": "・決まりなく自由に撮影する"
            },
            {
                "_id": ObjectId("62897d5911a728862388666c"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTOS_OF_FACILITIES_ID,
                "parent_id": CommonCategoryIDDefault.TAKE_PHOTOS_OF_FACILITIES_ID,
                "name": "ロビー",
                "direction": "横",
                "rule_required": True,
                "shooting_height": "床から1メートルくらいの高さ",
                "rule": "椅子や机を移動させ、対象物すべてが画格に収まるようにする。"
                        "空間を意識して撮影する。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/62c79bc90016a4d6a5c3943b.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                },
                "number_next_step": 0
            },
            {
                "_id": ObjectId("62897d6011a728862388666d"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTOS_OF_FACILITIES_ID,
                "parent_id": CommonCategoryIDDefault.TAKE_PHOTOS_OF_FACILITIES_ID,
                "name": "フロント",
                "direction": "横",
                "rule_required": True,
                "shooting_height": "床から1メートルくらいの高さ",
                "rule": "ペンや記帳簿など、不要なものは撤去する。"
                        "フロントマン（従業員）を立たせて撮影する。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6260a0ba18c443b509b589fc.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                },
                "number_next_step": 0,
            }
        ]
        return await self.collection.insert_many(data_inserts)

    async def get_list_category_default(self, mapping_show):
        if mapping_show:
            list_category_default = self.collection.find({self.ROOT_CATEGORY_ID: None}, mapping_show)
        else:
            list_category_default = self.collection.find({self.ROOT_CATEGORY_ID: None})
        return list_category_default

    async def check_category_exit_by_name(self, account_id, name):
        return await self.collection.find_one({self.NAME: name, self.ACCOUNT_ID: account_id})

    async def check_category_exit_by_filter(self, filter_option):
        return await self.collection.find_one(filter_option)

    async def get_name_by_id(self, category_id):
        detail_category = await self.collection.find_one({"_id": ObjectId(category_id)})
        return detail_category.get(self.NAME) if detail_category else ""

    async def add_category(self, data_category):
        category_id = await self.collection.insert_one(data_category)
        return data_category

    async def add_many_category(self, lst_category):
        category_ids = await self.collection.insert_many(lst_category)
        return category_ids

    async def get_list_category_by_filter(self, filter_option, mapping_show):
        if mapping_show:
            return self.collection.find(filter_option, mapping_show)
        return self.collection.find(filter_option)

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

        return await collection

    async def update_one_category(self, category_id, data_update):
        return await self.collection.update_one(
            {
                "_id": ObjectId(category_id)
            },
            {
                "$set": data_update
            }
        )

    async def delete_category(self, category_id):
        return await self.collection.delete_one(
            {
                "_id": ObjectId(category_id)
            }
        )

    async def seen_tutorial_category(self, account_id, category_id):
        return await self.collection.update_one(
            {
                "account_id": account_id,
                "_id": ObjectId(category_id)
            },
            {
                "$set": {
                    "video_tutorial.seen": StatusSeenLinkTutorial.SEEN
                }
            }
        )

    async def check_near_image_upload_in_category(self, category_id, coordinates, accuracy):
        return await self.collection.find(
            {
                "_id": ObjectId(category_id),
                "location":
                    {"$near":
                        {
                            "$geometry": {"type": "Point", "coordinates": coordinates},
                            "$minDistance": 50,
                            "$maxDistance": 100
                        }
                    }
            }
        )

    async def aggregate_child_category(self, root_category_id, type_category_ids, account_id, permission):
        filter_option = {
            "root_category_id": ObjectId(root_category_id),

            "type_category_id": {
                "$in": type_category_ids
            },
            "number_next_step": 0
        }
        if permission == PermissionAccount.USER:
            filter_option.update({"account_id": account_id})
        aggregate_pipline = [
            {
                "$match": filter_option
            },
            {
                "$group": {
                    "_id": "$photography_style_id",
                    "name": {"$addToSet": "$name"},
                    "type_category_id": {"$addToSet": "$type_category_id"}
                }
            },
            {
                "$project": {
                    "id": "$_id.photography_style_id",
                    "name": "$name",
                    "type_category_id": "$type_category_id",
                }
            }
        ]

        return self.collection.aggregate(aggregate_pipline)
