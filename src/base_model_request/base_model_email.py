#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from pydantic import EmailStr, BaseModel


class SendEmailResetPassword(BaseModel):
    email: EmailStr
