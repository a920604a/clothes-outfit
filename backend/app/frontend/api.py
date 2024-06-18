from frontend import *

# from app.notification import logger

router = APIRouter()

@router.post("/images")
def get_images(
    color: Optional[str] = Query(None, description="顏色篩選"),
    style: Optional[str] = Query(None, description="風格篩選"),
    gender: Optional[str] = Query(None, description="性別篩選"),
    page: int = Query(1, description="頁碼"),
    page_size: int = Query(12, description="每頁大小")
):
    # 設定快取鍵
    cache_key = f"clothes:{color}:{style}:{gender}:page{page}"
    
    # 檢查是否有快取的資料
    cached_data = Redis.read_dict(cache_key)
    if cached_data:
        return cached_data
    
    # 如果沒有快取，從資料庫中查詢
    data = fetch_filtered_data(color, style, gender, page, page_size)
    
    # 存入快取
    Redis.write_dict(cache_key, data)
    Redis.expire(cache_key, config.REDIS['REDIS_EXPIRE'])
    
    # 緩存未來幾頁的資料
    cache_filtered_data(color, style, gender, page, page_size, 5)
    
    return data