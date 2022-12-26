#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.api import build_message_susccess
from src.common import QuestionConstant
from src.common.exception import CustomError
from src.controllers import BaseController
from src.controllers.send_mail_controller import SendMailController
from src.helper.auth.handle_token import HandleToken
from src.models.mongo.account_model import AccountModel
from src.models.mongo.question_model import QuestionModel


class QuestionController(BaseController):

    @staticmethod
    async def add_question(request_body, back_ground_tasks):
        fullname = request_body.fullname
        email = request_body.email
        question = request_body.question
        emails = [email]
        html = QuestionController.build_html_send_question(fullname, request_body.email, question)
        await SendMailController().send_to_emails(emails, html, "お問い合わせ", back_ground_tasks)
        return build_message_susccess()

    @staticmethod
    def build_html_send_question(fullname, email, question):
        HTML_STR = """
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>【<span style='font-family:"Times New Roman",serif;'>Byme</span>】お問い合わせを受け付けました</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><a href="mailto:info@app-byme.com"><span style='font-family:"Times New Roman",serif;'>info@app-byme.com</span></a></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>[</span>施設名<span style='font-family:"Times New Roman",serif;'>]</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>{fullname} 様</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>いつも<span style='font-family:"Times New Roman",serif;'>Byme</span>をご利用いただきありがとうございます。</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>以下のお問い合わせを受け付けました。</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>確認次第担当者よりご連絡いたします。</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>３営業日経過後も連絡がない場合、恐れ入りますが再送いただきますようお願いいたします。</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>【お問い合わせ内容】</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>{question}<span style="font-family:&quot;Times New Roman&quot;,serif;"></span><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>今後とも<span style='font-family:"Times New Roman",serif;'>Byme</span>をよろしくお願いいたします。</p>
<div style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;'>
    <p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;border:none;padding:0cm;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
</div>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><span style='font-family:"Times New Roman",serif;'>&nbsp;</span></p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>宿泊施設向け写真撮影アプリ「<span style='font-family:"Times New Roman",serif;'>Byme</span>（バイミ）」</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'>お問い合わせ先</p>
<p style='margin:0cm;text-align:justify;font-size:14px;font-family:"Yu Mincho",serif;'><a href="mailto:info@app-byme.com"><span style='font-family:"Times New Roman",serif;'>info@app-byme.com</span></a></p>
<hr>
        """
        return HTML_STR.format(
            fullname=fullname,
            question=question
        )
