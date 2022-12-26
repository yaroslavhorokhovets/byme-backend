#!/usr/bin/env python
# -*- coding: utf-8 -*-


from fastapi import APIRouter, Header, Query

from src.api.uri import URI
from src.base_model_request.base_model_activity_history import BodyAddActivityHistory
from src.common.custom_router_class import LogRequest
from src.controllers.history_controller import HistoryController
from src.helper.auth.handle_token import HandleToken

history_service_router = APIRouter(route_class=LogRequest)


@history_service_router.get(URI.HISTORY.ACTIVITY_HISTORY)
@HandleToken.verify_token
async def lst_activity_history(
        year: str = Query(..., description="Năm"),
        month: str = Query(..., description="Tháng"),
        page: str = Query(..., description="Page"),
        per_page: str = Query(..., description="Per Page"),
        access_token: str = Header(...)
):
    return await HistoryController().get_activity_history(
        year=year,
        month=month,
        page=page,
        per_page=per_page,
        access_token=access_token
    )


@history_service_router.post(URI.HISTORY.ACTIVITY_HISTORY)
@HandleToken.verify_token
async def add_activity_history(
        body: BodyAddActivityHistory,
        access_token: str = Header(...)
):
    return await HistoryController().add_activity_history(
        body=body,
        access_token=access_token
    )
