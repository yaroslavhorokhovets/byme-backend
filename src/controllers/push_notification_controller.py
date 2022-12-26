#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import math

from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.api import build_message_susccess
from src.common.exception import CustomError
from src.controllers import BaseController
from src.models.mongo.push_notification_model import PushNotificationModel


class PushNotificationController(BaseController):

    @staticmethod
    async def add_push_notification(body, notification_type, access_token):
        data_add = body.dict()
        data_add["type"] = notification_type
        data_add["status_send"] = "unsent"
        data_add["created_time"] = datetime.datetime.utcnow()
        data_add["updated_time"] = datetime.datetime.utcnow()
        data_add["action_time"] = datetime.datetime.strptime(data_add["action_time"], "%Y-%m-%dT%H:%M:%S.%fZ")

        add_id = await PushNotificationModel().collection.insert_one(data_add)
        return build_message_susccess()

    @staticmethod
    async def lst_push_notification(page, per_page, notification_type, access_token):
        page = int(page)
        per_page = int(per_page)
        filter_option = {
            "type": notification_type
        }
        count = await PushNotificationModel().collection.count_documents(filter_option)
        total_page = math.ceil(count / per_page)
        lst_notification = await PushNotificationModel().find_paginate(filter_option, page, per_page,
                                                                       sort_option=[("updated_time", -1)])
        result = []
        page_data = {
            "total_count": count,
            "total_page": total_page,
            "page": page,
            "per_page": per_page
        }
        async for notification in lst_notification:
            result.append(jsonable_encoder(notification, custom_encoder={ObjectId: str}))

        return build_message_susccess(
            data={"data": result},
            page=page_data
        )

    @staticmethod
    async def update_push_notification(push_id, body_update, notification_type, access_token):
        filter_option = {
            "_id": ObjectId(push_id),
            "type": notification_type
        }

        detail_push_notification = await PushNotificationModel().detail_push_notification_by_filter(filter_option)
        if not detail_push_notification:
            raise CustomError("Notification not exists")
        data_update = body_update.dict(exclude_unset=True)
        data_update["updated_time"] = datetime.datetime.utcnow()
        status_update = await PushNotificationModel().update_push_notification_by_id(push_id, data_update)
        if status_update.matched_count > 0:
            return build_message_susccess()
        raise CustomError("Update fail")

    @staticmethod
    async def delete_push_notification(push_id, access_token):
        filter_option = {
            "_id": ObjectId(push_id)
        }

        status_push_notification = await PushNotificationModel().collection.delete_one(filter_option)
        if status_push_notification.deleted_count > 0:
            return build_message_susccess()
        raise CustomError("Delete fail")
