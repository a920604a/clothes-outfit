from app.scrapy.BEAMSExtractBase import BEAMSExtractBase
from app.utils.process import replace_spaces
from app.notification import logger
import pandas as pd
from itertools import product
import concurrent.futures

class BEAMSExtractWithHashTag(BEAMSExtractBase):

    def __init__(self):
        super().__init__()
        self.hash_tag_list = self.generate_hash_tag()
        logger.info(self.hash_tag_list)

    def generate_hash_tag(self):
        hash_tag_list = []
        hash_tags = self.data.find("div", class_="tags-content").find_all("li")
        for tag in hash_tags:
            hash_tag = tag.find("a").text
            hash_tag = replace_spaces(hash_tag, "+")
            hash_tag_list.append(hash_tag)
        return hash_tag_list

    def generate_url(self, hash_tag):
        return f"{self.url}/?hashtag={hash_tag}"
    
    def process_page(self, url, page_number, hash_tag):
        all_posts = pd.DataFrame()  # 初始化一個空的 DataFrame 來儲存所有的 posts

        for i in range(1, page_number + 1):
            page_data = self.executeRequest(f"{url}&p={i}")
            logger.info(f"現在處理網頁 {url} 其頁碼是: {i}/{page_number}")
            if page_data is None:
                continue
            posts = self.get_posts_element(page_data, hash_tag=hash_tag)
            all_posts = pd.concat([all_posts, posts], ignore_index=True)
        return pd.DataFrame(all_posts)
    

    def process_url(self, hash_tag):
        url = self.generate_url(hash_tag)
        logger.info(f"準備爬蟲 {url}")
        data = self.executeRequest(url)

        page_number = self.get_max_page(url, data)
        return self.process_page(url, page_number, hash_tag)

    

    def extract(self):
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
            futures = []
            for tag in self.hash_tag_list:
                futures.append(
                    executor.submit(self.process_url, tag)
                )
            for future in concurrent.futures.as_completed(futures):
                logger.info("{}{}{}".format('+'*30,'extract' , '+'*30))
                yield future.result()
