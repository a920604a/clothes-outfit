from app.scrapy.LoaderManager import LoaderManager
from app.models.popularity import Popularity
from app.notification import logger


class BEAMSLoaderWithHashTag(LoaderManager):

    def __init__(self, transform):
        self.transform = transform

    def load(self, posts):
        for idx, post in posts.iterrows():
            try:
                model = Popularity(
                    hash_tag=post["hash_tag"],
                    image_url=post["image_url"],
                    post_url=post["post_url"],
                )
                model.save()
            except Exception as e:
                logger.info(f"保存時發生錯誤：{e}")
