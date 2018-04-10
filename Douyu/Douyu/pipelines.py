# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from Douyu.settings import IMAGES_STORE as image_store


# ImagesPipeline图片处理管道
class DouyuPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        return item

    def get_media_requests(self, item, info):
        imagelink = item["imageLink"]
        yield scrapy.Request(imagelink)

    def item_completed(self, results, item, info):
        # 取出results里图片信息中的图片的路径
        image_path = [x["path"] for ok, x in results if ok]
        # 重命名
        os.rename(image_store + image_path[0], image_store + item["nickName"] + ".jpg")
        return item
