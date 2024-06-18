from models.clothes import Clothes
from scrapy.BEAMSExtract import BEAMSExtract
from scrapy.TransformManager import TransformManager
from scrapy.BEAMSExtractWithHashTag import BEAMSExtractWithHashTag
from scrapy.BEAMSTransform import BEAMSTransform
from scrapy.BEAMSLoader import BEAMSLoader
from notification import logger
import os


# 定義流水線管理器類
class PipelineManager:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor()
        self.transformer = transformer(self.extractor)
        self.loader = loader(self.transformer)
        Clothes.truncate_table()

        # os.makedirs("transform", exist_ok=True)
        # os.makedirs("extract", exist_ok=True)

    def run_pipeline(self):
        for posts in self.extractor.extract():
            try:
                logger.info("=" * 50)
                # logger.info(f"Processing URL: {url}")

                # Extract

                # 假設這裡已經完成 extract，posts 是從 extract 得到的數據

                # Transform

                logger.info("{}{}{}".format("-" * 30, "transform", "-" * 30))
                # 檢查 posts 是否為空的 DataFrame
                if posts.empty:
                    # logger.warning(f"DataFrame is empty for URL: {url}. Skipping transformation and loading.")
                    continue

                # for id, post in posts.iterrows():
                #     post.to_csv(f"extract/{url.replace('/', '_')}-{sex}-{category}-{color}.csv", index=False)

                transformed_posts = self.transformer.transform(posts)

                # for id, post in posts.iterrows():
                #     post.to_csv(f"transform/{url.replace('/', '_')}-{sex}-{category}-{color}.csv", index=False)

                # Load
                logger.info("{}{}{}".format("#" * 30, "load", "#" * 30))
                # logger.info(f"handling {url} {sex} {category} {color}")
                self.loader.load(transformed_posts)

                # logger.info(f"Successfully processed and loaded data for URL: {url}")

            except Exception as e:
                # logger.info(f"Failed to process URL {url} {sex} {category} {color} with error: {e}")
                break
            finally:
                logger.info("=" * 50)

    # def run_popularity_pipeline(self):
    #     for posts in self.extractor.extract():
    #         continue
