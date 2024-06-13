from app.scrapy.TransformManager import TransformManager
from app.scrapy.BEAMSExtract import BEAMSExtract



class BEAMSTransform(TransformManager):

    def __init__(self):

        self.category_mapping = BEAMSExtract().category_mapping_reversed
        self.sex_mapping = {
            "M": 1,  # 男性
            "F": 0   # 女性
        }
        
        
    def transform(self, posts):
        print('-'*30, "transform", '-'*30)
        posts['category'] = posts['category'].astype(str).map(self.category_mapping)
        posts['sex'] = posts['sex'].map(self.sex_mapping)
        return posts
