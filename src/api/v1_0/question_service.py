#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Header
from starlette.background import BackgroundTasks

from src.api.uri import URI
from src.base_model_request.base_model_question import AddQuestionBody
from src.common.custom_router_class import LogRequest
from src.controllers.question_controller import QuestionController
from src.helper.auth.handle_token import HandleToken

question_services_router = APIRouter(route_class=LogRequest)


@question_services_router.post(URI.QUESTION.QUESTIONS)
@HandleToken.verify_token
async def add_question(
        request_body: AddQuestionBody,
        back_ground_tasks: BackgroundTasks,
        access_token: str = Header(None)):
    return await QuestionController.add_question(request_body, back_ground_tasks)
