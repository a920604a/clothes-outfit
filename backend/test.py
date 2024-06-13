from app.scrapy import BEAMSExtract, BEAMSTransform, BEAMSLoader

if __name__ == "__main__":
    posts = BEAMSExtract.BEAMSExtract().extract()
    p = BEAMSTransform.BEAMSTransform().transform(posts)
    BEAMSLoader.BEAMSLoader().load(p)

    # for posts in BEAMSExtract.BEAMSExtract().process_all_urls_generator():
    #     p = BEAMSTransform.BEAMSTransform().transform(posts)
    #     BEAMSLoader.BEAMSLoader.load(p)
