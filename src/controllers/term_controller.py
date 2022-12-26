#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.api import build_message_susccess
from src.common.exception import CustomError
from src.controllers import BaseController
from src.models.mongo.term_model import TermModel


class TermController(BaseController):

    async def upsert(self, body):
        description = body.description
        if not description:
            raise CustomError("Description not null")
        term = await TermModel().collection.find_one({"type": "term"})
        if not term:
            await TermModel().collection.insert_one({"type": "term", "description": description})
        else:
            await TermModel().collection.update_one({"_id": term.get("_id")}, {"$set": {"description": description}})

        return build_message_susccess({"data": {"description": description}})

    async def get(self):
        term = await TermModel().collection.find_one({"type": "term"})
        return build_message_susccess(data={"data": {"description": term.get("description") if term else ""}})

    async def upsert_privacy_policy(self, body):
        description = body.description
        if not description:
            raise CustomError("Description not null")
        term = await TermModel().collection.find_one({"type": "privacy_policy"})
        if not term:
            await TermModel().collection.insert_one({"type": "privacy_policy", "description": description})
        else:
            await TermModel().collection.update_one({"_id": term.get("_id")}, {"$set": {"description": description}})

        return build_message_susccess({"data": {"description": description}})

    async def get_privacy_policy(self):
        term = await TermModel().collection.find_one({"type": "privacy_policy"})
        return build_message_susccess(data={"data": {"description": term.get("description") if term else ""}})
