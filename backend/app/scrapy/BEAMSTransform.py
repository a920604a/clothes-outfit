from app.scrapy.TransformManager import TransformManager
from enum import Enum
import threading
from app.utils.clothes import ClothesItem
from app.scrapy.BEAMSExtract import PostData


class BEAMSTransform(TransformManager):

    def __init__(self, posts):
        self.number = len(posts)
        self.posts = posts

    def transform(self):
        print(self.number)
        count = 0
        for post_data in self.posts:
            element = post_data.post.find("div", class_="beams-list-image-item-img")
            # if element:

            post_url = element.find("a")["href"]
            image_url = element.find("img")["src"]
            # print(post_data.sex)
            # print(post_data.color.upper())
            ClothesItem(
                sex=post_data.sex,
                color=post_data.color.upper(),
                post_url=post_url,
                image_url=image_url,
            )
