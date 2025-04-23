from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    username = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    birthday = Column(Date)
    create_time = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
