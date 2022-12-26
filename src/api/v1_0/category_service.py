#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Date: 20/03/2022
    Project: byme-api
"""
from typing import Optional

from fastapi import APIRouter, Header, Query

from src.api.uri import URI
from src.base_model_request.base_model_category import AddCategory, FilterCategory, UpdateCategory, ChildFilterImage
from src.common.custom_router_class import LogRequest
from src.controllers.category_controller import CategoryController
from src.helper.auth.handle_token import HandleToken

category_service_router = APIRouter(route_class=LogRequest)


@category_service_router.get(URI.CATEGORY.CATEGORY_DEFAULT)
@HandleToken.verify_token
async def list_category_default(
        field_keys: Optional[str] = Query("", description="Danh sách field cần lấy dữ liệu"),
        access_token: str = Header(None)
):
    return await CategoryController().list_category_default(field_keys)


@category_service_router.post(URI.CATEGORY.CATEGORY_DEFAULT)
@HandleToken.verify_token
async def insert_category_default(access_token: str = Header(None)):
    return await CategoryController().insert_default()


@category_service_router.post(URI.CATEGORY.CATEGORY)
@HandleToken.verify_token
async def add_category(request_body: AddCategory, access_token: str = Header(None)):
    return await CategoryController().add_category(request_body, access_token)


@category_service_router.post(URI.CATEGORY.FILTER_CATEGORY)
@HandleToken.verify_token
async def filter_category(
        request_body: FilterCategory,
        field_keys: Optional[str] = Query("", description="Danh sách field cần lấy dữ liệu"),
        access_token: str = Header(None)
):
    return await CategoryController().filter_category(field_keys, request_body, access_token)


@category_service_router.put(URI.CATEGORY.DETAIL_CATEGORY)
@HandleToken.verify_token
async def update_category(category_id, request_body: UpdateCategory, access_token: str = Header(None)):
    return await CategoryController().update_category(category_id, request_body)


@category_service_router.delete(URI.CATEGORY.DETAIL_CATEGORY)
@HandleToken.verify_token
async def delete_category(category_id, access_token: str = Header(None)):
    return await CategoryController().delete_category(category_id)


@category_service_router.put(URI.CATEGORY.SEEN_TUTORIAL_CATEGORY)
@HandleToken.verify_token
async def seen_tutorial_category(category_id, access_token: str = Header(None)):
    return await CategoryController().seen_tutorial_category(category_id, access_token)


@category_service_router.get(URI.CATEGORY.LST_SUB_CHILD_CATEGORY)
@HandleToken.verify_token
async def lst_sub_child_category(root_category_id, access_token: str = Header(None)):
    return await CategoryController().lst_sub_child_category(root_category_id, access_token)


@category_service_router.post(URI.CATEGORY.CHILD_FILTER_IMAGE)
@HandleToken.verify_token
async def child_filter_image(
        root_category_id,
        request_body: ChildFilterImage,
        page: Optional[int] = Query(..., description="Page cần lấy dữ liệu"),
        per_page: Optional[int] = Query(..., description="Số lượng ảnh cần lấy trên 1 trang"),
        access_token: str = Header(None)):
    return await CategoryController().child_filter_image(root_category_id, request_body, page, per_page, access_token)
