from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base
from datetime import datetime
import hashlib

# 資料庫連線字串，請根據你的設定調整
DATABASE_URL = "postgresql://todo-user:todopassword@localhost:5433/test"

# 建立連線
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# SHA256 密碼加密
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# 建立使用者資料
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

# 寫入資料庫
session.add_all(users)
session.commit()
