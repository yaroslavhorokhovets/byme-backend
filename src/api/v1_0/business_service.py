#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Date: 20/03/2022
    Project: byme-api
"""
from typing import Optional

from fastapi import APIRouter, Header, Query

import sys
import json
from googleapiclient import sample_tools
from googleapiclient.http import build_http

from src.api.uri import URI
from src.base_model_request.base_model_business_account import BodyRegister, UploadRegister
from src.common.custom_router_class import LogRequest
from src.controllers.business_controller import BusinessController
from src.controllers.file_controller import FileController
from src.helper.auth.handle_token import HandleToken
import requests

business_service_router = APIRouter(route_class=LogRequest)

@business_service_router.get(URI.BUSINESS.BUSINESS_ACCOUNTS)
# @HandleToken.verify_token
async def accounts():
    # Use the discovery doc to build a service that we can use to make
    # MyBusiness API calls, and authenticate the user so we can access their
    # account
    discovery_doc = "./client_secrets.json"
    MyBusinessAccount, flags = sample_tools.init(sys.argv, "mybusinessaccountmanagement", "v1", __doc__, __file__, scope="https://www.googleapis.com/auth/business.manage", discovery_filename=discovery_doc)
    
    # Get the list of accounts the authenticated user has access to
    output = MyBusinessAccount.accounts().list().execute()
    
    print("List of Accounts:\n")
    print(json.dumps(output, indent=2) + "\n")
    
    return await BusinessController().add_account()

@business_service_router.post(URI.BUSINESS.BUSINESS_STORE_ACCOUNTS)
@HandleToken.verify_token
async def store(request_body: BodyRegister, access_token: str = Header(None)):
    return await BusinessController().add_account(request_body, access_token)

@business_service_router.get(URI.BUSINESS.BUSINESS_GET_ACCOUNTS)
@HandleToken.verify_token
async def get(access_token: str = Header(None)):
    return await BusinessController().get_business_account(access_token)

@business_service_router.put(URI.BUSINESS.BUSINESS_CLOSE_ACCOUNTS)
@HandleToken.verify_token
async def close(access_token: str = Header(None)):
    return await BusinessController().update_account(access_token)

@business_service_router.put(URI.BUSINESS.BUSINESS_UPLOAD_IMAGES)
@HandleToken.verify_token
async def upload(request_body: UploadRegister, access_token: str = Header(None)):
    return await FileController().upload_google(request_body, access_token)

@business_service_router.delete(URI.BUSINESS.BUSINESS_DELETE_ACCOUNTS)
@HandleToken.verify_token
async def delete(access_token: str = Header(None)):
    return await BusinessController().delete_account(access_token)