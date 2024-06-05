
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
import json
import urllib.parse




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
            
                
    def transform(self, data, p):
        path = os.path.join("source_data", "men")
        for i, item in enumerate(data):
            post = item.find('a')
            if post:
                post_id = post['href'].split('/')[-1] #　/tw/zh_TW/stylingbook/stylehint/
                img_url   = post.find('img', class_='fr-ec-image__img')['src']
                if img_url:
                    item_data = {
                            "url": img_url,
                            "post_id": post_id
                        }
                    clothes_item = ClothesItem(**item_data)
                else:
                    print(f"post_id {post_id}")
            else:
                print(f"Faield to {path}/page-{p}-item-{i}.html")

                # print(item_data)


            # 根據示例數據創建ClothesItem實例
            # pass

    

    def executeSelenium(self):
        # 設定 Chrome 瀏覽器選項
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 啟用無頭模式
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])


        # 設定瀏覽器視窗大小
        chrome_options.add_argument("--window-size=1200,800")  # 指定寬度和高度

        # 啟動 Chrome 瀏覽器
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # 打開網址
        driver.get(f"{self.url}/men")  # 使用類屬性 url

        # 等待頁面加載完成（視情況調整等待時間）
        # time.sleep(2)
        driver.implicitly_wait(2)
        i=0
        page_height = driver.execute_script("return document.body.scrollHeight")

        # 開始模擬滾動操作，直到頁面不再增加為止
        while True:
            i+=1
            print(f"第{i} 頁")
            # 模擬按下鍵盤的 "End" 鍵，滾動到頁面底部
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # 等待頁面加載
            # driver.implicitly_wait(2)
            
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
            self.transform(target_element, i)

            # break
            

        driver.implicitly_wait(2)

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
                
   
    def executeRequest(self):
        url = "https://www.uniqlo.com/tw/api/ugc-proxy/v1/contents/search?style_gender%5B0%5D=1&order=published_at%3Adesc&result_limit=50&page=1&priority_flag=true&brand=uq"
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
        print(url)

        r = requests.get(url, headers=header)
        
        # 檢查請求是否成功
        if r.status_code == 200:
            try:
                data = json.loads(r.text)
                # print(data)
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                print("數據已成功保存到 data.json")
            except json.JSONDecodeError:
                print("JSON 解碼錯誤。響應內容不是有效的 JSON。")
                print("響應內容：", r.text)
        else:
            print(f"請求失敗。狀態碼：{r.status_code}")
            print("響應內容：", r.text)


    def executeRequest(self):
        base_url = "https://www.uniqlo.com/tw/api/ugc-proxy/v1/contents/search"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        }

        all_data =[]

        # 爬取前 5 頁的數據作為示例
        for page in range(1, 6):
              # 設定查詢參數的基本部分
            params = {
                "style_gender[0]": 1,
                "order": "published_at:desc",
                "result_limit": 50,
                "page":page,
                "priority_flag": "true",
                "brand": "uq"
            }

            # 使用 urlencode 編碼查詢參數
            encoded_params = urllib.parse.urlencode(params)

        
            url = f"{base_url}?{encoded_params}"
            print(url)
            r = requests.get(url, headers=headers)

            if r.status_code == 200:
                try:
                    data = json.loads(r.text)  # 直接解析 JSON 響應
                    all_data.append(data)  # 假設數據在 'results' 鍵下
                    print(len(all_data))
                except json.JSONDecodeError:
                    print(f"第 {page} 頁的 JSON 解碼錯誤。")
                    print("響應內容：", r.text)
            else:
                print(f"第 {page} 頁的請求失敗。狀態碼：{r.status_code}")
            #     print("響應內容：", response.text)

        # 將所有頁面的數據保存到 JSON 文件
        with open('all_data.json', 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=4)

        print("所有數據已成功保存到 all_data.json")


    def extract(self):
        
        

        # self.executeRequest()
        self.executeSelenium()

        # 獲取頁面高度
    
    # @abstractmethod
    
    # @abstractmethod
    # def load(self, data, destination):
    #     pass



# if __name__ == "__main__":
#     ExtractManagement().extract()




















