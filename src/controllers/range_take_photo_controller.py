#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from src.api import build_message_susccess
from src.controllers import BaseController
from src.helper.auth.handle_token import HandleToken
from src.models.mongo.range_take_photo_model import RangeTakePhotoModel


class RangeTakePhotoController(BaseController):

    @staticmethod
    async def add_log_out(access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        action_time = datetime.datetime.utcnow().timestamp()
        data_insert = {
            "account_id": account_id,
            "action_time": action_time
        }
        await RangeTakePhotoModel().collection.insert_one(data_insert)
        return build_message_susccess()
