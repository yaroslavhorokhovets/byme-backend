#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.models.mongo import BaseModel


class TermModel(BaseModel):

    def __init__(self):
        super().__init__()
        self.collection = self.db["term"]