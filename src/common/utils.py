#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 28/03/2022
"""
import datetime


def convert_string_to_datetime(dt_string, format_value="%Y-%m-%d %H:%M:%S"):
    dt_object = datetime.datetime.strptime(dt_string, format_value)
    return dt_object


def convert_string_to_date(dt_string, format_value="%Y-%m-%d"):
    dt_object = datetime.datetime.strptime(dt_string, format_value)
    return dt_object
