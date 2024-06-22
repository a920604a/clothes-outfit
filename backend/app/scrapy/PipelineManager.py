from app.notification import logger


class PipelineManager:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor()
        self.transformer = transformer(self.extractor)
        self.loader = loader(self.transformer)

    def run_pipeline(self):
        # Extract
        for posts in self.extractor.extract():
            try:
                logger.info("=" * 50)

                # Transform
                logger.info("{}{}{}".format("-" * 30, "transform", "-" * 30))
                if posts.empty:
                    continue

                transformed_posts = self.transformer.transform(posts)
                # Load

                logger.info("{}{}{}".format("#" * 30, "load", "#" * 30))
                self.loader.load(transformed_posts)

            except Exception as e:
                logger.info(f"Failed to process error: {e}")
                break
            finally:
                logger.info("=" * 50)
