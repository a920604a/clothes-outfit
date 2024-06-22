import requests
from bs4 import BeautifulSoup
from abc import abstractmethod
from app.notification import logger


class ExtractManager:
    def __init__(self):
        self.data = self.executeRequest(self.url)

    def executeRequest(self, url, retries=5):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        }
        for _ in range(retries):
            try:
                r = requests.get(url, headers=header)
                # 檢查請求是否成功
                if r.status_code == 200:
                    soup = BeautifulSoup(r.text, "html.parser")
                    return soup
                else:
                    logger.info(f"請求失敗。狀態碼：{r.status_code}")

            except requests.exceptions.RequestException as e:
                logger.info(f"Request failed: {e}. Retrying...{url}")
        logger.info(f"Failed to parse {url}")
        return None

    @abstractmethod
    def extract(self):
        pass
