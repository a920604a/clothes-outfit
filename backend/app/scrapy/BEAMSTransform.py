from app.scrapy.TransformManager import TransformManager
from app.notification import logger


class BEAMSTransform(TransformManager):

    def __init__(self, extract):
        self.extract = extract

        self.category_mapping = self.extract.category_mapping_reversed
        # self.sex_mapping = {
        #     "M": 1,  # 男性
        #     "W": 0   # 女性
        # }
        self.sex_mapping = {key: 1 if value=='MEN' else 0 for key , value in self.extract.sex_dict.items()}
        
        
    def transform(self, posts):
        try:
            posts['category'] = posts['category'].astype(str).map(self.category_mapping)
            posts['sex'] = posts['sex'].map(self.sex_mapping)
        except Exception as e:
            logger.info(f"post {posts} 錯誤 {e}" )
        return posts
