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
@router.get('/{id}')
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
> > ```
> > POST /tasks
> > GET /tasks/1
> > ```

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

