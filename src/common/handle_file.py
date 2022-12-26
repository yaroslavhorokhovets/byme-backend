#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 07/04/2022
"""
from io import BytesIO

import requests
from PIL import Image


def resize_image_by_url(url, filename, ratio=None):
    w = 1
    h = 1
    if ratio:
        w = int(ratio.split("x")[0])
        h = int(ratio.split("x")[1])
    path = filename
    image = Image.open(BytesIO(requests.get(url).content))
    width, height = image.size
    height_new = (height * w) // h
    size_new = (width, height)
    if height_new > height:
        width_new = (width * w) // h
        size_new = (width_new, height)
    image = image.resize(size_new, Image.ANTIALIAS)
    image.save(path)
    return path
