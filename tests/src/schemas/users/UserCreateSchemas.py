from sqlalchemy import Integer, String
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, Dict
import re

class UserCreate(BaseModel):
    '''
        Class đăng ký tài khoản
        Chứa dữ liệu đăng ký tài khoản
    '''

    email:EmailStr
    # field_name: type = Field(các_ràng_buộc)
    # ...: bắt buộc phải có
    # pattern=r"^[a-zA-Z0-9_]+$" -> regex
    # ^                bắt đầu chuỗi
    # [a-zA-Z0-9_]     cho phép ký tự
    # +                lặp 1 hoặc nhiều lần
    # $                kết thúc chuỗi
    username:str=Field(..., min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")
    full_name:str=Field(..., min_length=2, max_length=255)
    password:str=Field(..., min_length=8, max_length=100)
    # Optional[T] -> T hoặc là None. Bỏ trống -> None
    phone:Optional[str]=None

    # viết logic kiểm tra dữ liệu tùy chỉnh cho một field
    # @validator("tên_field")
    # def validate_field(cls, value):
    #     ...
    @validator('password') 
    def password_strength(cls, v):
        '''Mật khẩu phải có ít nhất một chữ hoa, 1 số'''
        if not re.search(r"[A-Z]", v):
            raise ValueError("Mật khẩu phải có ít nhất 1 chữ hoa")
        if not re.search(r"\d", v):
            raise ValueError("Mật khẩu phải có ít nhất 1 chữ số")
        return v