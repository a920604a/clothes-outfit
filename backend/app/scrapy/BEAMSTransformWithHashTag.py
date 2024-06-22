from app.scrapy.TransformManager import TransformManager


class BEAMSTransformWithHashTag(TransformManager):

    def __init__(self, extract):
        self.extract = extract

    def transform(self, posts):
        return posts
