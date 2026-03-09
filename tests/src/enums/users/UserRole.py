from enum import Enum

class UserRole(str, Enum):
    '''Phân quyền người dùng'''
    CUSTOMER='customer'
    ADMIN='admin'
    STAFF='staff'