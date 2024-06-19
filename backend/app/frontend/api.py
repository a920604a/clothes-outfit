from utils.redis_utils import Redis  # 使用绝对导入
from conf import config  # 使用绝对导入
from frontend.filter import fetch_filtered_data, cache_filtered_data , fetch_total_items # 使用绝对导入
from fastapi import APIRouter, Query
from typing import List, Optional
from utils.redis_utils import Redis
from utils.timer import timer
from utils.clothes import color_dict, sex_dict

# from app.notification import logger

router = APIRouter()

@router.get("/images")
@timer
def get_images(
    color: Optional[List[str]] = Query(None, description="顏色篩選", alias="color"),
    gender: Optional[str] = Query(None, description="性別篩選", regex="^(W|M|)$"),
    page: int = Query(1, description="頁碼"),
    page_size: int = Query(12, description="每頁大小"),
):
    filtered_color = []
    # 設定快取鍵
    if color:
        filtered_color = [color_dict[c] for c in color if c in color_dict.keys()]
    color_key = ",".join(filtered_color) if filtered_color else "all"

    gender_key = sex_dict.get(gender, -1)  # 使用預設值 -1

    cache_key = f"clothes:{color_key}:{gender_key}:page{page}"

    # 檢查是否有快取的資料
    cached_data = Redis.read_dict(cache_key)
    total_items_key = f"clothes:{color_key}:{gender_key}:total_items"
    total_items = Redis.read_dict(total_items_key)
    
    if cached_data:
        print(f"{cache_key} is already in cache")
        image_urls = [item.image_url for item in cached_data]
        post_urls = [item.post_url for item in cached_data]

        return {
            "all_items": total_items,
            "image_url": image_urls,
            "post_url": post_urls,
        }

    # 如果沒有快取，從資料庫中查詢
    data = fetch_filtered_data(filtered_color, gender_key, page, page_size)

    # 提取圖片URL和發布URL
    image_urls = [item.image_url for item in data]
    post_urls = [item.post_url for item in data]

    # 計算並快取總個數（僅當頁碼為1時）
    if page == 1 and total_items is None:
        total_items = fetch_total_items(filtered_color, gender_key)
        Redis.write_dict(total_items_key, total_items)

    # 存入快取
    print(f"Writing data to cache with key {cache_key}")
    Redis.write_dict(cache_key, data)
    Redis.expire(cache_key, config.REDIS["EXPIRE"])

    # 緩存未來幾頁的資料
    cache_filtered_data(filtered_color, gender_key, page, page_size, 5)

    response = {
        "all_items": total_items,
        "image_url": image_urls,
        "post_url": post_urls,
    }

    return response
