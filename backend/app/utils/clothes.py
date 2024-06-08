from pydantic import BaseModel
from enum import Enum


class ClothesColor(Enum):
    WHITE = "白色系"
    BLACK = "黑色系"
    GRAY = "灰色系"
    BROWN = "棕色系"
    BEIGE = "米色系"
    GREEN = "綠色系"
    BLUE = "藍色系"
    PURPLE = "紫色系"
    YELLOW = "黃色系"
    PINK = "粉色系"
    RED = "紅色系"
    ORANGE = "橘色系"
    SILVER = "銀色系"
    GOLD = "金色系"
    BRONZE = "其他"


class Role(Enum):
    STAFF = "店員"
    CUSTOMER = "顧客"


class Sex(Enum):
    MALE = "M"
    FEMALE = "W"


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
    # post_id: str
    # role: Role  # 角色，可能是店員或顧客
    sex: Sex  # 性別，可能是男性或女性
    # height: HeightRange  # 身高範圍
    # topic: Topic  # 主題標籤
    # category: str  # 商品分類
    color: ClothesColor  # 顏色
    post_url: str  # 商品鏈接
    image_url: str
