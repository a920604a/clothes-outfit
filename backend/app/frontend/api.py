from fastapi import APIRouter, Query
from typing import List, Optional
from app.frontend.fetch import get_popularity_data, get_filtered_data

from app.utils.timer import timer


router = APIRouter()


@router.get("/images")
@timer
def get_images(
    color: Optional[List[str]] = Query(None, description="顏色篩選", alias="color"),
    gender: Optional[str] = Query(None, description="性別篩選", regex="^(W|M|)$"),
    page: int = Query(1, description="頁碼"),
    page_size: int = Query(12, description="每頁大小"),
):
    # 如果 color 是單一字符串並包含逗號，則手動分割它
    if color and len(color) == 1 and ',' in color[0]:
        color = color[0].split(',')

    print(color, gender)  # 用於調試
    if color is None and gender is None:
        return get_popularity_data(page, page_size)
    else:
        return get_filtered_data(color, gender, page, page_size)
