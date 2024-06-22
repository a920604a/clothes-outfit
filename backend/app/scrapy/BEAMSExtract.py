import pandas as pd
from enum import Enum
import concurrent.futures
from app.utils.process import extract_tree_value
from app.scrapy.BEAMSExtractBase import BEAMSExtractBase
from app.notification import logger


class BEAMSExtract(BEAMSExtractBase):

    def __init__(self):
        super().__init__()

        self.ColorEnum = self.generate_color_enum()
        self.sex_dict = self.generate_sex_enum()
        self.categories = self.generate_category()

        for color_enum in self.ColorEnum:
            logger.info(f"{color_enum.name} : {color_enum.value}")
        logger.info(self.sex_dict)
        logger.info(self.categories)
        self.category_mapping_reversed = {v: k for k, v in self.categories.items()}

    def generate_color_enum(self):
        color_select = self.data.find("div", class_="color-select").find(
            "ul", class_="item-index-menu-colors search"
        )
        li_tags = color_select.find_all("li", class_="item-index-menu-colors-list")
        ColorEnum = Enum(
            "ColorEnum",
            [(li.get("data-code", li["class"][1].split("-")[1])) for li in li_tags],
        )
        return ColorEnum

    def generate_sex_enum(self):
        sex_tags = self.data.find("ul", class_="item-index-menu-navi").find_all(
            "li", class_="item-index-menu-navi-list"
        )
        sex_dict = {}
        for tag in sex_tags:
            link = tag.find("a")["href"]
            sex_key = link.split("=")[1]
            sex_value = tag.find("div", class_="option-name").text.strip()
            sex_dict[sex_key] = sex_value
        return sex_dict

    def generate_category(self):
        categories = {}
        category_tags = self.data.find("ul", class_="item-index-menu-navi-in").find_all(
            "li", class_="item-index-menu-navi-in-list"
        )
        for cat in category_tags[:9]:  # limit to 9 categories for example
            tree = cat.find("a")["href"]
            tree_value = extract_tree_value(tree)
            if tree_value:
                tag = cat.find("div", class_="option-name")
                categories[tag.text] = tree_value
        return categories

    def generate_url(self, sex, category, color=None):
        url = f"{self.url}/?sex={sex}"
        if category:
            url += f"&tree={category}"
        if color:
            url += f"&color_group={color.name}"
        return url

    # def get_posts_element(self, soup, sex, category, color=None):
    #     main_content = soup.find("body")
    #     list_items = main_content.find("div", class_="listed-items-4columns")
    #     list_posts = list_items.find_all(
    #         "li", class_="beams-list-image-item has-author"
    #     )
    #     all_posts = pd.DataFrame()
    #     for post in list_posts:
    #         element = post.find("div", class_="beams-list-image-item-img")
    #         post_url = element.find("a")["href"]
    #         image_url = element.find("img")["src"]
    #         post = pd.DataFrame(
    #             {
    #                 "post_url": [post_url],
    #                 "image_url": [image_url],
    #                 "sex": [sex],
    #                 "category": [category],
    #                 "color": [color],
    #             }
    #         )
    #         all_posts = pd.concat([all_posts, post], ignore_index=True)
    #     return all_posts

    def process_page(self, url, page_number, sex, category, color=None):
        all_posts = pd.DataFrame()  # 初始化一個空的 DataFrame 來儲存所有的 posts

        for i in range(1, page_number + 1):
            page_data = self.executeRequest(f"{url}&p={i}")
            logger.info(f"現在處理網頁 {url} 其頁碼是: {i}/{page_number}")
            if page_data is None:  # 此條件沒有滿足的
                continue
            else:
                posts = self.get_posts_element(
                    page_data, sex=sex, category=category, color=color.name
                )
                all_posts = pd.concat([all_posts, posts], ignore_index=True)
        return pd.DataFrame(all_posts)

    def process_url(self, sex, category, color=None):
        url = self.generate_url(sex, category, color)
        logger.info(f"準備爬蟲 {url}")
        data = self.executeRequest(url)
        page_number = self.get_max_page(url, data)
        return self.process_page(url, page_number, sex, category, color)

    def extract(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
            futures = []
            for sex in self.sex_dict.keys():
                for cat_k, cat_v in self.categories.items():
                    for color in self.ColorEnum:
                        futures.append(
                            executor.submit(self.process_url, sex, cat_v, color)
                        )
            for future in concurrent.futures.as_completed(futures):
                logger.info("{}{}{}".format("+" * 30, "extract", "+" * 30))
                yield future.result()
