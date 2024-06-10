import requests
from bs4 import BeautifulSoup
import os
from abc import ABC, abstractmethod


class ExtractManager:
    def __init__(self):
        self.data = self.executeRequest(self.url)

    def download(self, list_items, p):
        # path = os.path.join("source_data", "men")
        path = "source_data"
        if not os.path.exists(path):
            os.makedirs(path)

        for i, item in enumerate(list_items):
            file_path = f"source_data/{item.sex}/{item.color}"
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            with open(
                f"{file_path}/page-{p}-item-{i}.html",
                "w",
                encoding="utf-8",
            ) as f:
                # f.write(item)
                f.write(item.post.prettify())

    def executeRequest(self, url):
    # TODO: if failed , need to retry 
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        }

        r = requests.get(url, headers=header)

        # 檢查請求是否成功
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")

            with open("main.html", "w", encoding="utf-8") as f:
                f.write(soup.prettify())

            return soup
        else:
            print(f"請求失敗。狀態碼：{r.status_code}")
            # print("響應內容：", r.text)
        return None

    @abstractmethod
    def extract(self):
        pass
