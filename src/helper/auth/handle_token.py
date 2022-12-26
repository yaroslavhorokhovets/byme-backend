#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from functools import wraps

from jose import jwt
from pydantic import ValidationError

from config import settings
from src.common import CommonToken, AccessToken
from src.common.exception import Unauthorized, InputParamError


class HandleToken(object):

    @staticmethod
    def verify_token(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                token = kwargs.get("access_token", "").replace(AccessToken.PREFIX, '').replace('"', '')
                payload = jwt.decode(
                    token,
                    settings.SECRET_KEY,
                    algorithms=[settings.ALGORITHM]
                )
                if payload.get(CommonToken.EXPIRE) < datetime.datetime.utcnow().timestamp():
                    raise InputParamError("Token expired")
                return await func(*args, **kwargs)
            except Exception as e:
                raise InputParamError(str(e))

        return wrapper

    @staticmethod
    def check_permission_admin(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                token = kwargs.get("access_token", "").replace(AccessToken.PREFIX, '').replace('"', '')
                payload = jwt.decode(
                    token,
                    settings.SECRET_KEY,
                    algorithms=[settings.ALGORITHM]
                )
                if not payload.get("permission") or payload.get("permission") != "admin":
                    raise Unauthorized("You not permission")
                return await func(*args, **kwargs)
            except Exception as e:
                raise Unauthorized(str(e))

        return wrapper

    @staticmethod
    def check_permission_user(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                token = kwargs.get("access_token", "").replace(AccessToken.PREFIX, '').replace('"', '')
                payload = jwt.decode(
                    token,
                    settings.SECRET_KEY,
                    algorithms=[settings.ALGORITHM]
                )
                if not payload.get("permission") or payload.get("permission") == "admin":
                    raise Unauthorized("You not permission")
                return await func(*args, **kwargs)
            except Exception as e:
                raise Unauthorized(str(e))

        return wrapper

    @staticmethod
    def get_param_by_token(param, access_token):
        try:
            token = access_token.replace(AccessToken.PREFIX, '').replace('"', '')
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )
            return payload.get(param)
        except(jwt.JWSError, ValidationError):
            raise Unauthorized("Could not validate credentials")
