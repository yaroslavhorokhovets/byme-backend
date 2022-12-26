#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Header

from src.api.uri import URI
from src.base_model_request.base_model_term import BodyUpsert
from src.common.custom_router_class import LogRequest
from src.controllers.term_controller import TermController
from src.helper.auth.handle_token import HandleToken

terms_service_router = APIRouter(route_class=LogRequest)


@terms_service_router.put(URI.TERMS_OF_USE_AND_PRIVACY_POLICY.TERMS_OF_USE)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def upsert_terms(body: BodyUpsert, access_token: str = Header(None)):
    return await TermController().upsert(body)


@terms_service_router.get(URI.TERMS_OF_USE_AND_PRIVACY_POLICY.TERMS_OF_USE)
@HandleToken.verify_token
async def get_terms(access_token: str = Header(None)):
    return await TermController().get()


@terms_service_router.put(URI.TERMS_OF_USE_AND_PRIVACY_POLICY.PRIVACY_POLICY)
@HandleToken.verify_token
@HandleToken.check_permission_admin
async def upsert_privacy_policy(body: BodyUpsert, access_token: str = Header(None)):
    return await TermController().upsert_privacy_policy(body)


@terms_service_router.get(URI.TERMS_OF_USE_AND_PRIVACY_POLICY.PRIVACY_POLICY)
@HandleToken.verify_token
async def get_privacy_policy(access_token: str = Header(None)):
    return await TermController().get_privacy_policy()
