from scrapy.TransformManager import TransformManager
from notification import logger


class BEAMSTransformWithHashTag(TransformManager):

    def __init__(self, extract):
        self.extract = extract

    def transform(self, posts):
        return posts
