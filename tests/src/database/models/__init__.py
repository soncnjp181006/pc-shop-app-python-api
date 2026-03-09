from tests.src.database.models.users.UserTable import Base, User, UserRole
from tests.src.database.database import engine

__all__ = [
    "User", "UserRole"
]

# Tạo toàn bộ các bảng
Base.metadata.create_table(engine)