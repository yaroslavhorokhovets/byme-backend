#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel, Field


class UpdateInvoice(BaseModel):
    username: Optional[str] = Field(description="username")
    day_request: Optional[str] = Field(description="Day request")
    day_transfer: Optional[str] = Field(description="Day transfer")
    big_project: Optional[str] = Field(description="Big project")
    small_project: Optional[str] = Field(description="Small project")
    quantity: Optional[str] = Field(description="Quantity")
    account_bank: Optional[str] = Field(description="Account Bank")
    branch: Optional[str] = Field(description="Branch")
    payee: Optional[int] = Field(description="payee")


class DownloadInvoice(BaseModel):
    invoice_ids: Optional[list] = Field(description="Danh sách invoice_id cần tải")

