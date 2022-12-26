#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class BodyRegister(BaseModel):
    email: EmailStr = Field(..., description="Email người đăng ký")
    status: int = Field(..., description="trạng thái")
    name: str = Field("", description="Tên thuê bao")
    family_name: str = Field("", description="Họ tên thuê bao")
    given_name: str = Field("", description="Tên thuê bao")
    email_verified: bool = Field("", description="Email đã kích hoạt")
    iat: int = Field("", description="iat")
    sub: str = Field("", description="sub")
    exp: int = Field("", description="Ngày hết hạn")
    aud: str = Field("", description="kiểm toán viên")
    azp: str = Field("", description="azp")
    jti: str = Field("", description="jti")
    nbf: int = Field("", description="nbf")
    iss: str = Field("", description="iss")
    picture: str = Field("", description="Nình ảnh")
    access_token: str = Field("", description="Truy cập thẻ")
    refresh_token: str = Field("", description="làm mới mã thông báo")
    account_id: Optional[str] = Field(None, description="Id của tài khoản")

class UploadRegister(BaseModel):
    image_id: str = Field("", description="Tên thuê bao")
    google_status: int = Field(0, description="Họ tên thuê bao")