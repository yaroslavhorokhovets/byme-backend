#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio

import motor.motor_asyncio

from config import settings

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
mongo_client.get_io_loop = asyncio.get_running_loop
class BaseModel(object):

    def __init__(self):
        self.db = mongo_client.get_default_database()