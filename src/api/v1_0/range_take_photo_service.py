#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Header

from src.api.uri import URI
from src.common.custom_router_class import LogRequest
from src.controllers.range_take_photo_controller import RangeTakePhotoController
from src.helper.auth.handle_token import HandleToken

range_take_photo_services_router = APIRouter(route_class=LogRequest)


@range_take_photo_services_router.post(URI.RANGE_TAKE_PHOTO.OUT)
@HandleToken.verify_token
async def add_log_out_range_take_photo(
        access_token: str = Header(None)
):
    return await RangeTakePhotoController.add_log_out(access_token)
