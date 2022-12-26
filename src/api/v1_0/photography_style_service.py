#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Header

from src.api.uri import URI
from src.common.custom_router_class import LogRequest
from src.controllers.photography_style_controller import PhotographyStyleController
from src.helper.auth.handle_token import HandleToken

photography_style_service_router = APIRouter(route_class=LogRequest)


@photography_style_service_router.post(URI.PHOTOGRAPHY_STYLE.PHOTOGRAPHY_STYLE_DEFAULT)
@HandleToken.verify_token
async def insert_default(access_token: str = Header(None)):
    return await PhotographyStyleController().insert_default()

