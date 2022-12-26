#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Header
from fastapi.params import Query

from src.api.uri import URI
from src.common.custom_router_class import LogRequest
from src.controllers.notification_account_controller import NotificationAccountController
from src.helper.auth.handle_token import HandleToken

notification_account_service_router = APIRouter(route_class=LogRequest)


@notification_account_service_router.get(URI.NOTIFICATION_ACCOUNT.LST_NOTIFICATION_ACCOUNT)
@HandleToken.verify_token
async def lst_notification_account(
        page: int = Query(None),
        per_page: int = Query(None),
        access_token: str = Header(None)
):
    return await NotificationAccountController().lst_notification_account(page, per_page, access_token)
