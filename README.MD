# Mục Lục
- [Mục Lục](#mục-lục)
- [Phần 1. Cài đặt môi trường Python để phát triển Backend](#phần-1-cài-đặt-môi-trường-python-để-phát-triển-backend)
  - [1.1. Cài đặt môi trường `venv`](#11-cài-đặt-môi-trường-venv)
  - [1.2. Kích hoạt môi trường `venv`](#12-kích-hoạt-môi-trường-venv)
- [Phần 2. Cấu trúc thư mục cơ bản](#phần-2-cấu-trúc-thư-mục-cơ-bản)
- [Phần 3. Cài đặt thư viện - cấu hình file `requirements.txt`](#phần-3-cài-đặt-thư-viện---cấu-hình-file-requirementstxt)
- [Phần 4. Cấu hình file `.gitignore`](#phần-4-cấu-hình-file-gitignore)
- [Phần 5. Viết 1 backend cơ bản và phân tích cấu trúc](#phần-5-viết-1-backend-cơ-bản-và-phân-tích-cấu-trúc)
  - [5.1. Cấu trúc cơ bản của một backend](#51-cấu-trúc-cơ-bản-của-một-backend)
  - [5.2. Viết API cơ bản](#52-viết-api-cơ-bản)
  - [5.3. Viết API của một app Todo-List cơ bản](#53-viết-api-của-một-app-todo-list-cơ-bản)
  - [5.4. Thiết kế chuẩn REST API](#54-thiết-kế-chuẩn-rest-api)
  - [5.5. Phân tích 5.4. Thiết kế chuẩn REST API ](#55-phân-tích-54-thiết-kế-chuẩn-rest-api-)
    - [5.5.1. Schemas](#551-schemas)
    - [5.5.2. API](#552-api)
    - [5.5.3. Repository](#553-repository)
    - [5.5.4. Services](#554-services)
    - [5.5.5. Viết tách ra cho chuẩn cấu trúc](#555-viết-tách-ra-cho-chuẩn-cấu-trúc)
- [Phần 6. Cấu trúc dự án](#phần-6-cấu-trúc-dự-án)
  - [6.1. Thư mục `src/core/`](#61-thư-mục-srccore)
  - [6.2. Thư mục `src/database/`](#62-thư-mục-srcdatabase)
    - [6.2.1. Kết nối database](#621-kết-nối-database)
    - [6.2.2. Thư mục `src/database/models/`](#622-thư-mục-srcdatabasemodels)
    - [6.2.3. Thư mục `src/database/repositories/`](#623-thư-mục-srcdatabaserepositories)
    - [6.2.4. Thư mục `src/database/migrations/`](#624-thư-mục-srcdatabasemigrations)
  - [6.3. Thư mục `src/schemas/`](#63-thư-mục-srcschemas)
  - [6.4. Thư mục `src/services/`](#64-thư-mục-srcservices)
  - [6.5. Thư mục `src/api/`](#65-thư-mục-srcapi)
  - [6.6. Thư mục `src/api/dependencies/` hoặc `src/dependencies/`](#66-thư-mục-srcapidependencies-hoặc-srcdependencies)
- [Phần 7. Học SQLALCHEMY](#phần-7-học-sqlalchemy)
  - [7.1. SQL cơ bản](#71-sql-cơ-bản)
    - [7.1.1. Tạo database](#711-tạo-database)
    - [7.1.2. Tạo bảng](#712-tạo-bảng)
    - [7.1.3. SELECT](#713-select)
    - [7.1.4. JOIN](#714-join)
    - [7.1.5. INDEX](#715-index)
    - [7.1.6. TRANSACTION](#716-transaction)
    - [7.1.7. SELECT P2](#717-select-p2)
      - [7.1.7.1. Chọn tất cả các cột](#7171-chọn-tất-cả-các-cột)
      - [7.1.7.2. Chọn cột cụ thể và đặt bí danh (Alias)](#7172-chọn-cột-cụ-thể-và-đặt-bí-danh-alias)
      - [7.1.7.3. Loại bỏ dữ liệu trùng lặp (DISTINCT)](#7173-loại-bỏ-dữ-liệu-trùng-lặp-distinct)
    - [7.1.8. WHERE (LỌC DỮ LIỆU)](#718-where-lọc-dữ-liệu)
      - [7.1.8.1. Các toán tử logic (AND, OR, NOT)](#7181-các-toán-tử-logic-and-or-not)
      - [7.1.8.2. Các toán tử đặc biệt (IN, BETWEEN, LIKE)](#7182-các-toán-tử-đặc-biệt-in-between-like)
      - [7.1.8.3. Xử lý giá trị NULL](#7183-xử-lý-giá-trị-null)
    - [7.1.9. SẮP XẾP VÀ GIỚI HẠN DỮ LIỆU](#719-sắp-xếp-và-giới-hạn-dữ-liệu)
      - [7.1.9.1. ORDER BY (Sắp xếp)](#7191-order-by-sắp-xếp)
      - [7.1.9.2. LIMIT (Giới hạn số dòng)](#7192-limit-giới-hạn-số-dòng)
    - [7.1.10. NHÓM DỮ LIỆU VÀ HÀM TỔNG HỢP](#7110-nhóm-dữ-liệu-và-hàm-tổng-hợp)
      - [7.1.10.1. Các hàm tổng hợp (Aggregate Functions)](#71101-các-hàm-tổng-hợp-aggregate-functions)
      - [7.1.10.2. GROUP BY (Nhóm theo cột)](#71102-group-by-nhóm-theo-cột)
      - [7.1.10.3. HAVING (Lọc sau khi nhóm)](#71103-having-lọc-sau-khi-nhóm)

> Môi trường phát triển Window

# Phần 1. Cài đặt môi trường Python để phát triển Backend

## 1.1. Cài đặt môi trường `venv`

***`terminal`:***

```shell
python -m venv .venv 
```

hoặc:

```shell
py -m venv .venv
```

hoặc, ta có thể cài phiên bản python cụ thể để phát triển:

```shell
python -3.14 -m venv .venv # Phiên bản 3.14. Lưu ý, máy phải có phiên bản 3.14 mới cài được 
```

## 1.2. Kích hoạt môi trường `venv`

***`terminal`:***

```shell
.venv\Scripts\activate
```

# Phần 2. Cấu trúc thư mục cơ bản

```shell
pc-shop-app-python-api/
├── .venv/
├── src/
├── README.MD
├── requirements.txt
├── .gitignore
├── .env
├── tests/
```

**Giải thích:**

+ `.venv/` - Folder môi trường Python phát triển backend
+ `src/` - Folder mã nguồn backend
+ `requirements.txt` - File lưu các thư viện cài đặt dùng trong backend
+ `.gitignore` - File lưu tên các File, Folder không muốn push lên github
+ `.env` - File lưu cấu hình nhạy cảm (mật khẩu, tài khoản ...) sử dụng trong backend
+ `tests/` - Mô phỏng, test, thử tính năng mới của backend

# Phần 3. Cài đặt thư viện - cấu hình file `requirements.txt`

***`requirements.txt`:***

```txt
# WEB FRAMEWORK
fastapi  # Framework API hiện đại, hiệu năng cao, hỗ trợ async/await, tự động sinh docs (Swagger/ReDoc)
uvicorn[standard]    # ASGI server để chạy FastAPI, [standard] bao gồm websockets & http tools

# DATABASE
sqlalchemy           # ORM mạnh mẽ nhất Python - ánh xạ class Python ↔ bảng SQL, hỗ trợ nhiều DB
pymysql              # Driver kết nối MySQL/MariaDB thuần Python
cryptography         # Phụ thuộc của pymysql để hỗ trợ xác thực SSL/caching_sha2_password
alembic              # Migration tool cho SQLAlchemy - quản lý version schema database
asyncpg              # Driver PostgreSQL async hiệu năng cao (nếu chuyển sang PostgreSQL)
aiomysql             # Driver MySQL async, thay pymysql khi dùng SQLAlchemy async engine
redis                # Client Redis - dùng cho cache, session, rate limiting, pub/sub
motor                # Driver MongoDB async (nếu cần NoSQL cho một số collection)


# AUTHENTICATION & SECURITY
python-jose[cryptography]  # Tạo và xác thực JWT token (JSON Web Token) cho auth
passlib[bcrypt]    # Hash password an toàn, [bcrypt] dùng thuật toán bcrypt
python-multipart   # (đã có bên dưới, cần thiết cho OAuth2 form login của FastAPI)
authlib            # OAuth2/OpenID Connect client - đăng nhập qua Google, Facebook, GitHub...
pyotp              # Tạo mã OTP (TOTP/HOTP) cho xác thực 2 yếu tố (2FA)
itsdangerous       # Tạo token có chữ ký an toàn - dùng cho email verification, reset password

# VALIDATION & SETTINGS
pydantic[email]     # Validation dữ liệu request/response, [email] thêm validator cho email
pydantic-settings   # Quản lý config từ file .env hoặc biến môi trường với type checking
python-dotenv       # Đọc file .env vào os.environ khi khởi động ứng dụng

# EMAIL
fastapi-mail        # Gửi email HTML/text trong FastAPI, hỗ trợ template Jinja2, async
jinja2              # Template engine - render HTML email động với biến (thường đi kèm fastapi-mail)
emails              # Thư viện gửi email linh hoạt hơn, hỗ trợ SMTP/SendGrid/Mailgun

# FILE UPLOAD & IMAGE PROCESSING
python-multipart # Parse multipart/form-data - bắt buộc để upload file trong FastAPI
Pillow           # Xử lý ảnh: resize, crop, convert định dạng, tạo thumbnail

# Mở rộng - File & Storage
boto3            # AWS SDK - upload/download file lên S3 hoặc S3-compatible storage (MinIO)
cloudinary       # SDK Cloudinary - lưu trữ và transform ảnh/video trên cloud
aiofiles         # Đọc/ghi file bất đồng bộ (async), tránh block event loop khi xử lý file lớn
python-magic     # Detect MIME type thực của file (tránh giả mạo extension khi upload)

# UTILITIES
httpx            # HTTP client hỗ trợ async - gọi API bên ngoài, thay thế requests trong async app
python-slugify   # Tạo slug URL-friendly từ tiếng Việt/Unicode (vd: "Xin Chào" → "xin-chao")
celery           # Task queue - xử lý tác vụ nặng bất đồng bộ (gửi email, xử lý ảnh, report...)
flower           # Web UI giám sát Celery worker và task queue
apscheduler      # Lên lịch chạy task định kỳ (cron job) ngay trong ứng dụng Python
babel            # Đa ngôn ngữ (i18n/l10n) - format ngày giờ, tiền tệ theo locale
pytz             # Xử lý timezone, chuyển đổi múi giờ (zoneinfo là built-in từ Python 3.9+)
orjson           # Serialize/deserialize JSON cực nhanh, hỗ trợ datetime/UUID tự động

# CACHING & RATE LIMITING
fastapi-cache2   # Cache response API tự động với decorator, backend Redis/Memcached
slowapi          # Rate limiting cho FastAPI (giới hạn số request/phút theo IP hoặc user)

# MONITORING & LOGGING
loguru           # Logging đẹp và mạnh hơn module logging chuẩn, hỗ trợ rotation/compression
sentry-sdk       # Theo dõi lỗi và performance realtime trên Sentry platform
prometheus-fastapi-instrumentator  # Expose metrics Prometheus để monitor với Grafana

# WEBSOCKET & REALTIME
websockets       # Thư viện WebSocket thuần Python cho realtime features (chat, notification)

# TESTING & DATA SEEDING
pytest           # Framework test phổ biến nhất Python
pytest-asyncio   # Plugin cho pytest hỗ trợ test các hàm async/await
Faker            # Tạo dữ liệu giả (tên, email, địa chỉ...) để seed database hoặc test

factory-boy      # Tạo fixture/factory object test gắn với SQLAlchemy model, dùng cùng Faker
coverage         # Đo code coverage - xem bao nhiêu % code được test bao phủ
```

***Thực hiện cài đặt file:***

***`terminal`:***

```shell
python -m pip install -r requirements.txt
```

hoặc:

```shell
py -m pip install -r requirements.txt
```

hoặc:

```shell
pip install -r requirements.txt
```

# Phần 4. Cấu hình file `.gitignore`

***`.gitignore`:***

```gitignore
# Environment
.env
.venv
venv/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Build / Distribution
build/
dist/
*.egg-info/

# Logs
*.log

# IDE / Editor
.vscode/
.idea/
```

# Phần 5. Viết 1 backend cơ bản và phân tích cấu trúc

## 5.1. Cấu trúc cơ bản của một backend

```py
from fastapi import FastAPI   # Tạo app
from fastapi import APIRouter # Tạo router

# Tạo app
app=FastAPI() 

# Tạo router
router_1 = APIRouter()
router_2 = APIRouter()

# Khu vực viết API cho các router
# ... Code

app.include_router(router_1)
app.include_router(router_2)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

## 5.2. Viết API cơ bản

```python
from fastapi import FastAPI

app = FastAPI()

app.get('/get')                    # http://127.0.0.1:8000/get
def hello_world() -> dict:
    return {'hello': 'world'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

```python
from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()
router = APIRouter()

@router.get('/')                # http://127.0.0.1:8000/get
def hello_world() -> dict:
    return {'hello': 'world'}

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

Khi chạy trên trình duyệt, nếu dùng đường link: `http://127.0.0.1:8000/get` thì hai đoạn mã trên có đầu ra như nhau

Nhưng đoạn mã thứ hai, ta chỉ cần thay thành: `http://127.0.0.1:8000/docs` thì sẽ có đầu ra trực quan, dễ thao tác và dễ hiểu hơn

## 5.3. Viết API của một app Todo-List cơ bản

```python
from fastapi import FastAPI, APIRouter, HTTPException
from typing import Dict

app = FastAPI()
router = APIRouter()

# Một mhiệm vụ có cấu trúc: {id: name}
task_list = [] # Danh sách nhiệm vụ 

# Xem nhiệm vụ -> get (lấy thông tin từ server)
@router.get("/{id}")
def get_task(id: int) -> Dict[str, object]:

    res = next((task for task in task_list if task["id"] == id), None)

    if res is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy nhiệm vụ")

    return res

# Thêm nhiệm vụ -> post (gửi thông tin mới -> yêu cầu server thêm và lưu lại)
@router.post("/")
def add_task(name: str) -> Dict[str, object]:

    if not name.strip():
        # raise tương tự return -> nhung dùng để bắt lỗi
        # HTTPException -> lỗi API
        # status_code -> trạng thái lỗi
        # detail -> đầu ra
        # return detail, status_code
        raise HTTPException(status_code=400, detail="Tên nhiệm vụ không hợp lệ")

    new_task = {
        "id": len(task_list),
        "name": name
    }

    task_list.append(new_task)

    return new_task


app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

## 5.4. Thiết kế chuẩn REST API 

```python
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
router = APIRouter()

task_list = []

# Định nghĩa model
class TaskCreate(BaseModel): # Dùng để xem task
    name: str

class Task(BaseModel):       # Dùng để import task
    id: int
    name: str

@router.post('/', response_model=Task, status_code=201)
def add_task(task: TaskCreate):
    new_task = {
        "id": len(task_list),
        "name": task.name
    }

    task_list.append(new_task)
    return new_task

@router.get('/{id}')
def get_task(id: int):
    res = next((task for task in task_list if task["id"] == id), None)

    if res is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy nhiệm vụ")

    return res

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```


**Giải thích:**

```python
@router.post('/', response_model=Task, status_code=201)
def add_task(task: TaskCreate):
    new_task = {
        "id": len(task_list),
        "name": task.name
    }

    task_list.append(new_task)
    return new_task
```

**Ta có:**

- `response_model=Task`: bộ lọc thông báo đầu vào lấy từ client được lọc thành kiểu tương tự của class `Task`.  (Tức là loại bỏ các hàng dư thừa, chỉ giữ lại key `name`)
- `status_code` ở đây cho vào cũng được, không cho vào cũng được.
- `task: TaskCreate`: biến nhiệm vụ task có kiểu tương tự của class `TaskCreate`, nếu bị thiếu một key, thì key đó tự có value mặc định (0, ... hay gì không cần biết).

> Ở đây, đầu vào từ client được lọc bởi `Task` còn mỗi key `name`, không có key `id` sau đó ép thành biến `task`. Biến `task` buộc tuân theo `TaskCreate` nên `task{'name' = value_name}` sẽ được chuyển thành `task{'id': id_value, 'name': name_value}`

## 5.5. Phân tích [5.4. Thiết kế chuẩn REST API ](#54-thiết-kế-chuẩn-rest-api) 
```python
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
router = APIRouter()

task_list = []

# schemas/                   <- schemas định nghĩa cấu trúc dữ liệu
# Định nghĩa model
class TaskCreate(BaseModel): # Dùng để xem task
    name: str

class Task(BaseModel):       # Dùng để import task
    id: int
    name: str

# api/                       <- router
@router.post('/', response_model=Task, status_code=201)
def add_task(task: TaskCreate):
    # toàn bộ phần dưới là nghiệp vụ serviecs/ trừ dòng return
    new_task = {
        "id": len(task_list),
        "name": task.name
    }

    task_list.append(new_task)
    return new_task

# api/                       <- router
@router.get("/{id}", response_model=Task)
def get_task(id: int):
    # toàn bộ phần dưới là nghiệp vụ serviecs/ trừ dòng return
    res = next((task for task in task_list if task["id"] == id), None)

    if res is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy nhiệm vụ")

    return res

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

### 5.5.1. Schemas 
```python
from pydantic import BaseModel

class TaskCreate(BaseModel): # Dùng để xem task
    name: str

class Task(BaseModel):       # Dùng để import task
    id: int
    name: str
```

### 5.5.2. API 
```python
@router.post('/', response_model=Task, status_code=201)
def add_task(task: TaskCreate):
	# services
    return new_task

@router.get('/{id}')
def get_task(id: int):
	# services
    return res
```

### 5.5.3. Repository 
```python
task_list.append(new_task)
```

```python
res = next((task for task in task_list if task["id"] == id), None)
```
### 5.5.4. Services 
```python
new_task = {
	"id": len(task_list),
	"name": task.name
}
```

```python
if res is None:
	raise HTTPException(status_code=404, detail="Không tìm thấy nhiệm vụ")
```

### 5.5.5. Viết tách ra cho chuẩn cấu trúc
```python
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel

app = FastAPI()

# prefix
router = APIRouter(prefix="/tasks")

task_list = []

'''schemas - Định nghĩa model'''
class TaskCreate(BaseModel):
    name: str

class Task(BaseModel):
    id: int
    name: str


'''repository - Các hàm truy vấn, thao tác trên dữ liệu'''
def create_task_repository(task: dict):
    task_list.append(task)
    return task

def get_task_repository(id: int):
    return next((t for t in task_list if t["id"] == id), None)


'''services - Nghiệp vụ'''
def add_task_services(task: TaskCreate):

    new_task = {
        "id": len(task_list),
        "name": task.name
    }

    return create_task_repository(new_task)


def get_task_services(id: int):

    res = get_task_repository(id)

    if res is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy nhiệm vụ")

    return res


'''API - Router'''
@router.post("/", response_model=Task, status_code=201)
def add_task(task: TaskCreate):
    return add_task_services(task)

@router.get("/{id}", response_model=Task)
def get_task(id: int):
    return get_task_services(id)


app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

> **Ví dụ: Khi build API:**
>    ```
>    POST /tasks
>    GET /tasks/1
>    ```

Hoặc ta có thể cấu hình prefix thủ công như sau:

```python
router = APIRouter() # bỏ prefix="/tasks"

@router.post("/tasks/", response_model=Task, status_code=201)
def add_task(task: TaskCreate):
    return add_task_services(task)

@router.get("/tasks/{id}", response_model=Task)
def get_task(id: int):
    return get_task_services(id)
```

**Luồng xử lý khi Client gọi `/tasks/1`:**

```
Client
   ↓
GET /tasks/1
   ↓
Router
   ↓
get_task(id=1)
   ↓
Service
   ↓
get_task_services(1)
   ↓
Repository
   ↓
get_task_repository(1)
   ↓
task_list
```


# Phần 6. Cấu trúc dự án
```
src/
├── core/
├── database/
│   ├── models/
│   ├── repositories/
│   └── migrations/
├── schemas/
├── services/
└── api/
    ├── routers/
    └── dependencies/
```

hoặc:

```
src/
├── core/
├── database/
│   ├── models/
│   ├── repositories/
│   └── migrations/
├── schemas/
├── services/
├── api/
│   └── routers/
└── dependencies/   
```

Tùy người thiết kế.

## 6.1. Thư mục `src/core/`

> [!NOTE]
> Lưu cấu hình trung tâm
> + `settings.py`: Cấu hình hệ thống (Quản lý: Biến môi trường, Database URL, Secret Key, CORS, Debug mode)
> + `security.py`: Bảo mật (Hash password, JWT Token, OAuth2, Authentication logic)
> + `logging.py`: Ghi log hệ thống (ghi log request, ghi log lỗi, theo dõi hệ thống)
> + `constants.py`: Hằng số hệ thống (chứa các giá trị không thể thay đổi)

```
src/
└── core/
    ├── settings.py # Cấu hình, dữ liệu nhạy cảm lấy từ file .env
    ├── security.py
    ├── logging.py
    └── constants.py
```

## 6.2. Thư mục `src/database/`

### 6.2.1. Kết nối database

> [!NOTE]
> Kết nối database:
> + `database.py`: Tạo engine (kết nối database, cấu hình engine)
> + `session.py`: Quản lý session (tránh rò rỉ khi kết nối)
> + `base.py`: Base ORM (tạo class Base để các model kế thừa). Class Base này dùng để tạo các bảng


> [!IMPORTANT]
> Phân biệt
> 
> ```python
> from sqlalchemy.orm import declarative_base
> Base = declarative_base() # Class Base ORM dùng để tạo bảng
> ```
> 
> ```python
> from pydantic import BaseModel # Class BaseModel dùng để lọc dữ liệu
> ```

### 6.2.2. Thư mục `src/database/models/`

> [!NOTE]
> Lưu giữ các file tạo bảng database
> + Mapping bảng db thành class Python

### 6.2.3. Thư mục `src/database/repositories/`

> [!NOTE]
> Lưu giữ các file hàm truy vấn database

### 6.2.4. Thư mục `src/database/migrations/`

> [!NOTE]
> Alembic Migration (được Alembic tạo ra) (quản lí thay đổi schema DB, version control cho database)

## 6.3. Thư mục `src/schemas/`

> [!NOTE]
> Dùng để:
> + Lọc, lấy ép form dữ liệu đầu vào
> + Ép form dữ liệu đầu ra
> + Định nghĩa contract API

> [!IMPORTANT]
> Xem phần `Important` ở [6.2.1. Kết nối database](#621-kết-nối-database)


> [!CAUTION]
> Phân biệt: 
> + File `base.py` ở `database/` dùng để tạo class `Base`, dùng để tạo bảng.
> + Các file ở `schemas/` dùng class `BaseModel` dùng để lọc, ép form dữ liệu.

## 6.4. Thư mục `src/services/`

> [!NOTE]
> Lưu trữ các file, hàm nghiệp vụ:
> + Không validate (hiểu nôm na là ép form) cấu trúc request (việc đó do schemas)
> + Không truy vấn DB (việc đó do `repository/`)
> + Không xử lý HTTP (việc đó do `api/` cụ thể là `router`)

**Service có thể làm gì:**
Ví dụ: tạo task.

- Không chỉ đơn giản là thêm vào DB.
- Nghiệp vụ có thể gồm:
  - Kiểm tra trùng tên

  - Chuẩn hóa dữ liệu

  - Ghi log

  - Gửi event

  - Xử lý transaction

Như vậy `repository/` chỉ lập hàm truy vấn database. Còn `services/` thực hiện nghiệp vụ truy vấn database, chỉ việc gọi lại hàm có trong `repository/` và sử dụng, bổ sung thêm để hoàn chỉnh nghiệp vụ.

## 6.5. Thư mục `src/api/`

> [!NOTE]
> `api/` là interface layer của hệ thống. Nó chịu trách nhiệm:
> - Định nghĩa route (GET, POST, PUT, DELETE…)
> - Nhận request
> - Gắn dependency
> - Trả response
> - Gắn response_model
> - Xử lý HTTP exception
> - Nó không chứa nghiệp vụ.


**Cấu trúc cơ bản:**

```
app/
├── api/
│   ├── routers/
│   │   ├── user_router.py
│   │   ├── task_router.py
│   │   └── __init__.py
│   │
│   ├── dependencies/
│   └── api_router.py
```

## 6.6. Thư mục `src/api/dependencies/` hoặc `src/dependencies/`

> [!NOTE]
> Chứa các hàm:
> 
> - Xác thực (auth)
> - Phân quyền (authorization)
> - Inject DB session
> - Inject current user
> - Inject service/repository nếu muốn
> - Reusable dependency logic
> 
> Nó thuộc API layer, vì nó phục vụ HTTP request.


**Ví dụ, cấu trúc:**

```
app/
├── api/
│   ├── routers/
│   └── dependencies/
│       ├── auth.py
│       ├── permissions.py
│       └── db.py
```

hoặc:

```
app/
├── dependencies/
├── api/
```

Tùy theo phong cách tổ chức.

# Phần 7. Học SQLALCHEMY

## 7.1. SQL cơ bản

### 7.1.1. Tạo database

```sql
-- Tạo database pc_shop
CREATE DATABASE pc_shop;

-- Chọn sử dụng thao tác trên pc_shop
USE pc_shop;
```

### 7.1.2. Tạo bảng

```sql
-- Bảng Users: Lưu thông tin người dùng
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Khóa chính, tự tăng
    username VARCHAR(50) NOT NULL UNIQUE, -- Tên đăng nhập, không null, duy nhất
    email VARCHAR(100) NOT NULL, -- Email, không null
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Thời gian tạo mặc định là hiện tại
    status TINYINT DEFAULT 1 -- Trạng thái: 1=Active, 0=Inactive
);

-- Bảng Orders: Lưu thông tin đơn hàng
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL, -- Khóa ngoại liên kết sang bảng Users
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL, -- Số thập phân chính xác cho tiền tệ
    status VARCHAR(20) DEFAULT 'PENDING',

    -- Định nghĩa khóa ngoại (Foreign Key)
    CONSTRAINT fk_user_order  -- Đặt tên cho ràng buộc (thao tác sau sẽ dễ hơn)
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
    ON DELETE CASCADE                       -- Xóa user thì xóa luôn đơn hàng
    ON UPDATE CASCADE                       -- Cập nhật user_id thì cập nhật theo
);
```

> [!NOTE]
> Các bảng có khóa ngoại (`FOREIGN KEY`) liên kết đến bảng có khóa chính (`PRIMARY KEY`): **Bảng có khóa ngoại là con của bảng có khóa chính**.
>
> Trong trường hợp trên, ta có thể vẽ một cây như sau:
>
>           [Users]
>             /
>        [Orders]


### 7.1.3. SELECT

> [!NOTE] 
> Cú pháp chung:
>
>       SELECT cot1, cot2, ...
>       FROM ten_bang
>       WHERE dieu_kien
>       ORDER BY cot_sap_xep
>       LIMIT so_luong;

### 7.1.4. JOIN

```sql
-- INNER JOIN: Chỉ lấy người dùng có đặt hàng
SELECT
u.username,
u.email,
o.order_id,
o.total_amount
FROM Users u
INNER JOIN Orders o ON u.user_id = o.user_id;

-- LEFT JOIN: Lấy tất cả người dùng, kể cả người chưa đặt hàng
SELECT
u.username,
o.order_id,
o.total_amount
FROM Users u
LEFT JOIN Orders o ON u.user_id = o.user_id;

-- Mô phỏng FULL OUTER JOIN trong MySQL
SELECT u.username, o.order_id
FROM Users u
LEFT JOIN Orders o ON u.user_id = o.user_id
UNION
SELECT u.username, o.order_id
FROM Users u
RIGHT JOIN Orders o ON u.user_id = o.user_id;
```

### 7.1.5. INDEX
> [!NOTE]
> INDEX là cấu trúc dữ liệu giúp tăng tốc độ truy vấn (SELECT) nhưng làm giảm tốc độ ghi (INSERT, UPDATE, DELETE) do phải cập nhật chỉ mục.


> [!NOTE] 
> Khi nào dùng INDEX:
>  Khi nào cần tạo INDEX
> 
> + Cột thường xuyên dùng trong mệnh đề WHERE
> + Cột dùng để JOIN
> + Cột dùng trong ORDER BY hoặc GROUP BY
> + Cột có tính chọn lọc cao (High Cardinality), ví dụ: email, username. Không nên index cột giới tính (chỉ có Nam/Nữ)

```sql
-- Tạo index đơn cho cột email
CREATE INDEX idx_users_email ON Users(email);
-- Tạo index kết hợp (Composite Index) cho cột user_id và order_date
CREATE INDEX idx_orders_user_date ON Orders(user_id, order_date);
-- Tạo index duy nhất (Unique Index)
CREATE UNIQUE INDEX idx_users_username ON Users(username);
```

> Sử dụng lệnh EXPLAIN trước câu truy vấn để xem MySQL có sử dụng index hay không
> 
>  ```sql
>  EXPLAIN SELECT * FROM Orders WHERE user_id = 1;
>  ```

### 7.1.6. TRANSACTION
> [!NOTE]
> Transaction là một đơn vị công việc logic được thực hiện như một khối duy nhất. Hoặc tất cả cùng thành công, hoặc tất cả cùng thất bại

> [!NOTE] 
> Tính chất ACID
> + Atomicity (Nguyên tử): Không thể chia nhỏ. Thành công hết hoặc thất bại hết
> + Consistency (Nhất quán): Dữ liệu luôn đúng trạng thái quy định sau giao dịch
> + Isolation (Cô lập): Các giao dịch chạy song song không ảnh hưởng nhau
> + Durability (Bền vững): Khi đã commit, dữ liệu được lưu vĩnh viễn dù có lỗi hệ thống

**Giả sử người dùng A chuyển cho người dùng B 100 USD. Cần trừ tiền A và cộng tiền B. Nếu bước cộng tiền lỗi, bước trừ tiền phải được hoàn tác**

```sql
-- Bắt đầu giao dịch
START TRANSACTION;
-- Bước 1: Trừ tiền người gửi (Giả sử user_id = 1)
UPDATE Accounts
SET balance = balance - 100
WHERE user_id = 1 AND balance >= 100; -- Kiểm tra số dư đủ
-- Kiểm tra số hàng bị ảnh hưởng (trong code ứng dụng)
-- Nếu số hàng = 0 nghĩa là không đủ tiền -> ROLLBACK
-- Bước 2: Cộng tiền người nhận (Giả sử user_id = 2)
UPDATE Accounts
SET balance = balance + 100
WHERE user_id = 2;
-- Nếu mọi thứ thành công
COMMIT;
-- Nếu có lỗi xảy ra ở bất kỳ đâu
ROLLBACK;
```

### 7.1.7. SELECT P2

> [!NOTE] 
> Cú pháp chung:
> ```
> SELECT cot1, cot2, ...
> FROM ten_bang
> WHERE dieu_kien
> ORDER BY cot_sap_xep
> LIMIT so_luong;
> ```

#### 7.1.7.1. Chọn tất cả các cột

```sql
-- Lấy tất cả dữ liệu từ bảng Users
SELECT * FROM Users;
```

#### 7.1.7.2. Chọn cột cụ thể và đặt bí danh (Alias)

```sql
-- Chọn tên và email, đổi tên cột hiển thị
SELECT
username AS ten_dang_nhap,
email AS dia_chi_email
FROM Users;

-- Tính toán trực tiếp trong câu lệnh SELECT
SELECT
user_id,
total_amount,
total_amount * 0.1 AS thue_phai_dong
FROM Orders;
```

#### 7.1.7.3. Loại bỏ dữ liệu trùng lặp (DISTINCT)
Sử dụng khi cần lấy danh sách các giá trị duy nhất từ một cột.

```sql
-- Lấy danh sách các trạng thái đơn hàng duy nhất đã tồn tại
SELECT DISTINCT status FROM Orders;
```


### 7.1.8. WHERE (LỌC DỮ LIỆU)

> [!NOTE]
> Mệnh đề WHERE dùng để lọc các bản ghi thỏa mãn điều kiện cụ thể trước khi trả về kết quả.
> 
> Các toán tử so sánh:
> 
>       = (Bằng), <> hoặc != (Khác), > (Lớn hơn), < (Nhỏ hơn), >= (Lớn hơn hoặc bằng), <= (Nhỏ hơn hoặc bằng)

```sql
-- Lấy người dùng có trạng thái hoạt động (status = 1)
SELECT * FROM Users WHERE status = 1;

-- Lấy đơn hàng có tổng tiền lớn hơn 1000
SELECT * FROM Orders WHERE total_amount > 1000;
```

#### 7.1.8.1. Các toán tử logic (AND, OR, NOT)

```sql
-- Lấy đơn hàng của user_id = 1 VÀ có trạng thái PENDING
SELECT * FROM Orders
WHERE user_id = 1 AND status = 'PENDING';

-- Lấy đơn hàng có trạng thái PENDING HOẶC SHIPPED
SELECT * FROM Orders
WHERE status = 'PENDING' OR status = 'SHIPPED';
```

#### 7.1.8.2. Các toán tử đặc biệt (IN, BETWEEN, LIKE)

> [!NOTE]
> + IN: Kiểm tra giá trị nằm trong một tập hợp.
> + BETWEEN: Kiểm tra giá trị nằm trong một khoảng.
> + LIKE: Tìm kiếm theo mẫu chuỗi (sử dụng ký tự đại diện % và _).

```sql
-- Lấy đơn hàng của các user_id cụ thể
SELECT * FROM Orders
WHERE user_id IN (1, 5, 10);

-- Lấy đơn hàng tạo trong khoảng thời gian từ 2023-01-01 đến 2023-12-31
SELECT * FROM Orders
WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';

-- Tìm người dùng có tên bắt đầu bằng chữ 'A'
SELECT * FROM Users
WHERE username LIKE 'A%';

-- Tìm người dùng có email chứa ký tự '@gmail.com'
SELECT * FROM Users
WHERE email LIKE '%@gmail.com';
```

#### 7.1.8.3. Xử lý giá trị NULL
> [!NOTE]
> Không dùng = NULL, phải dùng IS NULL hoặc IS NOT NULL.

```sql
-- Lấy người dùng chưa có thông tin email (giả sử cột email cho phép NULL)
SELECT * FROM Users WHERE email IS NULL;
```

### 7.1.9. SẮP XẾP VÀ GIỚI HẠN DỮ LIỆU
#### 7.1.9.1. ORDER BY (Sắp xếp)

> [!NOTE]
> Mặc định sắp xếp tăng dần (ASC). Có thể sắp xếp giảm dần (DESC).

```sql
-- Sắp xếp đơn hàng theo ngày tạo mới nhất trước
SELECT * FROM Orders
ORDER BY order_date DESC;

-- Sắp xếp theo nhiều điều kiện: Theo user_id tăng dần, sau đó theo tổng tiền giảm dần
SELECT * FROM Orders
ORDER BY user_id ASC, total_amount DESC;
```

#### 7.1.9.2. LIMIT (Giới hạn số dòng)

> [!CAUTION]
> Thường dùng cho phân trang (pagination) trong ứng dụng Web hoặc Mobile.

```sql
-- Lấy 10 đơn hàng gần nhất
SELECT * FROM Orders
ORDER BY order_date DESC
LIMIT 10;

-- Phân trang: Lấy trang thứ 2, mỗi trang 10 bản ghi (Bỏ qua 10 bản ghi đầu, lấy 10 bản ghi tiếp)
-- Công thức: OFFSET = (so_trang - 1) * so_ban_ghi_tren_trang
SELECT * FROM Orders
LIMIT 10 OFFSET 10;
```

### 7.1.10. NHÓM DỮ LIỆU VÀ HÀM TỔNG HỢP

> [!Caution]
> Dùng cho các báo cáo thống kê (Analytics).


#### 7.1.10.1. Các hàm tổng hợp (Aggregate Functions)

> [!NOTE]
> + `COUNT()`: Đếm số lượng.
> + `SUM()`: Tính tổng.
> + `AVG()`: Tính trung bình.
> + `MAX()`: Tìm giá trị lớn nhất.
> + `MIN()`: Tìm giá trị nhỏ nhất.

```sql
-- Đếm tổng số đơn hàng
SELECT COUNT(*) AS tong_so_don FROM Orders;

-- Tính tổng doanh thu
SELECT SUM(total_amount) AS tong_doanh_thu FROM Orders;

-- Tính trung bình giá trị đơn hàng
SELECT AVG(total_amount) AS gia_tri_trung_binh FROM Orders;
```

#### 7.1.10.2. GROUP BY (Nhóm theo cột)

> [!NOTE]
> Chia dữ liệu thành các nhóm để tính toán trên từng nhóm

```sql
-- Đếm số đơn hàng của từng người dùng
SELECT user_id, COUNT(*) AS so_don_hang
FROM Orders
GROUP BY user_id;

-- Tính tổng doanh thu theo trạng thái đơn hàng
SELECT status, SUM(total_amount) AS doanh_thu_theo_trang_thai
FROM Orders
GROUP BY status;
```

#### 7.1.10.3. HAVING (Lọc sau khi nhóm)

> [!NOTE]
> Khác với WHERE (lọc trước khi nhóm), HAVING lọc kết quả sau khi đã thực hiện GROUP BY

```sql
-- Lấy những người dùng có nhiều hơn 5 đơn hàng
SELECT user_id, COUNT() AS so_don_hang
FROM Orders
GROUP BY user_id
HAVING COUNT() > 5;
```

