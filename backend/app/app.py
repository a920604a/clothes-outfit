from typing import Union
from typing import List, Dict
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/restaurant/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/api/images")
def get_images(filters: Dict[str, str]):
    print(f"filters {filters}")
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

    filtered_images = [
        image["url"]
        for image in all_images
        if (filters.get("color", "") == "" or image["color"] == filters["color"])
        and (filters.get("style", "") == "" or image["style"] == filters["style"])
        and (filters.get("gender", "") == "" or image["gender"] == filters["gender"])
    ]
    print(f"filtered_images = ={filtered_images}")

    return filtered_images


# option 1
# uvicorn app:app --reload


# option 2
if __name__ == "__main__":
    uvicorn.run(app="app:app", host="127.0.0.1", port=8080, reload=True)
