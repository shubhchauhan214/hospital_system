import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env file")

POOL_SIZE = int(os.getenv("DB_POOL_SIZE", 10))
MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", 20))

engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_size=POOL_SIZE,
                       max_overflow=MAX_OVERFLOW, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_postgres_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return "PostgreSQL Connected Successfully"
    except Exception as e:
        return f"PostgreSQL Connection Failed: {str(e)}"
