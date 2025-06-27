# FastAPI Hóa Đơn Backend

## Cài đặt

```bash
cd fastapi_backend
python -m venv venv
source venv/bin/activate  # hoặc venv\Scripts\activate trên Windows
pip install -r requirements.txt
```

## Chạy server

```bash
uvicorn main:app --reload
```

- API docs: http://localhost:8000/docs
- Endpoint chính: http://localhost:8000/api/hoa-don

## Tích hợp với React dashboard
- Đảm bảo sửa API_URL trong frontend nếu backend không chạy cùng domain.
- Đã bật CORS cho mọi origin (dev).

## Cấu trúc bảng (SQLite)
- File DB sẽ tự tạo: `hoa_don.db`
- Nếu muốn import dữ liệu mẫu, có thể dùng SQLite Browser hoặc thêm API import. 