#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Header
from starlette.background import BackgroundTasks

from src.api.uri import URI
from src.base_model_request.base_model_request_meeting import AddRequestMeetingModel
from src.common.custom_router_class import LogRequest
from src.controllers.request_meeting_controller import RequestMeetingController
from src.helper.auth.handle_token import HandleToken

request_meeting_services_router = APIRouter(route_class=LogRequest)


@request_meeting_services_router.post(URI.REQUEST_MEETING.REQUEST_MEETING)
@HandleToken.verify_token
async def add_request_meeting(
        request_body: AddRequestMeetingModel,
        back_ground_tasks: BackgroundTasks,
        access_token: str = Header(None)):
    return await RequestMeetingController.add_request_meeting(request_body, access_token, back_ground_tasks)
