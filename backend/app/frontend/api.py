from fastapi import APIRouter, Query
from typing import List, Optional
from typing import Dict
# from app.notification import logger

router = APIRouter()

@router.post("/images")
def get_images(
    color: Optional[str] = Query(None, description="顏色篩選"),
    style: Optional[str] = Query(None, description="風格篩選"),
    gender: Optional[str] = Query(None, description="性別篩選")
):
    # 根據篩選條件獲取影像URL
    all_images = [
        {
            "url": "//cdn.beams.co.jp/taiwan/img/styling/118018/118018_s.jpg",
            "color": "紅色",
            "style": "日系",
            "gender": "男性",
        },
        {
            "url": "//cdn.beams.co.jp/taiwan/img/staff/1/153_s.jpg",
            "color": "藍色",
            "style": "工業",
            "gender": "女性",
        },
        {
            "url": "//cdn.beams.co.jp/taiwan/img/styling/117986/117986_s.jpg",
            "color": "黑色",
            "style": "極簡",
            "gender": "不限性別",
        },
        # 添加更多影像...
    ]
    print(f"color {color}, style {style}, gender {gender}")
    filtered_images = [
        post
        for post in all_images
        if (not color or post["color"] == color)
        and (not style or post["style"] == style)
        and (not gender or post["gender"] == gender)
    ]
    print(filtered_images)
    # logger.info(filtered_images)

    return filtered_images