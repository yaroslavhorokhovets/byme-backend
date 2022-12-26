#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class AddRequestMeetingModel(BaseModel):
    facility_name: str = Field(..., description="Tên cơ sở")
    person_charge: str = Field(..., description="Người phụ trách")
    phone_number: str = Field(..., description="Số điện thoại")
    email: EmailStr = Field(..., description="Địa chỉ email")
    desired_schedule: Optional[str] = Field(..., description="Lịch trình mong muốn")