
# from . import url  # 使用絕對導入
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import time, os
from objprint import op
from abc import ABC, abstractmethod

from pydantic import BaseModel
from enum import Enum
from ..utils.clothes import ClothesItem




# from ..utils.clothes import ClothesItem

class ExtractManagement:

    # @abstractmethod
    url = "https://www.uniqlo.com/tw/zh_TW/stylingbook/stylehint"  # 定義類屬性 url
 

    def get_target_element(self, html_content):
        # 使用 BeautifulSoup 解析 HTML 內容
        soup = BeautifulSoup(html_content, 'html.parser')
        main_content = soup.find('body').find(id='root').find('main')
        # print(main_content)
        
        # option 1 
        # section_element = main_content.find('section', class_='fr-ec-layout-wrapper fr-ec-template-ilp__main-content-min-height')
        # div_element = section_element.find_all('div', class_='fr-ec-layout fr-ec-layout--gutter-md fr-ec-layout--gutter-lg fr-ec-layout--span-4-sm fr-ec-layout--span-12-md fr-ec-layout--span-12-lg')[1]
        # div_element = div_element.find('div', class_ = 'fr-ec-tab-group__content')
        # div_element = div_element.find('div', class_ = 'fr-ec-tab-group__content')
        # section_element = div_element.find('section', class_ = 'fr-ec-layout-wrapper fr-ec-filter-layout')
        # div_element = section_element.find('div', class_='fr-ec-layout fr-ec-layout--span-4-sm fr-ec-layout--span-12-md fr-ec-layout--span-12-lg fr-ec-filter-layout-utility-bar--wrapper')
        # div_element = div_element.find_all('div', recursive=False)[1]  # 獲取所有直接子元素
        # with open("div_elements.html", "w", encoding="utf-8") as f:
        #     f.write(div_element.prettify())
        # styling_grid_items = div_element.find_all('div', class_='fr-ec-styling-grid__item')

        # option 2 , directly
        styling_grid_items = main_content.find_all('div', class_='fr-ec-styling-grid__item')
        # print(type(styling_grid_items))
        
        return styling_grid_items
    
    def download(self, styling_grid_items, p):
        path = os.path.join("source_data", "men")

        if not os.path.exists(path):
            os.makedirs(path)

        for i, item in enumerate(styling_grid_items):
            with open(f"{path}/page-{p}-item-{i}.html", 'w',encoding="utf-8") as f:
                # f.write(item)
                f.write(item.prettify())

    


    def extract(self):
        # 設定 Chrome 瀏覽器選項
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 啟用無頭模式
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # 設定瀏覽器視窗大小
        chrome_options.add_argument("--window-size=1200,800")  # 指定寬度和高度

        # 啟動 Chrome 瀏覽器
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # 打開網址
        driver.get(f"{self.url}/men")  # 使用類屬性 url

        # 等待頁面加載完成（視情況調整等待時間）
        time.sleep(2)

        # 獲取頁面高度
        i=0
        page_height = driver.execute_script("return document.body.scrollHeight")

        # 開始模擬滾動操作，直到頁面不再增加為止
        while True:
            i+=1
            print(f"第{i} 頁")
            # 模擬按下鍵盤的 "End" 鍵，滾動到頁面底部
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # 等待頁面加載
            
            # 獲取新的頁面高度
            new_page_height = driver.execute_script("return document.body.scrollHeight")
            
            # 如果新的頁面高度和舊的相同，則表示已經滾動到頁面底部
            if new_page_height == page_height:
                break
            
            # 更新頁面高度
            page_height = new_page_height
            html_content = driver.page_source

            target_element = self.get_target_element(html_content)
            # for item in target_element:
            self.download(target_element, i)
            self.transform(target_element)

            break
            

        # 等待一段時間，以確保所有資料都已加載完畢
        time.sleep(2)

        html_content = driver.page_source
        target_element = self.get_target_element(html_content)
        
        self.download(target_element, 1+i)

        # 關閉瀏覽器
        driver.quit()

        # 使用提取目標元素的函數
        # try:
        #     target_element = self.get_target_element(html_content)
                
        #     for item in target_element:
        #         # 將每個 item 的 HTML 內容添加到列表中
        #         self.item_contents.append(item.prettify())
        # except Exception as e:
        #     print(f"錯誤：{e}")

    # @abstractmethod
    def transform(self, data):
        for i, item in enumerate(data):
            post = item.find('a')
            if post:
                post_id = post['href'].split('/')[-1] #　/tw/zh_TW/stylingbook/stylehint/
                img_url   = post.find('img', class_='fr-ec-image__img')['src']
                item_data = {
                        "url": img_url,
                        "post_id": post_id
                    }
                clothes_item = ClothesItem(**item_data)
                # print(item_data)


            # 根據示例數據創建ClothesItem實例
            # pass

    # @abstractmethod
    # def load(self, data, destination):
    #     pass



# if __name__ == "__main__":
#     ExtractManagement().extract()




















