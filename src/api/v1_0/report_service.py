#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Header, Query

from src.api.uri import URI
from src.common.custom_router_class import LogRequest
from src.controllers.report_controller import ReportController
from src.helper.auth.handle_token import HandleToken

report_service_router = APIRouter(route_class=LogRequest)


@report_service_router.get(URI.REPORT.REPORT)
@HandleToken.verify_token
async def report(
        start_time: str = Query(...,
                                description="Thời gian bắt đầu lấy báo cáo. Định dạnh %Y-%m-%d. Ví dụ: 2022-03-27"),
        end_time: str = Query(..., description="Thời gian kết thúc lấy báo cáo. Định dạnh %Y-%m-%d. Ví dụ: 2022-03-29"),
        access_token: str = Header(None)
):
    return await ReportController().report_home(start_time, end_time, access_token)


@report_service_router.get(URI.REPORT.REPORT_ADMIN)
@HandleToken.verify_token
async def report_admin(
        start_time: str = Query(...,
                                description="Thời gian bắt đầu lấy báo cáo. Định dạnh %Y-%m-%d. Ví dụ: 2022-03-27"),
        end_time: str = Query(..., description="Thời gian kết thúc lấy báo cáo. Định dạnh %Y-%m-%d. Ví dụ: 2022-03-29"),
        access_token: str = Header(None)
):
    return await ReportController().report_admin(start_time, end_time, access_token)
