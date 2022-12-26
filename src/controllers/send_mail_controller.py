#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from random import randint

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from starlette.background import BackgroundTasks

from src.api import build_message_susccess
from src.controllers import BaseController
from src.models.mongo.config_email_model import ConfigEmailModel


class SendMailController(BaseController):
    TEMPLATE_RESET_PASSWORD = """
        <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>[</span>施設名<span style='font-family:"Times New Roman",serif;'>]</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>ご担当者様</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>いつも<span style='font-family:"Times New Roman",serif;'>Byme</span>をご利用いただきありがとうございます。</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>セキュリティーコードは<span style='font-family:"Times New Roman",serif;'>***code***</span>です。</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>上記パセキュリティーコードでログインの上、パスワードを再設定してください。</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>今後とも<span style='font-family:"Times New Roman",serif;'>Byme</span>をよろしくお願いいたします。</p>
<div style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;'>
    <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;border:none;padding:0cm;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
</div>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>宿泊施設向け写真撮影アプリ「<span style='font-family:"Times New Roman",serif;'>Byme</span>（バイミ）」</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>お問い合わせ先</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><a href="mailto:info@app-byme.com"><span style='font-family:"Times New Roman",serif;'>info@app-byme.com</span></a></p>
    """

    async def set_config_email(self):
        config_email = await ConfigEmailModel().get_config_email()
        conf = ConnectionConfig(
            MAIL_USERNAME=config_email.get(ConfigEmailModel.MAIL_USERNAME),
            MAIL_PASSWORD=config_email.get(ConfigEmailModel.MAIL_PASSWORD),
            MAIL_FROM=config_email.get(ConfigEmailModel.MAIL_FROM),
            MAIL_PORT=config_email.get(ConfigEmailModel.MAIL_PORT),
            MAIL_SERVER=config_email.get(ConfigEmailModel.MAIL_SERVER),
            MAIL_FROM_NAME="info@app-byme.com",
            MAIL_TLS=True,
            MAIL_SSL=False,
            USE_CREDENTIALS=True,
            VALIDATE_CERTS=True
        )
        return conf

    async def send_email_reset_password(self, email, back_ground_tasks):
        email_to = email.email
        request_code, code = self.gen_hash_str_reset_email(email)
        conf = await self.set_config_email()
        message = MessageSchema(
            subject="【Byme】編集依頼を承りました info@app-byme.com",
            recipients=[email_to],  # List of recipients, as many as you can pass
            html=self.TEMPLATE_RESET_PASSWORD.replace("***code***", code),
            subtype="html"
        )
        fm = FastMail(conf)
        back_ground_tasks.add_task(fm.send_message, message)
        return build_message_susccess({
            "data": {
                "request_code": request_code
            }
        })

    async def send_to_emails(self, emails, html, subject, back_ground_tasks):
        conf = await self.set_config_email()
        message = MessageSchema(
            subject=subject,
            recipients=emails,  # List of recipients, as many as you can pass
            html=html,
            subtype="html"
        )
        fm = FastMail(conf)
        back_ground_tasks.add_task(fm.send_message, message)
        return

    @classmethod
    def gen_hash_str_reset_email(cls, email):
        code = "".join([str(randint(1, 9)) for _ in range(6)])
        identify = str(email.email) + str(code)
        return hashlib.md5(identify.encode()).hexdigest(), code
