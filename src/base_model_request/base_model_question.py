#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class AddQuestionBody(BaseModel):
    fullname: str = Field(..., description="Họ và tên")
    email: EmailStr = Field(..., description="Địa chỉ email")
    question: Optional[str] = Field(..., description="Câu hỏi")

