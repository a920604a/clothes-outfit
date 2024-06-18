from scrapy.PipelineManager import PipelineManager
from scrapy.BEAMSExtract import BEAMSExtract
from scrapy.BEAMSExtractWithHashTag import BEAMSExtractWithHashTag
from scrapy.BEAMSTransform import BEAMSTransform
from scrapy.BEAMSTransformWithHashTag import BEAMSTransformWithHashTag
from scrapy.BEAMSLoader import BEAMSLoader
from scrapy.BEAMSLoaderWithHashTag import BEAMSLoaderWithHashTag

if __name__ == "__main__":

    pipeline_manager = PipelineManager(BEAMSExtract, BEAMSTransform, BEAMSLoader)
    pipeline_manager.run_pipeline()

    pipeline_manager = PipelineManager(
        BEAMSExtractWithHashTag, BEAMSTransformWithHashTag, BEAMSLoaderWithHashTag
    )
    pipeline_manager.run_pipeline()
