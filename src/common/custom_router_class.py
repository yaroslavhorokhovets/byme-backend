#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 14/04/2022
"""
import time
from typing import Callable

from fastapi import Request, Response
from fastapi.routing import APIRoute

from src.common import logger
from src.common.exception import ConflictMessage


class LogRequest(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            from src.common.exception import CustomError
            logger.info(f"{request.method} {request.url}")
            if request.method != "GET":
                logger.info("Request body :: %s" % await request.body())
            before = time.time()
            try:
                response: Response = await original_route_handler(request)
            except CustomError as ex:
                logger.error(ex, exc_info=True)
                raise CustomError(str(ex))
            except ConflictMessage as ce:
                raise ConflictMessage(str(ce))
            except Exception as ex:
                logger.error(ex, exc_info=True)
                raise CustomError(str(ex))
            duration = time.time() - before
            logger.info("Time run: %s", duration)
            logger.info("Response: %s", response.body)
            return response

        return custom_route_handler
