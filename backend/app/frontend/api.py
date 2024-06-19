from utils.redis_utils import Redis  # 使用绝对导入
from conf import config  # 使用绝对导入
from frontend.filter import fetch_filtered_data, cache_filtered_data  # 使用绝对导入
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
    filtered_color = ""
    # 設定快取鍵
    if color:
        filtered_color = [color_dict[c] for c in color if c in color_dict.keys()]
    color_key = ",".join(name for name in filtered_color) if filtered_color else "all"

    if gender:
        gender = sex_dict.get(gender)
    # transform color
    cache_key = f"clothes:{color_key}:{gender}:page{page}"
    print(cache_key)

    # 檢查是否有快取的資料
    cached_data = Redis.read_dict(cache_key)
    if cached_data:
        print(f"{cache_key} is already in cache")
        total_items = len(cached_data)
        image_urls = [item.image_url for item in cached_data]
        post_urls = [item.post_url for item in cached_data]
        return {
            "all_items": total_items,
            "image_url": image_urls,
            "post_url": post_urls,
        }

    # 如果沒有快取，從資料庫中查詢
    if gender:
        total_items, data = fetch_filtered_data(filtered_color, gender, page, page_size)
    else:
        total_items, data = fetch_filtered_data(filtered_color, page, page_size)

    # 提取圖片URL和發布URL
    image_urls = [item.image_url for item in data]
    post_urls = [item.post_url for item in data]

    # 存入快取
    print(f"Writing data to cache with key {cache_key}")
    Redis.write_dict(cache_key, data)
    Redis.expire(cache_key, config.REDIS["EXPIRE"])

    # 緩存未來幾頁的資料
    cache_filtered_data(filtered_color, gender, page, page_size, 5)

    return {"all_items": total_items, "image_url": image_urls, "post_url": post_urls}


@router.get("/all-items")
@timer
def get_all_items(
    color: Optional[List[str]] = Query(None, description="顏色篩選", alias="color"),
    gender: Optional[str] = Query(None, description="性別篩選", regex="^(W|M|)$"),
):
    print(f" color {color} gender {gender}")
    # 轉換顏色代碼
    filtered_color = ""
    # 設定快取鍵
    if color:
        filtered_color = [color_dict[c] for c in color if c in color_dict.keys()]
    color_key = ",".join(name for name in filtered_color) if filtered_color else "all"

    # 轉換性別代碼
    if gender:
        gender = sex_dict.get(gender)
        total_items, _ = fetch_filtered_data(filtered_color, gender)
    else:
        total_items, _ = fetch_filtered_data(filtered_color)

    # 計算符合條件的所有項目數量

    return {"all_items": total_items}
