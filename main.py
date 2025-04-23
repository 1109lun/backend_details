from fastapi import FastAPI, Depends, HTTPException, status, Form , Body
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import hashlib
from schemas import UserCreate
from sqlalchemy.exc import IntegrityError
from database import SessionLocal
import models
from auth import create_access_token, get_current_user

app = FastAPI()

# 用於 Dependency Injection 的 DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # 找出該使用者
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="帳號或密碼錯誤")

    # 驗證密碼（SHA256）
    hashed_input_password = hashlib.sha256(password.encode()).hexdigest()
    if user.password != hashed_input_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="帳號或密碼錯誤")

    # 更新 last_login
    user.last_login = datetime.utcnow()
    db.commit()

    # 發 token
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/user/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # 檢查是否已存在
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="使用者已存在")

    # 加密密碼
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()

    # 新增使用者
    new_user = models.User(
        username=user.username,
        password=hashed_password,
        birthday=user.birthday
    )
    db.add(new_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="使用者建立失敗")

    return {"message": "使用者建立成功"}

