from app.scrapy.ExtractManager import ExtractManager
from enum import Enum
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

    def generate_color_enum(self):
        color_select = self.data.find("div", class_="color-select").find(
            "ul", class_="item-index-menu-colors search"
        )
        li_tags = color_select.find_all("li", class_="item-index-menu-colors-list")
        # data_codes = [li.get("data-code") for li in li_tags]
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

    def get_posts_element(self, soup, sex, color):
        main_content = soup.find("body")
        list_items = main_content.find("div", class_="listed-items-4columns")

        list_posts = list_items.find_all(
            "li", class_="beams-list-image-item has-author"
        )
        # split list_posts
        pd = [PostData(post=p, sex=sex, color=color) for p in list_posts]
        # return list_posts
        return pd

    def get_max_page(self, url, data):
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

    def generate_urls(self):
        urls = []
        for sex in self.sex_dict.keys():
            for color in self.ColorEnum:
                url = f"{self.url}/?sex={sex}&color_group={color.name}"
                urls.append(url)
                print(url)
        return urls

    # TODO: many parameter
    def process_page(self, url, page_number, sex, color):
        all_posts = []
        page_number = min(page_number, 1)  # for testing
        for i in range(1, page_number + 1):
            page_data = self.executeRequest(
                f"https://www.beams.tw/styling/?sex={sex}&p={i}"
            )
            print(f"現在處理網頁 {url} 其頁碼是: {i}/{page_number}")
            posts = self.get_posts_element(page_data, sex, color.name)
            all_posts.extend(posts)
            self.download(posts, i)
            # break  # 根據你的程式碼，這裡應該是跳出循環
        return all_posts

    def process_url(self, sex, color):

        url = f"{self.url}/?sex={sex}&color_group={color.name}"

        data = self.executeRequest(url)
        page_number = self.get_max_page(url, data)

        return self.process_page(url, page_number, sex, color)

    def extract(self):
        # for each sex and color, assume without depulicte image/post
        # urls = self.generate_urls()

        # FOR dev.
        # all_posts = []
        # for sex in self.sex_dict.keys():
        #     for color in self.ColorEnum:
        #         url = f"{self.url}/?sex={sex}&color_group={color.value}"

        #         data = self.executeRequest(url)
        #         page_number = self.get_max_page(url, data)

        #         page_number = min(page_number, 1)  # for testing

        #         all_posts.extend(self.process_page(url, page_number, sex, color))
        # print(f"all posts has {len(all_posts)}")
        # return all_posts

        # multithread, maybe block
        all_posts = []
        # TODO: use generator to feed transform
        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
            futures = []
            for sex in self.sex_dict.keys():
                for color in self.ColorEnum:
                    futures.append(executor.submit(self.process_url, sex, color))
            for future in concurrent.futures.as_completed(futures):
                all_posts.extend(future.result())

        print(f"all posts has {len(all_posts)}")
        return all_posts
