#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 22/03/2022
"""
from src.models.mongo import BaseModel


class ConfigEmailModel(BaseModel):
    MAIL_USERNAME = "mail_username"
    MAIL_PASSWORD = "mail_password"
    MAIL_FROM = "mail_from"
    MAIL_PORT = "mail_port"
    MAIL_SERVER = "mail_server"
    MAIL_FROM_NAME = "mail_from_name"
    MAIL_TLS = "mail_tls"
    MAIL_SSL = "mail_ssl"
    USE_CREDENTIALS = "use_credentials"
    VALIDATE_CERTS = "validate_certs"
    STATUS = "status"

    def __init__(self):
        super().__init__()
        self.collection = self.db["config_email"]

    async def get_config_email(self):
        filter_option = {
            self.STATUS: 1
        }
        return await self.collection.find_one(filter_option)