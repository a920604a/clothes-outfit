from app.scrapy.ExtractManager import ExtractManager
from enum import Enum
import pandas as pd
from itertools import product

from app.utils.process import replace_spaces, extract_tree_value
import threading
import concurrent.futures

from objprint import op
from collections import namedtuple

PostData = namedtuple("PostData", ["post", "sex", "color"])


class BEAMSExtract(ExtractManager):
    url = "https://www.beams.tw/styling"
    

    def __init__(self):
        # main page just for collect all filter(sex, color)
        self.data = self.executeRequest(self.url)

        # super().__init__()

        self.ColorEnum = self.generate_color_enum()
        self.sex_dict = self.generate_sex_enum()
        self.categories = self.generate_category()
        self.category_mapping_reversed = {v: k for k, v in self.categories.items()}

        self.hash_tag_list = self.generate_hash_tag()

    def generate_color_enum(self):
        color_select = self.data.find("div", class_="color-select").find(
            "ul", class_="item-index-menu-colors search"
        )
        li_tags = color_select.find_all("li", class_="item-index-menu-colors-list")
        ColorEnum = Enum(
            "ColorEnum",
            [(li.get("data-code", li["class"][1].split("-")[1])) for li in li_tags],
        )

        for color_enum in ColorEnum:
            print(color_enum.name, ":", color_enum.value)
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
        print(sex_dict)
        return sex_dict

    def generate_hash_tag(self):
        # 23AW, BEAMS, BEAMS PLUS, Ray BEAMS, BEAMS BOY, 別注
        hash_tag_list = []
        hash_tags = self.data.find("div", class_="tags-content").find_all("li")
        for tag in hash_tags:
            hash_tag = tag.find('a').text
            
            hash_tag = replace_spaces(hash_tag, "+")
            
            hash_tag_list.append(hash_tag)
        return hash_tag_list
        
    def generate_category(self):
        # 襯衫
        # T-shirt
        # 上衣
        # 外套
        # 短夾克
        # 大衣
        # 褲子
        # 裙子
        # 洋裝
        categories={}
        category_tags = self.data.find("ul", class_ = "item-index-menu-navi-in").find_all(
            "li",class_="item-index-menu-navi-in-list"
            )
        for cat in category_tags[:9]: # cheat
            tree = cat.find('a')['href']
            tree_value = extract_tree_value(tree)
            if tree_value:
                
                tag = cat.find("div", class_="option-name")
                
                categories[tag.text] = tree_value
        print(categories)
        return categories
            
    def get_posts_element(self, soup, sex, category, color):
        main_content = soup.find("body")
        list_items = main_content.find("div", class_="listed-items-4columns")

        list_posts = list_items.find_all(
            "li", class_="beams-list-image-item has-author"
        )
        all_posts = pd.DataFrame()
        for post in list_posts:
            element = post.find("div", class_="beams-list-image-item-img")
            # if element:

            post_url = element.find("a")["href"]
            image_url = element.find("img")["src"]
            post = pd.DataFrame(
            {
                        "post_url": [post_url],
                        "image_url": [image_url],
                        "sex": [sex],
                        "category": [category],
                        "color": [color]
                    })
            all_posts = pd.concat([all_posts, post ], ignore_index=True)
        return all_posts

    def get_max_page(self, url, data):
        if data is None: return 1
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
                    # print(f"{url} 最後一個頁碼是: {last_page_number}")
                    return last_page_number
                except ValueError:
                    print("最後一個頁碼無法轉換為整數")
                    return 1

            else:
                return 1
        else:
            return 1

    # def extract_page(self, page_number):
    # def extract_page(self, sex, color, page_number):

    #     page_data = self.executeRequest(
    #         f"https://www.beams.tw/styling/?sex=M&p={page_number}"
    #     )
    #     print(
    #         f"現在處理網頁 https://www.beams.tw/styling/?sex={sex.value}&p={page_number} 其頁碼是: {page_number}"
    #     )
    #     posts = self.get_posts_element(page_data)
    #     return PostData(posts=posts, sex=sex, color=color)

    # self.download(posts, page_number)

    # self.transform(posts, page_number)

    def generate_url(self, sex, category, color):
        url = f"{self.url}/?sex={sex}"
        if category:
            url += f"&tree={category}"
            if color:
                url += f"&color_group={color.name}"
        return url

    # TODO: many parameter
    def process_page(self, url, page_number, sex, category, color):
        all_posts = pd.DataFrame()  # 初始化一個空的 DataFrame 來儲存所有的 posts

        # page_number = min(page_number, 1)  # for testing
        for i in range(1, page_number + 1):
            page_data = self.executeRequest(
                f"{url}&p={i}"
            )
            print(f"現在處理網頁 {url} 其頁碼是: {i}/{page_number}")
            if page_data is None: # 此條件沒有滿足的
                continue
            else:
                posts = self.get_posts_element(page_data, sex, category , color.name)
                all_posts = pd.concat([all_posts, posts], ignore_index=True)
                # self.download(posts, i)
        return pd.DataFrame(all_posts)

    def process_url(self, sex, category, color):
        url = self.generate_url(sex, category, color)
        print(f"準備爬蟲 {url}")
        data = self.executeRequest(url)
        page_number = self.get_max_page(url, data)
        return self.process_page(url, page_number, sex, category, color)

    def extract(self):
     
    

        # 定義一個處理單一組合的函數
        all_posts = pd.DataFrame()
        def process_combination(args):
            sex, cat_v, color = args
            return self.process_url(sex, cat_v, color)

        # 使用product來生成所有的組合
        combinations = product(self.sex_dict.keys(), self.categories.values(), self.ColorEnum)

        # 使用map函數來處理每一個組合
        processed_posts = map(process_combination, combinations)

        # 展開嵌套的列表並加入到all_posts中
        for posts in processed_posts:
            all_posts = pd.concat([all_posts,posts])
        return all_posts

        # multithread, maybe block
        # all_posts = pd.DataFrame()
        # TODO: use generator to feed transform
        # with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        #     futures = []
        #     for sex in self.sex_dict.keys():
        #         for cat_k, cat_v in self.categories.items():
        #             for color in self.ColorEnum:
        #                 futures.append(executor.submit(self.process_url, sex, cat_v, color))
        #     for future in concurrent.futures.as_completed(futures):
        #         all_posts = pd.concat([all_posts, future.result()])

        # print(f"all posts has {len(all_posts)}")
        # return all_posts
    
    # 使用生成器版本的 process_all_urls
    def process_all_urls_generator(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
            futures = []
            for sex in self.sex_dict.keys():
                for cat_k, cat_v in self.categories.items():
                    for color in self.ColorEnum:
                        futures.append(executor.submit(self.process_url, sex, cat_v, color))
            for future in concurrent.futures.as_completed(futures):
                yield future.result()

    
