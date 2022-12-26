#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydantic import Field, BaseModel


class BodyAddActivityHistory(BaseModel):
    device: str = Field(..., description="Thiết bị. Ví dụ: Mobile, PC")
    description: str = Field(..., description="Nội dung")
