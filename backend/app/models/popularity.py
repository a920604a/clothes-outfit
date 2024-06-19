from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
from app.models.BaseModel import BaseModel


class Popularity(BaseModel):
    __tablename__ = "popularity"

    hash_tag = Column(String(255), nullable=True, comment="標籤")
    image_url = Column(String(255), nullable=True, comment="圖片網址")
    post_url = Column(String(255), nullable=True, comment="發布網址")

    def __repr__(self):
        return f"<Popularity(id={self.id}, hash_tag={self.hash_tag}, image_url={self.image_url}, post_url={self.post_url}, created_at={self.created_at}, updated_at={self.updated_at})>"
