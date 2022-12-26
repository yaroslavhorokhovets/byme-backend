from fastapi import APIRouter

from src.api import try_except_response, build_message_susccess
from src.api.uri import URI
from src.common.custom_router_class import LogRequest

check_services_router = APIRouter(route_class=LogRequest)


@check_services_router.get(URI.PING)
def check_services():
    return build_message_susccess("request full successes!!!")
