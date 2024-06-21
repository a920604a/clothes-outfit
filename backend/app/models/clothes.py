from app.models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String


class Clothes(BaseModel):
    __tablename__ = "clothes"

    sex = Column(Integer, nullable=True, comment="適用性別")
    color = Column(String(30), nullable=True, comment="顏色")
    category = Column(String(30), nullable=True, comment="分類")
    image_url = Column(String(255), nullable=True, comment="圖片網址")
    post_url = Column(String(255), nullable=True, comment="發布網址")

    def __repr__(self):
        return f"<Clothes(id={self.id}, sex={self.sex}, color={self.color}, category={self.category}, image_url={self.image_url}, post_url={self.post_url}, created_at={self.created_at}, updated_at={self.updated_at})>"
