#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 20/05/2022
"""

from fastapi import APIRouter, UploadFile, Header, File, Query
from starlette.background import BackgroundTasks

from src.api.uri import URI
from src.base_model_request.base_model_invoice import UpdateInvoice, DownloadInvoice
from src.common.custom_router_class import LogRequest
from src.controllers.invoice_controller import InvoiceController
from src.helper.auth.handle_token import HandleToken

invoice_service_router = APIRouter(route_class=LogRequest)


@invoice_service_router.post(URI.INVOICE.UPLOAD_INVOICE)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def upload_invoice(
        back_ground_tasks: BackgroundTasks,
        file: UploadFile = File(...),
        access_token: str = Header(...)
):
    return await InvoiceController().upload_invoice(file, back_ground_tasks, access_token)


@invoice_service_router.get(URI.INVOICE.INVOICES)
@HandleToken.verify_token
async def lst_invoices(
        action_time: str = Query(None, description="Thời gian đối với account user"),
        page: int = Query(None),
        per_page: int = Query(None),
        access_token: str = Header(...)
):
    return await InvoiceController().lst_invoices(action_time, page, per_page, access_token)


@invoice_service_router.put(URI.INVOICE.INVOICE_DETAIL)
@HandleToken.verify_token
async def invoice_detail(
        invoice_id,
        request_body: UpdateInvoice,
        access_token: str = Header(...)
):
    return await InvoiceController().update_invoice(invoice_id, request_body)


@invoice_service_router.post(URI.INVOICE.DOWNLOAD_INVOICE)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def download_invoices(
        request_body: DownloadInvoice,
        access_token: str = Header(...)
):
    return await InvoiceController().download_invoices(request_body)


@invoice_service_router.post(URI.INVOICE.DOWNLOAD_INVOICE_USER)
@HandleToken.verify_token
@HandleToken.check_permission_user
async def download_invoices_user(
        access_token: str = Header(...)
):
    return await InvoiceController().download_invoices_user(access_token)
