from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from data.config import DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Configure the sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for ORM models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from utils.db_api.models import User
    Base.metadata.create_all(bind=engine)
