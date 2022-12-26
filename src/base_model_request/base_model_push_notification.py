#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydantic import Field, BaseModel


class BodyAddNotificationEmail(BaseModel):
    action_time: str = Field(..., description="Thời gian thực hiện gửi thông báo. Ví dụ: 2022-05-31T00:01Z")
    title: str = Field(..., description="Tiêu đề")
    url: str = Field(..., description="URL")
    description: str = Field(..., description="Nội dung")


class BodyUpdateNotificationEmail(BaseModel):
    description: str = Field(..., description="Nội dung")


class BodyAddNotificationWeb(BaseModel):
    action_time: str = Field(..., description="Thời gian thực hiện gửi thông báo. Ví dụ: 2022-05-31T00:01Z")
    title: str = Field(..., description="Tiêu đề")
    url: str = Field(..., description="URL")
    description: str = Field(..., description="Nội dung")


class BodyUpdateNotificationWeb(BaseModel):
    description: str = Field(..., description="Nội dung")
