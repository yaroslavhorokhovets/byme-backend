#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
from logging.config import dictConfig

from bson import ObjectId

from config import settings
from src.common.log import LogConfig

WORKING_DIR = str(settings.BYME_HOME)
SHARE_FOLDER_STATIC = WORKING_DIR + "/static/"
os.makedirs(SHARE_FOLDER_STATIC, exist_ok=True)

dictConfig(LogConfig().dict())
logger = logging.getLogger("buyme_app")


class TypeCoding:
    SHIFT_JIS = "shift-jis"


class AccessToken:
    PREFIX = "Bearer "


class CommonToken:
    EXPIRE = "expire"


class PermissionAccount:
    ADMIN = "admin"
    USER = "user"


class StatusSeenLinkTutorial:
    NOT_SEEN = 0
    SEEN = 1


class FolderUpload:
    TEST = "test"
    TUTORIAL = "tutorial"


class CommonCategoryIDDefault:
    TAKE_PHOTO_GUEST_ROOM_ID = ObjectId('623dc80d66247bd4dd7103a0')
    TAKE_PHOTO_OUTSIDE_ID = ObjectId('623dc81b66247bd4dd7103a1')
    TAKE_PHOTOS_OF_FACILITIES_ID = ObjectId('623dc82666247bd4dd7103a2')
    TAKE_PHOTO_OF_FOOD_ID = ObjectId('623dc82d66247bd4dd7103a3')
    TAKE_PHOTO_OF_COMFORT_ID = ObjectId('623dc83566247bd4dd7103a4')
    TAKE_PHOTO_OF_PUBLIC_BATHS_ID = ObjectId('623deac666247bd4dd7103b4')
    TAKE_PHOTO_OF_OTHER_ID = ObjectId('62402b3caf8f4045edbd9813')


class TypeCategoryAddIDDefault:
    class Room:
        STYLE_ROOM_JAPAN_ID = ObjectId('623de0d966247bd4dd7103a4')
        STYLE_ROOM_FOREIGN_ID = ObjectId('623de1cc66247bd4dd7103a6')
        STYLE_ROOM_FOREIGN_JAPAN_ID = ObjectId('623de27666247bd4dd7103a7')
        LITTLE_HOUSE_ID = ObjectId('623de2a166247bd4dd7103a8')
        JAPAN_BED_ID = ObjectId('623de36b66247bd4dd7103a9')
        CAPSULE_ID = ObjectId('623de3a666247bd4dd7103aa')
        DORMITORY_ID = ObjectId('623de3d266247bd4dd7103ab')

    class Other:
        LOBBY_ID = ObjectId('623de52866247bd4dd7103ac')
        RECEPTIONIST_ID = ObjectId('623de56666247bd4dd7103ad')
        DISHES_SERVINGS_ID = ObjectId('623de58766247bd4dd7103af')
        BUFFET_ID = ObjectId('623de5a166247bd4dd7103af')
        CONVENIENT_ID = ObjectId('623de5d966247bd4dd7103b0')
        YUKATA_ID = ObjectId('623de60966247bd4dd7103b1')
        DRESSING_ROOM_ID = ObjectId('623de65566247bd4dd7103b2')
        BATHROOM_ID = ObjectId('623de68866247bd4dd7103b3')


class SubCategory:
    class FOOD:
        CATEGORY_1 = ObjectId('626178805f2473e9cdaf2cb4')  # Chụp các món ăn, phần ăn nhiều món
        CATEGORY_2 = ObjectId('626178aa5f2473e9cdaf2cb5')  # Chụp ảnh Buffet

    class COMFORT:
        CATEGORY_1 = ObjectId('626182005f2473e9cdaf2cb7')  # Xà phòng, mỹ phẩm, v.v.
        CATEGORY_2 = ObjectId('626182185f2473e9cdaf2cb8')  # chụp quẩn áo dùng trong phòng, yukata

    class PUBLIC_BATH:
        CATEGORY_1 = ObjectId('626185705f2473e9cdaf2cb9')  # Chụp phòng thay đồ
        CATEGORY_2 = ObjectId('6261858a5f2473e9cdaf2cba')  # chụp phòng tắm


class AccountID:
    DEFAULT = "default"


class FileConstant:
    class StatusRequest:
        UPLOAD = "upload"
        EDIT = "edit"
        PENDING = "pending"

    class StatusFile:
        ACTIVE = 1
        DELETE = -1

    class TypeFile:
        IMAGE = "image"


class QuestionConstant:
    ACTIVE = 1
    DELETE = -1


class EmailContact:
    EMAIL = "byme.yado2022@gmail.com"
    # EMAIL = "tungdd180997@gmail.com"
