# test_db.py
from sqlalchemy.orm import sessionmaker
from utils.db_api.database import engine
from utils.db_api.models import User

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def test_query():
    user = session.query(User).filter_by(telegram_id='123345455').first()
    if user:
        print(f"User found: {user}")
    else:
        print("User not found")

    session.close()

if __name__ == "__main__":
    test_query()
