from tests.src.core.settings import settings

# Tạo kết nối engine
from sqlalchemy import create_engine

engine=create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=settings.POOL_SIZE,
    max_overflow=settings.MAX_OVERFLOW,
    pool_pre_ping=settings.POOL_PRE_PING
)