from tests.src.database.models.users.UserTable import Base, User, UserRole
from tests.src.database.database import engine

Base.metadata.create_table(engine)