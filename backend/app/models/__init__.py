from sqlalchemy import create_engine
from conf import config
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base
from models.BaseModel import BaseModel

from sqlalchemy.exc import SQLAlchemyError



# 假設你已經有一個引擎
db_url = f'mysql+mysqlconnector://{config.MYSQL["USER"]}:{config.MYSQL["PASSWD"]}@{config.MYSQL["HOST"]}:{config.MYSQL["PORT"]}/{config.MYSQL["DB"]}'

engine = create_engine(
    db_url, pool_size=5, pool_timeout=10, echo=False
)  # echo=True for debug

# 創建 Session 類別
Session = sessionmaker(bind=engine)

# # 創建 session 物件
# session = Session()