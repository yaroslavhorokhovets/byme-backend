#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Date: 20/03/2022
    Project: byme-api
"""
from datetime import datetime, timedelta
from typing import Optional

from jose import jwt

from config import settings
from src.common import AccessToken


class JwtHandler:
    EXPIRE = "expire"
    ACCESS_TOKEN = "access_token"
    ROLE = "role"
    FACILITY_NAME = "facility_name"

    def __init__(self):
        self.access_token_expire_day = int(settings.ACCESS_TOKEN_EXPIRE_DAY)
        self.algorithm = settings.ALGORITHM

    def signJWT(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(days=self.access_token_expire_day)
        to_encode.update({self.EXPIRE: expire.timestamp()})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=self.algorithm)
        return {
            self.ACCESS_TOKEN: AccessToken.PREFIX + encoded_jwt,
            self.ROLE: data.get("permission"),
            self.FACILITY_NAME: data.get(self.FACILITY_NAME)
        }
