from sqlalchemy import Column, Integer, String, Boolean, create_engine, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, unique=True, nullable=False)
    city = Column(String, nullable=True)
    notify = Column(Boolean, default=False)


    def __repr__(self):
        return f"<User(telegram_id={self.telegram_id}, city='{self.city}', notify={self.notify})>"
