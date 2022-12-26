#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel, Field


class AddCategory(BaseModel):
    name: str = Field(..., description="Tên của category")
    number_next_step: int = Field(..., description="Bước trước đó")
    root_category_id: str = Field(..., description="Định danh của thằng gốc")
    link_video_tutorial: Optional[str] = Field(None, description="Link video hướng dẫn")
    parent_id: Optional[str] = Field(None, description="Id của thằng cha")
    type_category_id: Optional[str] = Field(None, description="Loại danh mục được chọn")
    description: Optional[str] = Field(None, description="Mô tả")
    coordinates: Optional[list] = Field(..., description="Toạ độ khi tạo phòng")
    accuracy: Optional[float] = Field(..., description="Độ chính xác của toạ độ")


class UpdateCategory(BaseModel):
    name: Optional[str] = Field(..., description="Tên của category")
    link_video_tutorial: Optional[str] = Field(None, description="Link video hướng dẫn")
    coordinates: Optional[list] = Field(..., description="Toạ độ khi tạo phòng")
    accuracy: Optional[float] = Field(..., description="Độ chính xác của toạ độ")


class FilterCategory(BaseModel):
    number_next_step: int = Field(..., description="Bước hiện tại")
    root_category_id: Optional[str] = Field(None, description="Định danh của thằng gốc")
    code_root_category: Optional[str] = Field(None, description="Mã của của thằng gốc")
    parent_id: Optional[str] = Field(None, description="Id của thằng cha")
    search: Optional[str] = Field(None, description="Từ khoá tìm kiếm")


class ChildFilterImage(BaseModel):
    child_id: Optional[str] = Field(None, description="Child id")
    type_query: Optional[str] = Field(None, description="Loại query")
    account_ids: Optional[list] = Field([], description="Danh sach account duoc filter")
    start_time: Optional[str] = Field("", description="Thoi gian bat dau tim kiem. Vi du: 2022/04/06")
    end_time: Optional[str] = Field("", description="Thoi gian ket thuc tim kiem. Vi du: 2022/04/06")
    is_express_delivery: Optional[bool] = Field(False, description="Giao hoả tốc hay không? Mặc định là không")
