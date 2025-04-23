from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base
from datetime import datetime
import hashlib

DATABASE_URL = "postgresql://todo-user:todopassword@localhost:5433/test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

users = [
    User(
        username="aaa",
        password=hash_password("aaa123"),
        birthday=datetime(2000, 1, 1),
    ),
    User(
        username="bbb",
        password=hash_password("bbb123"),
        birthday=datetime(2001, 1, 1),
    ),
    User(
        username="ccc",
        password=hash_password("ccc123"),
        birthday=datetime(2002, 1, 1),
    )
]

session.add_all(users)
session.commit()
