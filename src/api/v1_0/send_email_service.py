#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter, Header, BackgroundTasks

from src.api.uri import URI
from src.base_model_request.base_model_email import SendEmailResetPassword
from src.common.custom_router_class import LogRequest
from src.controllers.send_mail_controller import SendMailController
from src.helper.auth.handle_token import HandleToken

send_email_service_router = APIRouter(route_class=LogRequest)


@send_email_service_router.post(URI.EMAIL.SEND_EMAIL_RESET_PASSWORD)
# @HandleToken.verify_token
async def send_email_reset_password(
        email: SendEmailResetPassword, back_ground_tasks: BackgroundTasks
):
    return await SendMailController().send_email_reset_password(email, back_ground_tasks)
