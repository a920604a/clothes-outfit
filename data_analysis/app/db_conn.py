import pandas as pd
from conf import MYSQL
from sqlalchemy import create_engine
import logging
import os

# 日誌檔案名稱
log_filename = "example.log"

# 如果日誌檔案存在，則清空檔案
if os.path.exists(log_filename):
    with open(log_filename, "w", encoding="utf-8") as f:
        f.truncate(0)

# 設定 logging
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# 獲取 logger
logger = logging.getLogger(__name__)


# 假設你已經有一個引擎
db_url = f'mysql+mysqlconnector://{MYSQL["USER"]}:{MYSQL["PASSWD"]}@{MYSQL["HOST"]}:{MYSQL["PORT"]}/{MYSQL["DB"]}'

engine = create_engine(
    db_url, pool_size=5, pool_timeout=10, echo=False
)  # echo=True for debug


colors_list = [
    {"code": "brown", "name": "棕色系"},
    {"code": "orange", "name": "橘色系"},
    {"code": "gray", "name": "灰色系"},
    {"code": "white", "name": "白色系"},
    {"code": "beige", "name": "米色系"},
    {"code": "pink", "name": "粉色系"},
    {"code": "red", "name": "紅色系"},
    {"code": "purple", "name": "紫色系"},
    {"code": "green", "name": "綠色系"},
    {"code": "blue", "name": "藍色系"},
    {"code": "gold", "name": "金色系"},
    {"code": "silver", "name": "銀色系"},
    {"code": "yellow", "name": "黃色系"},
    {"code": "black", "name": "黑色系"},
]

# 轉換成字典
color_dict = {color["code"]: color["name"] for color in colors_list}

sex_dict = {"M": 1, "W": 0}


# 查詢數據
def query_clothes(color, sex):

    # conn = create_connection()
    print(color, sex)
    color = color_dict[color]
    gender = "M"
    if sex == "女":
        gender = "W"
    logger.info(color, gender)
    query = "SELECT * FROM clothes WHERE color=%s AND sex=%s"
    df = pd.read_sql(query, engine, params=(color, gender))

    return df
