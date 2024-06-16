from app.scrapy.PipelineManager import PipelineManager
from app.scrapy.BEAMSExtract import BEAMSExtract
from app.scrapy.BEAMSExtractWithHashTag import BEAMSExtractWithHashTag
from app.scrapy.BEAMSTransform import BEAMSTransform
from app.scrapy.BEAMSTransformWithHashTag import BEAMSTransformWithHashTag
from app.scrapy.BEAMSLoader import BEAMSLoader
from app.scrapy.BEAMSLoaderWithHashTag import BEAMSLoaderWithHashTag

if __name__ == "__main__":

    pipeline_manager = PipelineManager(BEAMSExtract, BEAMSTransform, BEAMSLoader)
    # pipeline_manager = PipelineManager(BEAMSExtractWithHashTag, BEAMSTransformWithHashTag, BEAMSLoaderWithHashTag)

    pipeline_manager.run_pipeline()