from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.conf import config

# 假設你已經有一個引擎
db_url = f'mysql+mysqlconnector://{config.MYSQL["USER"]}:{config.MYSQL["PASSWD"]}@{config.MYSQL["HOST"]}:{config.MYSQL["PORT"]}/{config.MYSQL["DB"]}'

engine = create_engine(
    db_url, pool_size=5, pool_timeout=10, echo=False
)  # echo=True for debug

# 創建 Session 類別
Session = sessionmaker(bind=engine)

# # 創建 session 物件
# session = Session()
