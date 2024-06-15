# from fastapi import FastAPI, Body
# from typing import List, Dict
# from app import app


# @app.post("/api/images")
# def get_images(filters: Dict[str, str]):
#     # 根據篩選條件獲取影像URL
#     all_images = [
#         {
#             "url": "//cdn.beams.co.jp/taiwan/img/styling/118018/118018_s.jpg",
#             "color": "紅色",
#             "style": "日系",
#             "gender": "男性",
#         },
#         {
#             "url": "//cdn.beams.co.jp/taiwan/img/staff/1/153_s.jpg",
#             "color": "藍色",
#             "style": "工業",
#             "gender": "女性",
#         },
#         {
#             "url": "//cdn.beams.co.jp/taiwan/img/styling/117986/117986_s.jpg",
#             "color": "黑色",
#             "style": "極簡",
#             "gender": "不限性別",
#         },
#         # 添加更多影像...
#     ]

#     filtered_images = [
#         image["url"]
#         for image in all_images
#         if (filters.get("color", "") == "" or image["color"] == filters["color"])
#         and (filters.get("style", "") == "" or image["style"] == filters["style"])
#         and (filters.get("gender", "") == "" or image["gender"] == filters["gender"])
#     ]
#     print(f"filtered_images {filtered_images}")

#     return filtered_images
