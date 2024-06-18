import requests
from bs4 import BeautifulSoup
import os
from abc import ABC, abstractmethod
import pandas as pd
from notification import logger


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
                    logger.info(f"請求失敗。狀態碼：{r.status_code}")
                    # logger.info("響應內容：", r.text)

            except requests.exceptions.RequestException as e:
                logger.info(f"Request failed: {e}. Retrying...{url}")
        logger.info(f"Failed to parse {url}")
        return None

    @abstractmethod
    def extract(self):
        pass
