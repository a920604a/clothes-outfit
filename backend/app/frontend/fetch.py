from typing import List, Optional
from app.utils.redis_utils import Redis
from app.conf import config
from app.frontend.filter import (
    fetch_filtered_data,
    cache_filtered_data,
    fetch_total_clothes_items,
    fetch_popularity_data,
    cache_popularity_data,
    fetch_total_popularity_items,
)
from app.utils.clothes import color_dict, sex_dict


def get_popularity_data(page: int, page_size: int):
    popularity_cache_key = f"popularity:page{page}"
    popularity_cached_data = Redis.read_dict(popularity_cache_key)
    total_items_key = "popularity:total_items"
    total_items = Redis.read_dict(total_items_key)

    if popularity_cached_data:
        print(f"{popularity_cached_data} is already in cache")
        image_urls = [item.image_url for item in popularity_cached_data]
        post_urls = [item.post_url for item in popularity_cached_data]
        return {
            "all_items": total_items,
            "image_url": image_urls,
            "post_url": post_urls,
        }

    data = fetch_popularity_data(page, page_size)
    image_urls = [item.image_url for item in data]
    post_urls = [item.post_url for item in data]

    if page == 1 and total_items is None:
        total_items = fetch_total_popularity_items()
        Redis.write_dict(total_items_key, total_items)

    print(f"Writing data to cache with key {popularity_cache_key}")
    Redis.write_dict(popularity_cache_key, data)
    Redis.expire(popularity_cache_key, config.REDIS["EXPIRE"])

    cache_popularity_data(page, page_size, 5)

    return {
        "all_items": total_items,
        "image_url": image_urls,
        "post_url": post_urls,
    }


def get_filtered_data(
    color: Optional[List[str]], gender: Optional[str], page: int, page_size: int
):
    filtered_color = (
        [color_dict[c] for c in color if c in color_dict.keys()] if color else []
    )
    color_key = ",".join(filtered_color) if filtered_color else "all"
    gender_key = sex_dict.get(gender, -1)

    cache_key = f"clothes:{color_key}:{gender_key}:page{page}"
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

    data = fetch_filtered_data(filtered_color, gender_key, page, page_size)
    image_urls = [item.image_url for item in data]
    post_urls = [item.post_url for item in data]

    if page == 1 and total_items is None:
        total_items = fetch_total_clothes_items(filtered_color, gender_key)
        Redis.write_dict(total_items_key, total_items)

    print(f"Writing data to cache with key {cache_key}")
    Redis.write_dict(cache_key, data)
    Redis.expire(cache_key, config.REDIS["EXPIRE"])

    cache_filtered_data(filtered_color, gender_key, page, page_size, 5)

    return {
        "all_items": total_items,
        "image_url": image_urls,
        "post_url": post_urls,
    }
