from app.scrapy.PipelineManager import PipelineManager

if __name__ == "__main__":
    # posts = BEAMSExtract.BEAMSExtract().extract()
    # p = BEAMSTransform.BEAMSTransform().transform(posts)
    # BEAMSLoader.BEAMSLoader().load(p)

    pipeline_manager = PipelineManager()
    pipeline_manager.run_pipeline()