from database import engine
from sqlalchemy.orm import sessionmaker

SessionLocal=sessionmaker(
    autocommit=False, # Không tự lưu
    autoflush=False,
    bind=engine
)

# session
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback() # hủy thao tác, trở về trước khi thay đổi (lần commit cuối)
        raise # ném lỗi
    finally:
        db.close() 