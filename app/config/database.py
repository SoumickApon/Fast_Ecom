from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHAMY_DATABASE_URL = "postgresql://postgres:5588@localhost:5432/esj_dev_student_user_local_37"
SQLALCHAMY_DATABASE_URL = 'sqlite:///./ig_api.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
