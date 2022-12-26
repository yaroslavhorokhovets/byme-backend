#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Header, Query

from src.api.uri import URI
from src.base_model_request.base_model_push_notification import BodyAddNotificationEmail, BodyUpdateNotificationEmail, \
    BodyAddNotificationWeb, BodyUpdateNotificationWeb
from src.common.custom_router_class import LogRequest
from src.controllers.push_notification_controller import PushNotificationController
from src.helper.auth.handle_token import HandleToken

push_notification_service_router = APIRouter(route_class=LogRequest)


@push_notification_service_router.post(URI.PUSH_NOTIFICATION.PUSH_NOTIFICATION_EMAIL)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def add_notification_email(body: BodyAddNotificationEmail, access_token: str = Header(None)):
    return await PushNotificationController().add_push_notification(body, "email", access_token)


@push_notification_service_router.get(URI.PUSH_NOTIFICATION.PUSH_NOTIFICATION_EMAIL)
@HandleToken.verify_token
async def lst_notification_email(
        page: int = Query(None),
        per_page: int = Query(None),
        access_token: str = Header(...)
):
    return await PushNotificationController().lst_push_notification(page, per_page, "email", access_token)


@push_notification_service_router.put(URI.PUSH_NOTIFICATION.PUSH_NOTIFICATION_EMAIL_DETAIL)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def update_notification_email(
        push_id,
        body: BodyUpdateNotificationEmail,
        access_token: str = Header(...)
):
    return await PushNotificationController().update_push_notification(push_id, body, "email", access_token)


@push_notification_service_router.delete(URI.PUSH_NOTIFICATION.PUSH_NOTIFICATION_EMAIL_DETAIL)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def delete_notification_email(
        push_id,
        access_token: str = Header(...)
):
    return await PushNotificationController().delete_push_notification(push_id, access_token)


@push_notification_service_router.post(URI.PUSH_NOTIFICATION.PUSH_NOTIFICATION_WEB)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def add_notification_web(body: BodyAddNotificationWeb, access_token: str = Header(None)):
    return await PushNotificationController().add_push_notification(body, "web", access_token)


@push_notification_service_router.get(URI.PUSH_NOTIFICATION.PUSH_NOTIFICATION_WEB)
@HandleToken.verify_token
async def lst_notification_web(
        page: int = Query(None),
        per_page: int = Query(None),
        access_token: str = Header(...)
):
    return await PushNotificationController().lst_push_notification(page, per_page, "web", access_token)


@push_notification_service_router.put(URI.PUSH_NOTIFICATION.PUSH_NOTIFICATION_WEB_DETAIL)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def update_notification_web(
        push_id,
        body: BodyUpdateNotificationWeb,
        access_token: str = Header(...)
):
    return await PushNotificationController().update_push_notification(push_id, body, "web", access_token)


@push_notification_service_router.delete(URI.PUSH_NOTIFICATION.PUSH_NOTIFICATION_WEB_DETAIL)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def delete_notification_web(
        push_id,
        access_token: str = Header(...)
):
    return await PushNotificationController().delete_push_notification(push_id, access_token)
