#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from fastapi import APIRouter, Header, Query

from src.api.uri import URI
from src.base_model_request.base_model_account import (
    BodyLogin,
    BodyRegister, UpdateAccount, ResetPassword, ActionFilterAccount, ActionDownloadCsvAccount, BodyDeleteAccount
)
from src.common.custom_router_class import LogRequest
from src.controllers.account_controller import AccountController
from src.helper.auth.handle_token import HandleToken

account_services_router = APIRouter(route_class=LogRequest)


@account_services_router.post(URI.ACCOUNT.LOGIN)
async def login(information_login: BodyLogin):
    return await AccountController().login(information_login.username, information_login.password)


@account_services_router.post(URI.ACCOUNT.REGISTER)
async def register(information_login: BodyRegister):
    return await AccountController().register(information_login)


@account_services_router.get(URI.ACCOUNT.DETAIL)
@HandleToken.verify_token
async def detail_account(access_token: str = Header(None)):
    return await AccountController().detail_account(access_token)


@account_services_router.put(URI.ACCOUNT.UPDATE_ACCOUNT)
@HandleToken.verify_token
async def update_account(account_id: str, request_body: UpdateAccount, access_token: str = Header(None)):
    return await AccountController().update_account(account_id, request_body)


@account_services_router.post(URI.ACCOUNT.RESET_PASSWORD)
# @HandleToken.verify_token
async def reset_password(request_body: ResetPassword):
    return await AccountController().reset_password(request_body)


@account_services_router.get(URI.ACCOUNT.RANDOM_CHOICE_IMAGE_UPLOAD)
# @HandleToken.verify_token
async def random_choice_image_upload():
    return await AccountController().random_choice_image_upload()


@account_services_router.post(URI.ACCOUNT.ACCOUNT_FILTER)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def account_action_filter(
        body: ActionFilterAccount,
        page: Optional[int] = Query(..., description="Page cần lấy dữ liệu"),
        per_page: Optional[int] = Query(..., description="Số lượng ảnh cần lấy trên 1 trang"),
        access_token: str = Header(None)
):
    return await AccountController().filter_account(body, page, per_page)


@account_services_router.post(URI.ACCOUNT.DELETE_ACCOUNT)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def delete_accounts(
        body: BodyDeleteAccount,
        access_token: str = Header(None)
):
    return await AccountController().delete_accounts(body)


@account_services_router.post(URI.ACCOUNT.ACCOUNT_DOWNLOAD_CSV)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def account_action_download_csv(
        body: ActionDownloadCsvAccount,
        access_token: str = Header(None)
):
    return await AccountController().download_csv_account_by_filter(body)
