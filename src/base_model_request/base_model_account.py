#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional, Union

from pydantic import BaseModel, Field, EmailStr

from src.common import PermissionAccount


class BodyLogin(BaseModel):
    username: str
    password: str


class Prices(BaseModel):
    price: dict = Field(0, description="Giá tiền")
    annual_usage_fee: float = Field(0, description="Phí sử dụng hàng năm")
    instant_delivery_request_fee: float = Field(0, description="Phí yêu cầu giao hàng ngay lập tức")


class BodyRegister(BaseModel):
    facility_name: str = Field("", description="Tên cơ sở")
    facility_code: str = Field("", description="Mã cơ sở")
    sales_staff: str = Field(..., description="Nhân viên bán hàng")
    password: str = Field(..., description="Mật khẩu")
    representative_name: str = Field(..., description="Tên người đại diện")
    email: EmailStr = Field(..., description="Email người đăng ký")
    postal_code: str = Field(..., description="Mã bưu điện")
    address: str = Field(..., description="Địa chỉ")
    phone_number: str = Field(..., description="Số điện thoại")
    fax_number: str = Field(..., description="Số Fax")
    ID_use: str = Field(..., description="ID sử dụng")
    type_base: str = Field("", description="Loại cơ sở")
    lst_buy: list = Field([], description="Danh sách sản phẩm muốn mua")
    price: float = Field(0, description="Giá tiền")
    annual_usage_fee: float = Field(0, description="Phí sử dụng hàng năm")
    instant_delivery_request_fee: float = Field(0, description="Phí yêu cầu giao hàng ngay lập tức")
    permission: Optional[str] = Field(
        PermissionAccount.USER,
        description="Quyền của account mặc định truyền lên thì sẽ là quyền User"
    )


class UpdateAccount(BaseModel):
    facility_name: str = Field(None, description="Tên cơ sở")
    facility_code: str = Field(None, description="Mã cơ sở")
    sales_staff: str = Field(None, description="Nhân viên bán hàng")
    password: str = Field(None, description="Mật khẩu")
    representative_name: str = Field(None, description="Tên người đại diện")
    email: EmailStr = Field(None, description="Email người đăng ký")
    postal_code: str = Field(None, description="Mã bưu điện")
    address: str = Field(None, description="Địa chỉ")
    phone_number: str = Field(None, description="Số điện thoại")
    fax_number: str = Field(None, description="Số Fax")
    ID_use: str = Field(None, description="ID sử dụng")
    type_base: str = Field("", description="Loại cơ sở")
    lst_buy: list = Field([], description="Danh sách sản phẩm muốn mua")
    price: float = Field(None, description="Giá tiền")
    annual_usage_fee: float = Field(None, description="Phí sử dụng hàng năm")
    instant_delivery_request_fee: float = Field(None, description="Phí yêu cầu giao hàng ngay lập tức")
    permission: Optional[str] = Field(
        PermissionAccount.USER,
        description="Quyền của account mặc định truyền lên thì sẽ là quyền User"
    )


class ResetPassword(BaseModel):
    email: EmailStr = Field(description="Email")
    request_code: str = Field(description="Mã request từ hệ thống")
    code: str = Field(description="Mã bảo vệ")
    new_password: str = Field(description="Mật khẩu mới")


class ActionFilterAccount(BaseModel):
    search: str = Field(None, description="Từ khoá cần tìm kếm")
    code_user: str = Field(None, description="Mã tài khoản cần tìm kiếm")


class BodyDeleteAccount(BaseModel):
    account_ids: list = Field(..., description="Danh sách account id cần xoá")


class ActionDownloadCsvAccount(BaseModel):
    search: str = Field(None, description="Từ khoá cần tìm kếm")
    code_user: str = Field(None, description="Mã tài khoản cần tìm kiếm")
    start_time: str = Field(None, description="Thời gian bắt đầu tìm kiếm. Ví dụ: 2022-04-22")
    end_time: str = Field(None, description="Thời gian kết túc tìm kiếm. Ví dụ: 2022-04-22")
