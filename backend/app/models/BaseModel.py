from contextlib import contextmanager
from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from app.models import Session


Base = declarative_base()


@contextmanager
def session_scope():
    """提供一個事務範圍來處理session的上下文管理"""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class BaseModel(Base):
    __abstract__ = True  # abstract class
    id = Column(Integer, primary_key=True, autoincrement=True, comment="pk")
    # created_by = Column(String(64))
    created_at = Column(
        TIMESTAMP(True), comment="創立時間", nullable=False, server_default=func.now()
    )
    # updated_by = Column(String(64))
    updated_at = Column(
        TIMESTAMP(True),
        comment="更新時間",
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
    # remark = Column(String(200), comment="comment")

    def save(self):
        with session_scope() as session:
            session.add(self)

    def update(self):
        with session_scope() as session:
            session.merge(self)

    def delete(self):
        with session_scope() as session:
            session.delete(self)

    @classmethod
    def save_all(cls, objects):
        with session_scope() as session:
            session.add_all(objects)

    @classmethod
    def exists(cls, **kwargs):
        """
        检查是否存在符合条件的实例

        Args:
            model_class: 要检查的模型类
            **kwargs: 检查条件，例如 {'id': 1, 'name': 'John'}

        Returns:
            bool: 是否存在符合条件的实例
        """
        with session_scope() as session:
            query = session.query(cls)
            for key, value in kwargs.items():
                query = query.filter(getattr(cls, key) == value)
            return session.query(query.exists()).scalar()

    @classmethod
    def truncate_table(cls):
        """清空 clothes 表中所有數據"""
        with session_scope() as session:
            try:
                session.query(cls).delete()
            except SQLAlchemyError as e:
                session.rollback()
                raise
