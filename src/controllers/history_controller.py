#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import math

import pytz
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.api import build_message_susccess
from src.common.exception import CustomError
from src.controllers import BaseController
from src.helper.auth.handle_token import HandleToken
from src.models.mongo.account_model import AccountModel
from src.models.mongo.history_model import HistoryModel


class HistoryController(BaseController):

    @staticmethod
    async def get_activity_history(year, month, page, per_page, access_token):
        if not year or not month:
            raise CustomError("Year and month must")

        account_id = HandleToken().get_param_by_token("_id", access_token)
        if int(month) < 10:
            month = "0{}".format(int(month))
        time_query = "{year}-{month}".format(year=year, month=month)
        filter_option = {
            "account_id": account_id,
            "month_action_time": time_query
        }

        detail_account = await AccountModel().detail_account_by_id(account_id)
        account_id_show = detail_account.get("id_use") if detail_account.get("id_use") else detail_account.get("email")

        page = int(page)
        per_page = int(per_page)
        count = await HistoryModel().collection.count_documents(filter_option)
        total_page = math.ceil(count / per_page)
        lst_history = await HistoryModel().find_paginate(filter_option, page, per_page,
                                                         sort_option=[("action_time", -1)])
        result = []
        page_data = {
            "total_count": count,
            "total_page": total_page,
            "page": page,
            "per_page": per_page
        }
        async for history in lst_history:
            data = jsonable_encoder(history, custom_encoder={ObjectId: str})
            data["account_id"] = account_id_show
            result.append(data)
        return build_message_susccess(
            data=result,
            page=page_data
        )

    @staticmethod
    async def add_activity_history(body, access_token):
        tz = datetime.timezone.utc
        body = body.dict()
        account_id = HandleToken().get_param_by_token("_id", access_token)
        body["account_id"] = account_id
        month_action_time = datetime.datetime.utcnow().strftime("%Y-%m")

        action_time = (datetime.datetime.utcnow().replace(tzinfo=tz)).strftime(
            "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        body["month_action_time"] = month_action_time
        body["action_time"] = action_time
        history_id = await HistoryModel().collection.insert_one(body)
        if history_id:
            return build_message_susccess()
        raise CustomError("Add history error")
