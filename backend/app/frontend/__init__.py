from fastapi import APIRouter, Query
from typing import List, Optional
from typing import Dict
from utils.redis_utils import Redis  # 使用绝对导入
from conf import config  # 使用绝对导入
from frontend.filter import fetch_filtered_data, cache_filtered_data  # 使用绝对导入
from fastapi import APIRouter, Query
from typing import List, Optional
from typing import Dict
from sqlalchemy.orm import Session
from models.clothes import Clothes
from models import engine
from utils.redis_util import Redis