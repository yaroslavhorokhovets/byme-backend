from src.api import app
from src.api.v1_0.account_service import account_services_router
from src.api.v1_0.category_service import category_service_router
from src.api.v1_0.check_services import check_services_router
from src.api.v1_0.file_service import file_service_router
from src.api.v1_0.history_service import history_service_router
from src.api.v1_0.invoice_service import invoice_service_router
from src.api.v1_0.notification_account_service import notification_account_service_router
from src.api.v1_0.photography_style_service import photography_style_service_router
from src.api.v1_0.push_notification_service import push_notification_service_router
from src.api.v1_0.question_service import question_services_router
from src.api.v1_0.report_service import report_service_router
from src.api.v1_0.request_meeting_service import request_meeting_services_router
from src.api.v1_0.send_email_service import send_email_service_router
from src.api.v1_0.terms_service import terms_service_router
from src.api.v1_0.type_category_service import type_category_service_router

from src.api.v1_0.business_service import business_service_router

api_prefix = "/api/v1.0"

app.include_router(router=check_services_router, prefix=api_prefix)
app.include_router(router=account_services_router, prefix=api_prefix)
app.include_router(router=category_service_router, prefix=api_prefix)
app.include_router(router=file_service_router, prefix=api_prefix)
app.include_router(router=send_email_service_router, prefix=api_prefix)
app.include_router(router=photography_style_service_router, prefix=api_prefix)
app.include_router(router=type_category_service_router, prefix=api_prefix)
app.include_router(router=question_services_router, prefix=api_prefix)
app.include_router(router=report_service_router, prefix=api_prefix)
app.include_router(router=request_meeting_services_router, prefix=api_prefix)
app.include_router(router=history_service_router, prefix=api_prefix)
app.include_router(router=invoice_service_router, prefix=api_prefix)
app.include_router(router=terms_service_router, prefix=api_prefix)
app.include_router(router=push_notification_service_router, prefix=api_prefix)
app.include_router(router=notification_account_service_router, prefix=api_prefix)

app.include_router(router=business_service_router, prefix=api_prefix)