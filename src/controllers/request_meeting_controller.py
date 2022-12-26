#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from src.api import build_message_susccess
from src.common import EmailContact
from src.controllers import BaseController
from src.controllers.send_mail_controller import SendMailController
from src.helper.auth.handle_token import HandleToken
from src.models.mongo.account_model import AccountModel


class RequestMeetingController(BaseController):

    @staticmethod
    async def add_request_meeting(request_body, access_token, back_ground_tasks):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        data_insert = request_body.dict(exclude_unset=True)
        data_insert.update({
            "account_id": account_id,
            "created_time": datetime.datetime.utcnow()
        })

        emails = [data_insert.get("email")]
        html = RequestMeetingController.build_html_send_request_meeting(data_insert)
        await SendMailController().send_to_emails(emails, html, "【Byme】勉強会依頼を承りました", back_ground_tasks)
        return build_message_susccess()

    @staticmethod
    def build_html_send_request_meeting(request_body):
        HTML_STR = """
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>【<span style='font-family:"Times New Roman",serif;'>Byme</span>】勉強会依頼を承りました</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'></span>{facility_name}<span style='font-family:"Times New Roman",serif;'></span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>{person_charge} 様</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>いつも<span style='font-family:"Times New Roman",serif;'>Byme</span>をご利用いただきありがとうございます。</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>勉強会依頼を承りました。</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>弊社担当より３営業日以内にご連絡させていただきます。</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>今しばらくお待ちくださいませ。</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>【お問い合わせ内容】</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>{desired_schedule}</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>今後とも<span style='font-family:"Times New Roman",serif;'>Byme</span>をよろしくお願いいたします。</p>
<hr>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>宿泊施設向け写真撮影アプリ「<span style='font-family:"Times New Roman",serif;'>Byme</span>（バイミ）」</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>お問い合わせ先</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><a href="mailto:info@app-byme.com"><span style='font-family:"Times New Roman",serif;'>info@app-byme.com</span></a></p>
<hr>
        """
        return HTML_STR.format(
            facility_name=request_body.get("facility_name"),
            person_charge=request_body.get("person_charge"),
            phone_number=request_body.get("phone_number"),
            email=request_body.get("email"),
            desired_schedule=request_body.get("desired_schedule"),
        )
