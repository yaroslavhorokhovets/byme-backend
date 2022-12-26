#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field


class BodyUpsert(BaseModel):
    description: str = Field(..., description="Nội dung")