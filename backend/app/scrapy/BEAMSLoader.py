from app.scrapy.LoaderManager import LoaderManager
from app.models.clothes import Clothes
from app.notification import logger

class BEAMSLoader(LoaderManager):

    def __init__(self):
        pass

    def load(self, posts):
        for idx, post in posts.iterrows():
            try:
                model = Clothes(
                    sex=post["sex"],
                    color=post["color"],
                    category=post["category"],
                    image_url=post["image_url"],
                    post_url=post["post_url"],
                )
                model.save()
            except Exception as e:
                logger.info(f"保存時發生錯誤：{e}")
