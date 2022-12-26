#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import math

from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.api import build_message_susccess
from src.common import PermissionAccount
from src.controllers import BaseController
from src.helper.auth.handle_token import HandleToken
from src.models.mongo.push_notification_model import PushNotificationModel


class NotificationAccountController(BaseController):

    async def lst_notification_account(self, page, per_page, access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        permission = HandleToken().get_param_by_token("permission", access_token)
        if permission == PermissionAccount.USER:
            page = int(page)
            per_page = int(per_page)
            time_now = datetime.datetime.utcnow()
            filter_option = {
                "action_time": {"$lte": time_now},
                "type": "web"
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
        return build_message_susccess(
            data={"data": []},
            page={}
        )
