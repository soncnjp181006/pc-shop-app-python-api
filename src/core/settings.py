from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    
    # Database - Import cấu hình từ .env
    DB_HOST:str='localhost'
    DB_PORT:int=3306
    DB_NAME:str
    DB_USER:str
    DB_PASSWORD:str
    POOL_SIZE:int=10          # số kết nối tối thiểu
    MAX_OVERFLOW:int=20       # số kết nối mở thêm khi quá tải -> max 30 kết nối
    POOL_PRE_PING:int=True    # kiểm tra Ping trước khi bắt đầu
    DEBUG:bool=True   

    @property # Bình thường khi gọi: fun() -> trở thành fun
    def DATABASE_URL(self) -> str:
        return(
            f'mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
            f'?charset=utf8mb4' # hỗ trợ emoji và kí tự đặc biệt
        )


    class Config:
        env_file='test/.env' # path
        env_file_encoding='utf-8'
        case_sensitive=True # phân biệt hoa thường

# Cho phép tái sử dụng
@lru_cache
def get_setting() -> Settings:
    return Settings()

# Instance , dùng trực tiếp: from .test.core import settings
settings = Settings()