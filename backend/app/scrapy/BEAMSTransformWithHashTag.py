from app.scrapy.TransformManager import TransformManager
from app.notification import logger


class BEAMSTransformWithHashTag(TransformManager):

    def __init__(self, extract):
        self.extract = extract

        
    def transform(self, posts):
        return posts
