#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel, Field


class ImageRequestEditBody(BaseModel):
    image_ids: list = Field(..., description="Danh sách ID hình ảnh yêu cầu chỉnh sửa")
    note: str = Field(..., description="Ghi chú yêu cầu chỉnh sửa")
    express_delivery: bool = Field(False, description="Giao hoả tốc hay không?")


class DeleteFileBody(BaseModel):
    image_ids: list = Field(..., description="Danh sách ID hình ảnh cần xoá")


class DeleteFileTutorialBody(BaseModel):
    file_ids: list = Field(..., description="Danh sách ID file tutorial cần xoá")


class FilterFileBody(BaseModel):
    category_ids: list = Field(..., description="Danh sách ID danh mục cần lấy hình ảnh")
    root_category_id: str = Field(..., description="Root category ID")


class DownloadImageBody(BaseModel):
    ratio: Optional[str] = Field(..., description="Tỷ lệ ảnh muốn download")
    image_ids: list = Field(..., description="Danh sách ID hình ảnh muốn download")
