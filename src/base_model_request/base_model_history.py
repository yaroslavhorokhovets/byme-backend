#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 29/06/2022
"""
from typing import Optional

from pydantic import BaseModel, Field


class FilterHistoryImage(BaseModel):
    account_ids: Optional[list] = Field([], description="Danh sach account duoc filter")
    start_time: Optional[str] = Field("", description="Thoi gian bat dau tim kiem. Vi du: 2022/04/06")
    end_time: Optional[str] = Field("", description="Thoi gian ket thuc tim kiem. Vi du: 2022/04/06")
