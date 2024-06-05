from pydantic import BaseModel
from enum import Enum

class ClothesColor(Enum):
    WHITE = "白"
    GRAY = "灰"
    BLACK = "黑"
    PINK = "粉"
    RED = "紅"
    ORANGE = "橙"
    BEIGE = "米"
    BROWN = "棕"
    YELLOW = "黃"
    GREEN = "綠"
    BLUE = "藍"
    PURPLE = "紫"

class Role(Enum):
    STAFF = "店員"
    CUSTOMER = "顧客"

class Sex(Enum):
    MALE = "男性"
    FEMALE = "女性"

class HeightRange(Enum):
    UNDER_150CM = "150cm以下"
    BETWEEN_150_155CM = "150cm - 155cm"
    BETWEEN_155_160CM = "155cm - 160cm"
    BETWEEN_160_165CM = "160cm - 165cm"
    BETWEEN_165_170CM = "165cm - 170cm"
    BETWEEN_170_175CM = "170cm - 175cm"
    ABOVE_175CM = "175cm以上"

class Topic(Enum):
    OFFICIAL_STYLING = "Official Styling"
    STYLEHINT = "StyleHint"

class ClothesItem(BaseModel):
    post_id: str
    role: Role  # 角色，可能是店員或顧客
    sex: Sex  # 性別，可能是男性或女性
    height: HeightRange  # 身高範圍
    topic: Topic  # 主題標籤
    category: str  # 商品分類
    color : ClothesColor  # 顏色
    url : str  # 商品鏈接
