from app.scrapy import BEAMSExtract, BEAMSTransform

if __name__ == "__main__":

    posts = BEAMSExtract.BEAMSExtract().extract()
    BEAMSTransform.BEAMSTransform(posts).transform()
