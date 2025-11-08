# 🗺️ Mini_GGMap

Ứng dụng web tìm đường (mini Google Maps) — dự án nhóm triển khai các thuật toán tìm đường và quản lý dữ liệu bản đồ.

## 📋 Tổng quan dự án

Mini-GGMap là một ứng dụng Flask nhỏ dùng để minh họa và thử nghiệm các thuật toán tìm đường trên dữ liệu bản đồ (GeoJSON). Mục tiêu chính:
- Hiển thị dữ liệu bản đồ (GeoJSON)
- Xây dựng graph đường từ dữ liệu thô và lưu trữ (nếu cần)
- Triển khai và so sánh các thuật toán tìm đường (A*, Dijkstra, v.v.)
- Cung cấp API đơn giản để truy vấn đường đi và dữ liệu liên quan

## 🏗️ Cấu trúc project

```
Mini_GGMap/
├── app.py                 # Entry point (Flask)
├── requirements.txt       # Dependencies
├── app/
│   ├── __init__.py
│   ├── config.py          # Cấu hình
│   ├── extensions.py      # Khởi tạo extensions
│   ├── algorithms/        # Thuật toán (app/algorithms/pathfinder.py)
│   └── routes/            # app/routes/main.py, app/routes/api.py
├── scripts/               # scripts/build_graph.py
├── static/
│   └── data/
│       ├── geojson/       # roads.geojson
│       └── graph/
├── templates/             # Jinja2 templates
├── tests/                 # tests/test_basic.py
└── README.md
```

## 🚀 Hướng dẫn nhanh (Windows - cmd.exe)

1. Mở cmd và chuyển tới thư mục dự án:

```cmd
cd C:\KTMT\Mini_GGMap
```

2. Tạo và kích hoạt virtual environment (cmd.exe):

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

3. Cài đặt phụ thuộc:

```cmd
pip install -r requirements.txt
```

4. Chạy ứng dụng:

```cmd
python app.py
```

5. Mở trình duyệt vào:

	http://127.0.0.1:5000


"# Mini_GGMaps" 
