#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import mimetypes
import os
import uuid
from datetime import datetime, timedelta
from zipfile import ZipFile

from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.api import build_message_susccess
from src.common import FolderUpload, FileConstant, PermissionAccount
from src.common.exception import CustomError
from src.common.handle_file import resize_image_by_url
from src.common.utils import convert_string_to_date
from src.controllers import BaseController
from src.helper.auth.handle_token import HandleToken
from src.helper.s3 import S3Service
from src.models.mongo.file_model import FileModel
from src.models.mongo.report_image_model import ReportImageModel


class FileController(BaseController):

    @staticmethod
    async def upload_image(file, root_category_id, category_id, coordinates, access_token):
        if not file:
            raise CustomError("File not exit")
        account_id = HandleToken().get_param_by_token("_id", access_token)
        mime_type = file.content_type
        extension_file = mimetypes.guess_extension(mime_type)
        filename = str(ObjectId()) + ".jpg"
        request_metadata = {
            "Content-Type": mime_type
        }
        result = S3Service().upload_image(file.file, FolderUpload.TEST, filename, request_metadata)
        if result:
            image_id = ObjectId()
            data_insert = {
                "_id": image_id,
                "account_id": account_id,
                "root_category_id": ObjectId(root_category_id),
                "category_id": ObjectId(category_id),
                "filename": filename,
                "folder": FolderUpload.TEST,
                "status": FileConstant.StatusFile.ACTIVE,
                "status_request": FileConstant.StatusRequest.UPLOAD,
                "origin_url": result,
                "edit_url": "",
                "google_status": 0,
                "location": {
                    "type": "Point",
                    "coordinates": coordinates
                },
                "type": "image",
                "action_time": datetime.utcnow()
            }
            file_id = await FileModel().add_file(data_insert)
            print("file_id: " + str(file_id))
            data_insert_report = {
                "image_id": image_id,
                "root_category_id": root_category_id,
                "category_id": category_id,
                "account_id": account_id,
                "url": result,
                "status": "upload",
                "action_time": datetime.utcnow()
            }
            report_id = await ReportImageModel().add_data(data_insert_report)
            print("report_id: " + str(report_id))

        return build_message_susccess({
            "data": result
        })

    @staticmethod
    async def upload_google(request_body, access_token):
        update_data = {
            'google_status': request_body.google_status
        }
        status_update = await FileModel().upload_google(request_body.image_id, update_data)
        if status_update.matched_count > 0:
            return build_message_susccess()
        raise CustomError("Google upload fail")

    @staticmethod
    async def override_image(file, image_id, access_token):
        if not file:
            raise CustomError("File not exit")
        account_id = HandleToken().get_param_by_token("_id", access_token)
        mime_type = file.content_type
        extension_file = mimetypes.guess_extension(mime_type)
        filename = str(ObjectId()) + extension_file
        request_metadata = {
            "Content-Type": mime_type
        }
        result = S3Service().upload_image(file.file, FolderUpload.TEST, filename, request_metadata)
        if result:
            status_update = await FileModel().override_image(image_id=image_id, link_file=result)
        return {
            "data": result
        }

    @staticmethod
    async def upload_file(file, folder):
        if not file:
            raise CustomError("File not exit")
        mime_type = file.content_type
        extension_file = mimetypes.guess_extension(mime_type)
        filename = str(ObjectId()) + extension_file
        request_metadata = {
            "Content-Type": mime_type
        }
        result = S3Service().upload_file(file.file, folder, filename, request_metadata, mime_type)
        return build_message_susccess({
            "data": result
        })

    @staticmethod
    async def image_request_edit(request_body):
        image_ids = request_body.image_ids
        note = request_body.note
        express_delivery = request_body.express_delivery

        image_ids = [ObjectId(image_id) for image_id in image_ids]
        filter_update = {
            "_id": {
                "$in": image_ids
            }
        }
        data_update = {
            "status_request": FileConstant.StatusRequest.PENDING,
            "note": note,
            "express_delivery": express_delivery
        }
        data_report_request_image = []
        lst_image = FileModel().collection.find(filter_update)
        async for image in lst_image:
            if not image.get("root_category_id"):
                continue
            data_inserts = [
                {
                    "image_id": image["_id"],
                    "root_category_id": image["root_category_id"],
                    "category_id": image["category_id"],
                    "account_id": image["account_id"],
                    "url": image["origin_url"],
                    "status": "upload",
                    "action_time": datetime.utcnow()
                },
                {
                    "image_id": image["_id"],
                    "root_category_id": image["root_category_id"],
                    "category_id": image["category_id"],
                    "account_id": image["account_id"],
                    "url": image["origin_url"],
                    "status": "pending",
                    "express_delivery": express_delivery,
                    "action_time": datetime.utcnow()
                }
            ]
            data_report_request_image.extend(data_inserts)
        if not data_report_request_image:
            raise CustomError("Not find image")
        file_ids = await ReportImageModel().collection.insert_many(data_report_request_image)
        print("file_ids: " + str(file_ids))

        status_update = await FileModel().collection.update_many(filter_update, {"$set": data_update})
        if status_update.matched_count > 0:
            return build_message_susccess()
        raise CustomError("Request edit image fail!")

    @staticmethod
    async def delete_images(request_body):
        image_ids = request_body.image_ids
        image_ids = [ObjectId(image_id) for image_id in image_ids]
        filter_delete = {
            "_id": {
                "$in": image_ids
            }
        }

        data_update = {
            "status": FileConstant.StatusFile.DELETE
        }
        status_update = await FileModel().collection.update_many(filter_delete, {"$set": data_update}, upsert=True)
        if status_update.matched_count > 0:
            return build_message_susccess()
        raise CustomError("Delete image fail!")

    @staticmethod
    async def delete_file_tutorial(request_body):
        file_ids = request_body.file_ids
        file_ids = [ObjectId(file_id) for file_id in file_ids]
        filter_delete = {
            "_id": {
                "$in": file_ids
            }
        }
        multi_filepath_delete = []
        all_file_delete = FileModel().collection.find(filter_delete)
        async for file in all_file_delete:
            folder = file.get('folder')
            filename = file.get("filename")
            if folder:
                filepath = os.path.join(folder, filename)
            else:
                filepath = filename
            multi_filepath_delete.append(
                {
                    "Key": filepath
                }
            )
        if multi_filepath_delete:
            S3Service().delete_multipath_file(multi_filepath_delete)
        status_update = await FileModel().collection.delete_many(filter_delete)
        if status_update.deleted_count > 0:
            return build_message_susccess()
        raise CustomError("Delete file tutorial fail!")

    @staticmethod
    async def filter_image(request_body, page, per_page, access_token):
        category_ids = request_body.category_ids
        root_category_id = request_body.root_category_id

        category_ids = [ObjectId(category_id) for category_id in category_ids]

        filter_option = {
            "category_id": category_ids,
            "root_category_id": root_category_id
        }
        count = await FileModel().collection.count_documents(filter_option)
        total_page = math.ceil(count / per_page)
        files = await FileModel().find_paginate(filter_option, page, per_page, sort_option=[("action_time", -1)])
        result = []
        page_data = {
            "total_count": count,
            "total_page": total_page,
            "page": page,
            "per_page": per_page
        }
        async for file in files:
            data = jsonable_encoder(file, custom_encoder={ObjectId: str})
            data["url"] = data["origin_url"]
            result.append(data)
        return build_message_susccess(
            data=result,
            page=page_data
        )

    @staticmethod
    async def download_image(request_body, access_token):
        ratio = request_body.ratio
        image_ids = request_body.image_ids

        if not image_ids:
            return build_message_susccess({})

        image_ids = [ObjectId(image_id) for image_id in image_ids]

        filter_option = {
            "_id": {
                "$in": image_ids
            },
        }

        field_show = {"_id": 0, "origin_url": 1, "edit_url": 1, "filename": 1}
        lst_image = FileModel().collection.find(filter_option, field_show)
        lst_path = []
        async for image in lst_image:
            origin_url = image["origin_url"]
            edit_url = image["edit_url"]
            filename = image["filename"]

            url = origin_url if not edit_url else edit_url
            path = resize_image_by_url(url, filename, ratio=ratio)
            lst_path.append(path)
        file_download = "DownloadImage.zip"
        with ZipFile(file_download, 'w') as zip:
            # writing each file one by one
            for file in lst_path:
                zip.write(file)
                os.remove(file)
        request_metadata = {
            "Content-Type": "application/zip"
        }
        result = S3Service().upload_file(
            open(file_download, "rb"),
            FolderUpload.TEST,
            file_download,
            request_metadata,
            "application/zip"
        )
        if result:
            os.remove(file_download)
        return build_message_susccess({
            "data": result
        })

    @staticmethod
    async def history_request_image(request_body, tab, page, per_page, access_token):
        account_id = HandleToken().get_param_by_token("_id", access_token)
        permission = HandleToken().get_param_by_token("permission", access_token)
        filter_option = {
            "type": "image"
        }
        mapping_filter = {
            "before_upload": {
                "status_request": "upload"
            },
            "pending": {
                "status_request": "pending"
            },
            "edited": {
                "status_request": "edit"
            }
        }
        if permission == PermissionAccount.USER:
            filter_option.update({
                "account_id": account_id,
            })
            if tab and mapping_filter.get(tab):
                filter_option.update(mapping_filter.get(tab))
        if permission == PermissionAccount.ADMIN:
            account_ids = request_body.account_ids
            start_time = request_body.start_time
            end_time = request_body.end_time
            try:
                start_time = convert_string_to_date(start_time, "%Y-%m-%dT%H:%M:%S.%fZ")
                end_time = convert_string_to_date(end_time, "%Y-%m-%dT%H:%M:%S.%fZ") + timedelta(days=1)
            except Exception as e:
                raise CustomError(str(e))
            filter_option.update({
                "$and": [
                    {
                        "action_time": {"$gte": start_time}
                    },
                    {
                        "action_time": {"$lte": end_time}
                    }
                ]
            })
            if account_ids:
                filter_option.update({
                    "account_id": {
                        "$in": account_ids
                    }
                })
        count = await FileModel().collection.count_documents(filter_option)
        total_page = math.ceil(count / per_page)
        files = await FileModel().find_paginate(filter_option, page, per_page, sort_option=[("action_time", -1)])
        result = []
        page_data = {
            "total_count": count,
            "total_page": total_page,
            "page": page,
            "per_page": per_page
        }
        async for file in files:
            data = jsonable_encoder(file, custom_encoder={ObjectId: str})
            data["image_id"] = data["_id"]
            data["url"] = data["origin_url"]
            result.append(data)
        return build_message_susccess(
            data=result,
            page=page_data
        )

    @staticmethod
    async def upload_tutorial(file, format_tutorial, access_token):
        permission = HandleToken().get_param_by_token("permission", access_token)
        if permission != "admin":
            raise CustomError("No permission upload file tutorial!")
        if not file:
            raise CustomError("File not exit")
        account_id = HandleToken().get_param_by_token("_id", access_token)
        mime_type = file.content_type
        filename_origin = file.filename
        extension_file = mimetypes.guess_extension(mime_type)
        filename_origin = filename_origin.replace(extension_file, "")
        filename = filename_origin + "_" + str(uuid.uuid1())[:8] + extension_file
        request_metadata = {
            "Content-Type": mime_type
        }
        result = S3Service().upload_file(file.file, FolderUpload.TUTORIAL, filename, request_metadata, mime_type)
        if result:
            file_tutorial_id = ObjectId()
            data_insert = {
                "_id": file_tutorial_id,
                "filename": filename,
                "folder": FolderUpload.TUTORIAL,
                "status": FileConstant.StatusFile.ACTIVE,
                "status_request": FileConstant.StatusRequest.UPLOAD,
                "url": result,
                "is_tutorial": 1,
                "format_tutorial": format_tutorial,
                "action_time": datetime.utcnow()
            }
            file_id = await FileModel().add_file(data_insert)
            print("file_id: " + str(file_id))

        return build_message_susccess({
            "data": result
        })

    @staticmethod
    async def lst_file_tutorial(format_tutorial, page, per_page, access_token):
        filter_option = {
            "is_tutorial": 1
        }
        if format_tutorial:
            filter_option = {
                "format_tutorial": format_tutorial
            }

        count = await FileModel().collection.count_documents(filter_option)
        total_page = math.ceil(count / per_page)
        files = await FileModel().find_paginate(filter_option, page, per_page, sort_option=[("action_time", -1)])
        result = []
        page_data = {
            "total_count": count,
            "total_page": total_page,
            "page": page,
            "per_page": per_page
        }
        async for file in files:
            result.append(jsonable_encoder(file, custom_encoder={ObjectId: str}))
        return build_message_susccess(
            data=result,
            page=page_data
        )
