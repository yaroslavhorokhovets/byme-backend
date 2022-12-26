#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Date: 22/03/2022
    Project: byme-api
"""
from typing import Optional

from fastapi import APIRouter, Form, UploadFile, Header, File, Query

from src.api.uri import URI
from src.base_model_request.base_model_file import ImageRequestEditBody, DeleteFileBody, FilterFileBody, \
    DownloadImageBody, DeleteFileTutorialBody
from src.base_model_request.base_model_history import FilterHistoryImage
from src.common.custom_router_class import LogRequest
from src.controllers.file_controller import FileController
from src.helper.auth.handle_token import HandleToken

file_service_router = APIRouter(route_class=LogRequest)


@file_service_router.post(URI.FILE.UPLOAD_IMAGE)
@HandleToken.verify_token
async def upload_image(
        file: UploadFile = File(...),
        root_category_id: str = Form(..., description="ID category root"),
        category_id: str = Form(..., description="ID category upload"),
        coordinates: list = Form(..., description="Toạ độ khi up ảnh"),
        access_token: str = Header(...)
):
    return await FileController().upload_image(file, root_category_id, category_id, coordinates, access_token)


@file_service_router.post(URI.FILE.OVERRIDE_IMAGE)
@HandleToken.verify_token
async def override_image(
        file: UploadFile = File(...),
        image_id: str = Form(..., description="ID image cần ghi đè"),
        note: str = Form(None, description="Ghi chú khi ghi đè"),
        access_token: str = Header(None)
):
    return await FileController().override_image(file, image_id, access_token)


@file_service_router.post(URI.FILE.UPLOAD_FILE)
async def upload_file(
        file: UploadFile = File(...),
        folder: str = File(..., description="Folder")
):
    return await FileController().upload_file(file, folder)


@file_service_router.post(URI.FILE.IMAGE_REQUEST_EDIT)
@HandleToken.verify_token
async def image_request_edit(
        request_body: ImageRequestEditBody, access_token: str = Header(None)
):
    return await FileController().image_request_edit(request_body)


@file_service_router.post(URI.FILE.IMAGE_ACTIONS_DELETE)
@HandleToken.verify_token
async def image_action_delete(
        request_body: DeleteFileBody, access_token: str = Header(None)
):
    return await FileController().delete_images(request_body)


@file_service_router.post(URI.FILE.IMAGE_ACTIONS_FILTER)
@HandleToken.verify_token
async def image_action_filter(
        request_body: FilterFileBody,
        page: Optional[int] = Query(..., description="Page cần lấy dữ liệu"),
        per_page: Optional[int] = Query(..., description="Số lượng ảnh cần lấy trên 1 trang"),
        access_token: str = Header(None)
):
    return await FileController().filter_image(request_body, page, per_page, access_token)


@file_service_router.post(URI.FILE.DOWNLOAD_IMAGE)
@HandleToken.verify_token
async def download_image(
        request_body: DownloadImageBody,
        access_token: str = Header(None)
):
    return await FileController().download_image(request_body, access_token)


@file_service_router.post(URI.FILE.HISTORY_REQUEST_IMAGE)
@HandleToken.verify_token
async def history_request_image(
        request_body: FilterHistoryImage,
        tab: Optional[str] = Query(None, description="Tab cần lấy dữ liệu. Ví dụ: before_upload, pending, edited"),
        page: Optional[int] = Query(..., description="Page cần lấy dữ liệu"),
        per_page: Optional[int] = Query(..., description="Số lượng ảnh cần lấy trên 1 trang"),
        access_token: str = Header(None)
):
    return await FileController().history_request_image(request_body, tab, page, per_page, access_token)


@file_service_router.post(URI.FILE.UPLOAD_FILE_TUTORIAL)
@HandleToken.verify_token
async def upload_file_tutorial(
        file: UploadFile = File(...),
        format_tutorial: str = Query(..., description="Định dạng file hướng dẫn"),
        access_token: str = Header(...)
):
    return await FileController().upload_tutorial(file, format_tutorial, access_token)


@file_service_router.post(URI.FILE.DELETE_FILE_TUTORIAL)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def delete_file_tutorial(
        body: DeleteFileTutorialBody,
        access_token: str = Header(...)
):
    return await FileController().delete_file_tutorial(body)


@file_service_router.get(URI.FILE.LIST_FILE_TUTORIAL)
@HandleToken.verify_token
async def lst_file_tutorial(
        format_tutorial: str = Query(None, description="Định dạng tutorial"),
        page: Optional[int] = Query(..., description="Page cần lấy dữ liệu"),
        per_page: Optional[int] = Query(..., description="Số lượng ảnh cần lấy trên 1 trang"),
        access_token: str = Header(None)
):
    return await FileController().lst_file_tutorial(format_tutorial, page, per_page, access_token)
