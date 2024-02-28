from sqlalchemy.orm import Session
from new import User
from database_connection import Base, engine

Base.metadata.create_all(bind=engine)

def create_user(db: Session, user_name: str, password: str):
    db_user = User(user_name=user_name, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_name: str):
    return db.query(User).filter(User.user_name == user_name).first()



