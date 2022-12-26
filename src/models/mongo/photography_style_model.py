#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 25/03/2022
"""
from bson import ObjectId

from src.common import AccountID, StatusSeenLinkTutorial, CommonCategoryIDDefault, TypeCategoryAddIDDefault
from src.models.mongo import BaseModel


class PhotographyStyleModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.collection = self.db["photography_style"]

    async def insert_data_default(self):
        self.collection.delete_many({"account_id": AccountID.DEFAULT})
        data_inserts = [
            {
                "_id": ObjectId("62897bc011a7288623886641"),
                "account_id": AccountID.DEFAULT,
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.JAPAN_BED_ID,
                "name": "Bed",
                "name_japan": "和ベッドを撮影",
                "direction": "横",
                "shooting_height": "ベッドボード",
                "rule": "ベッドに対し正面から撮影。電気は間接照明含めすべて点ける。",
                "rule_required": True,
                "source": "default",
                "type_create": "default",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d2d680722f936a7728d5.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897bcd11a7288623886642"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_JAPAN_ID,
                "name": "RoomView",
                "name_japan": "入り口から客室全体を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の対角線を取るような構図で 。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253c8b8f23093c702419624.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897bdd11a7288623886643"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_JAPAN_ID,
                "name": "RoomView",
                "name_japan": "入り口から客室全体を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の対角線を取るような構図で 。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253c8b8f23093c702419624.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897be711a7288623886644"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.LITTLE_HOUSE_ID,
                "name": "RoomView",
                "name_japan": "入り口から客室全体を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の対角線を取るような構図で 。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253c8b8f23093c702419624.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897bee11a7288623886645"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.JAPAN_BED_ID,
                "name": "RoomView",
                "name_japan": "入り口から客室全体を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の対角線を取るような構図で 。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253c8b8f23093c702419624.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897bf711a7288623886646"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_ID,
                "name": "RoomView",
                "name_japan": "入り口から客室全体を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の対角線を取るような構図で 。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253c98e9bc5e4c5c58379c4.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c2111a7288623886647"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_JAPAN_ID,
                "name": "RoomWindow",
                "name_japan": "窓際から客室全体を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の対角線を取るような構図で（RoomViewと対角の位置から）。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く。"
                ,
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cdfe1882a2b0c4d00b2c.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c2e11a7288623886648"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_ID,
                "name": "RoomWindow",
                "name_japan": "窓際から客室全体を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の対角線を取るような構図で（RoomViewと対角の位置から）。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cdfe1882a2b0c4d00b2c.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c3611a7288623886649"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_JAPAN_ID,
                "name": "RoomWindow",
                "name_japan": "窓際から客室全体を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の対角線を取るような構図で（RoomViewと対角の位置から）。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cdfe1882a2b0c4d00b2c.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c3e11a728862388664a"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.LITTLE_HOUSE_ID,
                "name": "RoomWindow",
                "name_japan": "窓際から客室全体を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の対角線を取るような構図で（RoomViewと対角の位置から）。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cdfe1882a2b0c4d00b2c.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c4c11a728862388664b"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.JAPAN_BED_ID,
                "name": "RoomWindow",
                "name_japan": "窓際から客室全体を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の対角線を取るような構図で（RoomViewと対角の位置から）。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cdfe1882a2b0c4d00b2c.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c5711a728862388664c"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_JAPAN_ID,
                "name": "LivingSpace",
                "name_japan": "居間を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の中心から、机を真ん中に置き外の景色が見えるような構図で。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く"
                ,
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cf496bd207c37ca2ec48.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c5f11a728862388664d"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.LITTLE_HOUSE_ID,
                "name": "LivingSpace",
                "name_japan": "居間を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の中心から、机を真ん中に置き外の景色が見えるような構図で。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く"
                ,
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cf496bd207c37ca2ec48.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c6911a728862388664e"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.JAPAN_BED_ID,
                "name": "LivingSpace",
                "name_japan": "居間を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の中心から、机を真ん中に置き外の景色が見えるような構図で。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く"
                ,
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cf496bd207c37ca2ec48.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c7111a728862388664f"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_JAPAN_ID,
                "name": "LivingSpace",
                "name_japan": "居間を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "部屋の中心から、机を真ん中に置き外の景色が見えるような構図で。"
                        "部屋の電気は間接照明含めすべて点ける。"
                        "家具などは切れないように。"
                        "ティッシュやゴミ箱などの見栄えが悪いものは取り除く"
                ,
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253ce8be40d3f786a610c7a.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c7811a7288623886650"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_JAPAN_ID,
                "name": "WindowView",
                "name_japan": "客室から見える景色を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "窓の中心ではなく、部屋の中心から撮影する。部屋の電気は間接照明含めすべて点ける。部屋の内側に露出を合わせたものと、外に露出を合わせたものの２枚を撮影する。ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cf8cba7c1d792e8dc2f3.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c8011a7288623886651"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_JAPAN_ID,
                "name": "WindowView",
                "name_japan": "客室から見える景色を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "窓の中心ではなく、部屋の中心から撮影する。部屋の電気は間接照明含めすべて点ける。部屋の内側に露出を合わせたものと、外に露出を合わせたものの２枚を撮影する。ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cf8cba7c1d792e8dc2f3.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c8911a7288623886652"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.LITTLE_HOUSE_ID,
                "name": "WindowView",
                "name_japan": "客室から見える景色を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "窓の中心ではなく、部屋の中心から撮影する。部屋の電気は間接照明含めすべて点ける。部屋の内側に露出を合わせたものと、外に露出を合わせたものの２枚を撮影する。ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cf8cba7c1d792e8dc2f3.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c9311a7288623886653"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.JAPAN_BED_ID,
                "name": "WindowView",
                "name_japan": "客室から見える景色を撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "窓の中心ではなく、部屋の中心から撮影する。部屋の電気は間接照明含めすべて点ける。部屋の内側に露出を合わせたものと、外に露出を合わせたものの２枚を撮影する。ティッシュやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cf8cba7c1d792e8dc2f3.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897c9911a7288623886654"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_JAPAN_ID,
                "name": "Bathroom",
                "name_japan": "風呂を撮影",
                "direction": "縦",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "シャワーヘッドは壁を向ける。シャンプーなどのボトルや椅子・桶を整える 。対象がなるべく切れないように 。鏡に自分が映らないように注意する 。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cff130ef34d83d673b52.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897ca011a7288623886655"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_JAPAN_ID,
                "name": "Bathroom",
                "name_japan": "風呂を撮影",
                "direction": "縦",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "ボトルは満タンにしアメニティは整える。椅子がある場合は切れないように注意する。鏡に自分が映らないように注意する。どちら側から撮影すべきか迷ったら、「情報量が多い方を映す」。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cff130ef34d83d673b52.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897ca911a7288623886656"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.LITTLE_HOUSE_ID,
                "name": "Bathroom",
                "name_japan": "風呂を撮影",
                "direction": "縦",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "ボトルは満タンにしアメニティは整える。椅子がある場合は切れないように注意する。鏡に自分が映らないように注意する。どちら側から撮影すべきか迷ったら、「情報量が多い方を映す」。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cff130ef34d83d673b52.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897caf11a7288623886657"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.JAPAN_BED_ID,
                "name": "Bathroom",
                "name_japan": "風呂を撮影",
                "direction": "縦",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "ボトルは満タンにしアメニティは整える。椅子がある場合は切れないように注意する。鏡に自分が映らないように注意する。どちら側から撮影すべきか迷ったら、「情報量が多い方を映す」。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253cff130ef34d83d673b52.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897cb611a7288623886658"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_JAPAN_ID,
                "name": "Dress Room",
                "name_japan": "洗面所を撮影",
                "direction": "縦",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "ボトルは満タンにしアメニティは整える。椅子がある場合は切れないように注意する。鏡に自分が映らないように注意する。どちら側から撮影すべきか迷ったら、「情報量が多い方を映す」。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d04b28727263a72b9158.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897cbd11a7288623886659"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_JAPAN_ID,
                "name": "Dress Room",
                "name_japan": "洗面所を撮影",
                "direction": "縦",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "ボトルは満タンにしアメニティは整える 椅子がある場合は切れないように注意する 鏡に自分が映らないように注意する どちら側から撮影すべきか迷ったら、「情報量が多い方を映す」",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d04b28727263a72b9158.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897cc511a728862388665a"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.LITTLE_HOUSE_ID,
                "name": "Dress Room",
                "name_japan": "洗面所を撮影",
                "direction": "縦",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "ボトルは満タンにしアメニティは整える 椅子がある場合は切れないように注意する 鏡に自分が映らないように注意する どちら側から撮影すべきか迷ったら、「情報量が多い方を映す」",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d04b28727263a72b9158.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897ccb11a728862388665b"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.JAPAN_BED_ID,
                "name": "Dress Room",
                "name_japan": "洗面所を撮影",
                "direction": "縦",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "ボトルは満タンにしアメニティは整える 椅子がある場合は切れないように注意する 鏡に自分が映らないように注意する どちら側から撮影すべきか迷ったら、「情報量が多い方を映す」",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d04b28727263a72b9158.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897cd211a728862388665c"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_JAPAN_ID,
                "name": "Toilet",
                "name_japan": "トイレを撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "トイレットペーパーなど備品を整える。 露出の調整を慎重に。対象がなるべく切れないように。予備のトイレットペーパーやゴミ箱などの見栄えが悪いものは取り除く 。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d0a3ba3d0fdee3ae98b6.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897cda11a728862388665d"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_JAPAN_ID,
                "name": "Toilet",
                "name_japan": "トイレを撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "トイレットペーパーなど備品を整える。 露出の調整を慎重に。対象がなるべく切れないように。予備のトイレットペーパーやゴミ箱などの見栄えが悪いものは取り除く 。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d0a3ba3d0fdee3ae98b6.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897ce111a728862388665e"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.LITTLE_HOUSE_ID,
                "name": "Toilet",
                "name_japan": "トイレを撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "トイレットペーパーなど備品を整える。 露出の調整を慎重に。対象がなるべく切れないように。予備のトイレットペーパーやゴミ箱などの見栄えが悪いものは取り除く 。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d0a3ba3d0fdee3ae98b6.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897ce911a728862388665f"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id": TypeCategoryAddIDDefault.Room.JAPAN_BED_ID,
                "name": "Toilet",
                "name_japan": "トイレを撮影",
                "direction": "横",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "トイレットペーパーなど備品を整える。 露出の調整を慎重に。対象がなるべく切れないように。予備のトイレットペーパーやゴミ箱などの見栄えが悪いものは取り除く 。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d0a3ba3d0fdee3ae98b6.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897cef11a7288623886660"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id":
                    TypeCategoryAddIDDefault.Room.STYLE_ROOM_JAPAN_ID,
                "name": "Open Air Bath",
                "name_japan": "客室露天風呂を撮影",
                "direction": "横or縦",
                "shooting_height": "浴槽の中が少し見える高さ",
                "rule": "日光強い場合は手で遮光する。",
                "rule_required": True,
                "type_create": "default",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d0fa0cd0901715a71ecd.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897cf611a7288623886661"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id":
                    TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_JAPAN_ID,
                "name": "Open Air Bath",
                "name_japan": "客室露天風呂を撮影",
                "direction": "横or縦",
                "shooting_height": "浴槽の中が少し見える高さ",
                "rule": "日光強い場合は手で遮光する。",
                "rule_required": True,
                "type_create": "default",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d0fa0cd0901715a71ecd.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897d0111a7288623886662"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id":
                    TypeCategoryAddIDDefault.Room.LITTLE_HOUSE_ID,
                "name": "Open Air Bath",
                "name_japan": "客室露天風呂を撮影",
                "direction": "横or縦",
                "shooting_height": "浴槽の中が少し見える高さ",
                "rule": "日光強い場合は手で遮光する。",
                "rule_required": True,
                "type_create": "default",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d0fa0cd0901715a71ecd.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897d0a11a7288623886663"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id":
                    TypeCategoryAddIDDefault.Room.JAPAN_BED_ID,
                "name": "Open Air Bath",
                "name_japan": "客室露天風呂を撮影",
                "direction": "横or縦",
                "shooting_height": "浴槽の中が少し見える高さ",
                "rule": "日光強い場合は手で遮光する。",
                "rule_required": True,
                "type_create": "default",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d0fa0cd0901715a71ecd.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897d1811a7288623886664"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id":
                    TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_ID,
                "name": "Unitbath",
                "name_japan": "ユニットバスを撮影",
                "direction": "横or縦",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "洗面台・バスタブ（シャワー）・トイレがすべて映るようになるべく引いて撮影する。シャワーヘッドは壁側を向ける。予備のトイレットペーパーやゴミ箱などの見栄えが悪いものは取り除く。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d1356298bcec715e108b.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897d2211a7288623886665"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id":
                    TypeCategoryAddIDDefault.Room.LITTLE_HOUSE_ID,
                "name": "Stairs",
                "name_japan": "階段を撮影",
                "direction": "横or縦",
                "shooting_height": "扉の取っ手",
                "rule_required": True,
                "type_create": "default",
                "rule": "階段の段差や２Fとの空間が伝わるようにする",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d1c4549a6483deec79bd.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897d2a11a7288623886666"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id":
                    TypeCategoryAddIDDefault.Room.LITTLE_HOUSE_ID,
                "name": "BedRoom",
                "name_japan": "ベッドルームを撮影",
                "direction": "横",
                "shooting_height": "ベッドボード",
                "rule_required": True,
                "type_create": "default",
                "rule": "ベッドに対し４５°から撮影。電気は間接照明含めすべて点ける。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d162b4075b3a0389cb69.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897d3211a7288623886667"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id":
                    TypeCategoryAddIDDefault.Room.STYLE_ROOM_FOREIGN_JAPAN_ID,
                "name": "BedRoom",
                "name_japan": "ベッドルームを撮影",
                "direction": "横",
                "shooting_height": "ベッドボード",
                "rule_required": True,
                "type_create": "default",
                "rule": "ベッドに対し４５°から撮影。電気は間接照明含めすべて点ける。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d162b4075b3a0389cb69.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897d3a11a7288623886668"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id":
                    TypeCategoryAddIDDefault.Room.CAPSULE_ID,
                "name": "Capsule",
                "name_japan": "カプセル内を撮影",
                "direction": "横",
                "shooting_height": "カプセルの高さの中央",
                "rule_required": True,
                "type_create": "default",
                "rule": "カプセルの中心から奥行きを感じるように撮影。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d21f30d8658c9727519d.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897d4311a7288623886669"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id":
                    TypeCategoryAddIDDefault.Room.CAPSULE_ID,
                "name": "Public Space",
                "name_japan": "カプセルエリア全体を撮影",
                "direction": "横",
                "shooting_height": "床から1メートルくらいの高さ",
                "rule": "カプセルの入り口や居空間が伝わるように撮影。",
                "rule_required": True,
                "type_create": "default",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d272109688d1f41e23f7.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897d4a11a728862388666a"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_GUEST_ROOM_ID,
                "type_category_id":
                    TypeCategoryAddIDDefault.Room.DORMITORY_ID,
                "name": "Dormitory",
                "name_japan": "ドミトリー・大部屋を撮影",
                "direction": "横",
                "shooting_height": "床から1メートルくらいの高さ",
                "rule": "ドミトリーの居空間が伝わるように撮影。",
                "rule_required": True,
                "type_create": "default",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/6253d299ade3e94d12f70abc.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            },
            {
                "_id": ObjectId("62897d5111a728862388666b"),
                "account_id": AccountID.DEFAULT,
                "source": "default",
                "root_category_id": CommonCategoryIDDefault.TAKE_PHOTO_OF_OTHER_ID,
                "type_category_id":
                    CommonCategoryIDDefault.TAKE_PHOTO_OF_OTHER_ID,
                "name": "眺望撮影",
                "name_japan": "",
                "direction": "横",
                "rule_required": True,
                "type_create": "default",
                "shooting_height": "床から1メートルくらいの高さ",
                "rule": "・１枚目は部屋の内側に露出を合わせ、２枚目は外側に露出を合わせる。"
                        "・三脚とタイマー機能を使用し、位置がずれないように注意する。",
                "video_tutorial": {
                    "link": "https://byme-bucket.s3.ap-northeast-1.amazonaws.com/video_tutorial/625d761430ab140c174d7ef2.mp4",
                    "status": StatusSeenLinkTutorial.NOT_SEEN
                }
            }
        ]
        return self.collection.insert_many(data_inserts)

    async def get_photography_style(self, root_category_id, type_category_id):
        filter_option = {
            "root_category_id": ObjectId(root_category_id),
            "type_category_id": {
                "$in": [ObjectId(type_category_id)]
            }
        }
        return self.collection.find(
            filter_option,
            {"account_id": 0, "root_category_id": 0}
        )

    async def get_photography_style_by_root_id(self, root_category_id):
        filter_option = {
            "root_category_id": ObjectId(root_category_id),
            "type_category_id": {
                "$in": [ObjectId(root_category_id)]
            }
        }
        return self.collection.find(
            filter_option,
            {"account_id": 0, "root_category_id": 0}
        )
