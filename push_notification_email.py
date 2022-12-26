#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import datetime
import logging
import time

import aioschedule as schedule
from starlette.background import BackgroundTasks

from src.common import PermissionAccount
from src.controllers.send_mail_controller import SendMailController
from src.models.mongo.account_model import AccountModel
from src.models.mongo.push_notification_model import PushNotificationModel


def build_html_send_notification(description):
    HTML_STR = f"""
            <br>Description: {description}
    """
    return HTML_STR


async def push_notification_email():
    background = BackgroundTasks()
    logging.error("Start")
    time_now = datetime.datetime.utcnow()
    lst_notification = await PushNotificationModel().filter_by_option(
        {
            "action_time": {"$lte": time_now},
            "type": "email",
            "status_send": "unsent"
        }
    )
    if not lst_notification:
        return
    lst_email_user = await AccountModel().collection.distinct("email", {"permission": PermissionAccount.USER})
    async for notification in lst_notification:
        notification_id = notification.get("_id")
        html = build_html_send_notification(notification["description"])
        await SendMailController().send_to_emails(lst_email_user, html, "Notification", background)
        await PushNotificationModel().update_push_notification_by_id(notification_id, {"status_send": "sent"})
    return


loop = asyncio.get_event_loop()

if __name__ == '__main__':
    schedule.every(1).minutes.do(
        push_notification_email
    )

    while True:
        time.sleep(0.2)
        loop.run_until_complete(schedule.run_pending())
