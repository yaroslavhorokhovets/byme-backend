#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 20/03/2022
"""
import logging
import os.path

import boto3
from botocore.exceptions import ClientError

from config import settings

logger = logging.getLogger(__name__)

'''
For Asynchronous Events
'''


class S3Service(object):

    def __init__(self):
        self.aws_access_key_id = settings.AWS_SERVER_PUBLIC_KEY
        self.aws_secret_access_key = settings.AWS_SERVER_SECRET_KEY
        self.bucket_name = settings.S3_BUCKET_NAME
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )

        bucket_location = self.s3.get_bucket_location(Bucket=self.bucket_name)
        if bucket_location:
            self.region = bucket_location['LocationConstraint']

    def upload_image(self, file_binary, folder, key_result, request_metadata):
        """Upload a file to an S3 bucket

        :param file_binary: Path File to upload
        :param folder: Folder save file in s3
        :param key_result: Key save s3
        :param request_metadata: Key save s3
        :return: True if file was uploaded, else False
        """
        try:
            key_save_s3 = os.path.join(folder, key_result)
            url = "https://{}.s3.{}.amazonaws.com/{}".format(self.bucket_name, self.region, key_save_s3)
            result = self.s3.put_object(
                Key=key_save_s3,
                Body=file_binary,
                Bucket=self.bucket_name,
                Metadata=request_metadata,
                ContentType="image/jpg")
            return url
        except ClientError as e:
            logging.error(e)
        return False

    def upload_file(self, file_binary, folder, key_result, request_metadata, mime_type):
        """Upload a file to an S3 bucket

        :param file_binary: Path File to upload
        :param folder: Folder save file in s3
        :param key_result: Key save s3
        :param request_metadata: Key save s3
        :param mime_type: Key save s3
        :return: True if file was uploaded, else False
        """
        try:
            key_save_s3 = os.path.join(folder, key_result)
            url = "https://{}.s3.{}.amazonaws.com/{}".format(self.bucket_name, self.region, key_save_s3)
            result = self.s3.put_object(
                Key=key_save_s3,
                Body=file_binary,
                Bucket=self.bucket_name,
                Metadata=request_metadata,
                ContentType=mime_type)
            return url
        except ClientError as e:
            logging.error(e)
        return False

    def download_file(self, filename, path):
        self.s3.download_file(self.bucket_name, filename, path)

    def delete_file(self, filepath):
        self.s3.delete_object(Bucket=self.bucket_name, key=filepath)

    def delete_multipath_file(self, lst_path_delete):
        response = self.s3.delete_objects(
            Bucket=self.bucket_name,
            Delete={"Objects": lst_path_delete},
        )
        print(response)
