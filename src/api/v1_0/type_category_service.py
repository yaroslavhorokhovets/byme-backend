#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Header

from src.api.uri import URI
from src.common.custom_router_class import LogRequest
from src.controllers.type_category_controller import TypeCategoryController
from src.helper.auth.handle_token import HandleToken

type_category_service_router = APIRouter(route_class=LogRequest)


@type_category_service_router.post(URI.TYPE_CATEGORY.TYPE_CATEGORY_DEFAULT)
@HandleToken.verify_token
async def insert_default(access_token: str = Header(None)):
    return await TypeCategoryController().insert_default()


@type_category_service_router.get(URI.TYPE_CATEGORY.TYPE_CATEGORY)
@HandleToken.verify_token
async def get_type_category_by_root_category_id(root_category_id, access_token: str = Header(None)):
    return await TypeCategoryController().get_type_category_by_root_category_id(root_category_id, access_token)
