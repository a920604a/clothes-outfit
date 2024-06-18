from sqlalchemy.orm import Session

from conf import config  # 使用绝对导入
from fastapi import Query
from models.clothes import Clothes
from models import engine
from utils.redis_utils import Redis


def fetch_filtered_data(color=None, gender=None, page_number=1, page_size=12):
    offset = (page_number - 1) * page_size
    with Session(engine) as session:
        query = session.query(Clothes)

        if color:
            query = query.filter(Clothes.color == color)
        if gender:
            query = query.filter(Clothes.sex == gender)

        result = query.offset(offset).limit(page_size).all()
    return result


def cache_filtered_data(color, gender, current_page, page_size, num_pages):
    for i in range(1, num_pages + 1):
        next_page = current_page + i
        cache_key = f"clothes:{color}:{gender}:page{next_page}"
        if not Redis.read_dict(cache_key):
            data = fetch_filtered_data(color, gender, next_page, page_size)
            Redis.write_dict(cache_key, data)
            Redis.expire(cache_key, config.REDIS["EXPIRE"])
            print(f"Cached data for page {next_page}")
        else:
            print(f"Page {next_page} data already cached")
