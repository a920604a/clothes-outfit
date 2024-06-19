from app.scrapy.ExtractManager import ExtractManager
from app.utils.process import replace_spaces, extract_tree_value
from app.notification import logger
import pandas as pd


class BEAMSExtractBase(ExtractManager):
    url = "https://www.beams.tw/styling"

    def __init__(self):
        self.data = self.executeRequest(self.url)

    def get_max_page(self, url, data):
        if data is None:
            return 1
        page_number_ul = data.find("ul", class_="page-number")
        if page_number_ul:
            li_elements = page_number_ul.find_all("li")

            if li_elements:
                # 獲取最後一個 <li> 元素
                last_li = li_elements[-1]

                # 抓取最後一個 <li> 元素中的 <a> 元素的文本內容
                last_page_value = last_li.find("a").text
                try:
                    # 將文本內容轉換為整數
                    last_page_number = int(last_page_value)
                    # logger.info(f"{url} 最後一個頁碼是: {last_page_number}")
                    return last_page_number
                except ValueError:
                    logger.info("最後一個頁碼無法轉換為整數")
                    return 1

            else:
                return 1
        else:
            return 1

    def get_posts_element(self, soup, **kwargs):
        main_content = soup.find("body")
        list_items = main_content.find("div", class_="listed-items-4columns")
        list_posts = list_items.find_all(
            "li", class_="beams-list-image-item has-author"
        )

        all_posts = pd.DataFrame()
        for post in list_posts:
            element = post.find("div", class_="beams-list-image-item-img")
            post_url = element.find("a")["href"]
            image_url = element.find("img")["src"]

            # 將所有的關鍵字參數加入到post_data中
            post_data = {"post_url": [post_url], "image_url": [image_url]}
            post_data.update(kwargs)  # 添加其他的關鍵字參數

            post = pd.DataFrame(post_data)
            all_posts = pd.concat([all_posts, post], ignore_index=True)

        return all_posts
