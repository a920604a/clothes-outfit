import requests
from bs4 import BeautifulSoup
import os
from abc import ABC, abstractmethod
import pandas as pd


class ExtractManager:
    def __init__(self):
        self.data = self.executeRequest(self.url)

    def executeRequest(self, url, retries=5):
    # TODO: if failed , need to retry 
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        }
        for _ in range(retries):
            try:
                r = requests.get(url, headers=header)
                # 檢查請求是否成功
                if r.status_code == 200:
                    soup = BeautifulSoup(r.text, "html.parser")

                    # with open("main.html", "w", encoding="utf-8") as f:
                    #     f.write(soup.prettify())

                    return soup
                else:
                    print(f"請求失敗。狀態碼：{r.status_code}")
                    # print("響應內容：", r.text)
            
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}. Retrying...{url}")
        print(f"Failed to parse {url}")
        return None

    @abstractmethod
    def extract(self):
        pass
