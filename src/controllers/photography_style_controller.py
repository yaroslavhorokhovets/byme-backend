#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.api import build_message_susccess
from src.common.exception import CustomError
from src.controllers import BaseController
from src.models.mongo.photography_style_model import PhotographyStyleModel


class PhotographyStyleController(BaseController):

    @staticmethod
    async def insert_default():
        lst_type_category_id = await PhotographyStyleModel().insert_data_default()
        if lst_type_category_id:
            return build_message_susccess()
        raise CustomError("Photography Style default fail")
