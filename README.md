# 🗺️ Mini-GGmap

Ứng dụng tìm đường tối ưu trên bản đồ với nhiều thuật toán khác nhau - dự án nhóm.

## 📋 Tổng quan dự án

Mini-GGmap là một ứng dụng web tìm đường giống Google Maps đơn giản, được thiết kế để:
- Hiển thị bản đồ tương tác
- Tìm đường giữa 2 điểm với nhiều thuật toán khác nhau
- Hỗ trợ nhiều loại phương tiện (ô tô, xe máy, đi bộ)
- Quản lý dữ liệu bản đồ thông qua admin panel

## 🏗️ Cấu trúc project

```
mini_GGmap/
├── app.py                 # Entry point
├── requirements.txt       # Dependencies  
├── app/
│   ├── config.py         # Configuration
│   ├── extensions.py     # Flask extensions
│   ├── routes/           # Web routes
│   │   ├── main.py       # Main pages
│   │   ├── api.py        # API endpoints
│   │   └── admin.py      # Admin interface
│   ├── algorithms/       # Pathfinding algorithms
│   ├── models/           # Data models
│   └── utils/            # Utilities
├── static/               # CSS, JS, data files
├── templates/            # HTML templates
├── tests/                # Unit tests
└── docs/                 # Documentation
```

## 🚀 Quick Start

1. **Cài đặt môi trường:**
```bash
cd mini_GGmap
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

2. **Chạy ứng dụng:**
```bash
python app.py
```

3. **Truy cập:**
- Ứng dụng: http://127.0.0.1:5000
- Admin: http://127.0.0.1:5000/admin

## 👥 Phân chia công việc cho team

### 🎯 PHASE 1: Core Foundation (Tuần 1-2)

#### **Team Lead / Architecture (1 người)**
- [ ] **P1.1** Setup project structure và git workflow
- [ ] **P1.2** Review và finalize requirements
- [ ] **P1.3** Code review và integration testing
- [ ] **P1.4** Viết documentation và deployment guide

#### **Backend Developer 1 (1 người)**
- [ ] **P1.5** Implement graph data structure và loading
  - Parse GeoJSON files
  - Build NetworkX graph từ road data
  - Optimize graph for pathfinding
- [ ] **P1.6** Implement core pathfinding algorithms
  - Dijkstra algorithm
  - A* algorithm  
  - Node indexing và nearest neighbor search

#### **Backend Developer 2 (1 người)**
- [ ] **P1.7** Implement additional algorithms
  - BFS (Breadth-First Search)
  - DFS (Depth-First Search)
  - Greedy Best-First Search
- [ ] **P1.8** API endpoints cho pathfinding
  - `/api/pathfinding` POST endpoint
  - Input validation và error handling
  - Response formatting

#### **Frontend Developer 1 (1 người)**
- [ ] **P1.9** Map interface với Leaflet.js
  - Interactive map display
  - Click handlers cho start/end points
  - Marker management
- [ ] **P1.10** Control panel UI
  - Vehicle selection
  - Algorithm selection
  - Results display

#### **Frontend Developer 2 (1 người)**
- [ ] **P1.11** Path visualization
  - Draw path on map
  - Animation effects
  - Path info display (distance, time)
- [ ] **P1.12** Mobile responsive design
  - Bootstrap integration
  - Touch-friendly interface
  - Responsive layout

#### **QA/Tester (1 người)**
- [ ] **P1.13** Write unit tests
  - Algorithm testing
  - API endpoint testing
  - Frontend component testing
- [ ] **P1.14** Integration testing
  - End-to-end workflow testing
  - Cross-browser testing
  - Performance testing

### 🚀 PHASE 2: Enhanced Features (Tuần 3-4)

#### **Backend Team**
- [ ] **P2.1** Multiple vehicle support
  - Vehicle-specific road filtering
  - Speed calculations per vehicle type
  - Vehicle restriction handling

- [ ] **P2.2** Advanced features
  - Real-time traffic simulation
  - Road condition modeling
  - Alternative route suggestions

- [ ] **P2.3** Data management
  - GeoJSON file upload
  - Data validation
  - Graph rebuilding

#### **Frontend Team**
- [ ] **P2.4** Enhanced UI features
  - Search functionality (geocoding)
  - Route history
  - Settings panel

- [ ] **P2.5** Admin interface
  - Data management dashboard
  - System monitoring
  - User analytics

- [ ] **P2.6** Performance optimization
  - Map tile caching
  - Lazy loading
  - Bundle optimization

#### **QA/DevOps Team**
- [ ] **P2.7** Production setup
  - Docker containerization
  - CI/CD pipeline
  - Monitoring setup

## 🔧 Technical Stack

- **Backend:** Flask, NetworkX, NumPy, GeoPy
- **Frontend:** HTML5, Bootstrap 5, Leaflet.js, Vanilla JS
- **Data:** GeoJSON, JSON
- **Testing:** pytest, unittest
- **Deployment:** Gunicorn, Docker (optional)

## 📝 Coding Standards

### **Git Workflow:**
1. Feature branches từ `main`
2. Pull requests với code review
3. Merge sau khi pass tests

### **Naming Conventions:**
- **Files:** `snake_case.py`
- **Classes:** `PascalCase`
- **Functions/Variables:** `snake_case`
- **Constants:** `UPPER_CASE`

### **Code Quality:**
- Write docstrings cho functions
- Comment các logic phức tạp
- Follow PEP 8 style guide
- Include unit tests cho new features

## 📊 Timeline & Milestones

### **Week 1:** Foundation
- [x] Project setup
- [ ] Core algorithms implementation
- [ ] Basic UI

### **Week 2:** Integration
- [ ] API integration
- [ ] Frontend-backend connection
- [ ] Testing

### **Week 3:** Enhancement
- [ ] Advanced features
- [ ] UI/UX improvements
- [ ] Performance optimization

### **Week 4:** Polish & Deploy
- [ ] Bug fixes
- [ ] Documentation
- [ ] Deployment setup

## 🧪 Testing Strategy

### **Unit Tests:**
- Algorithm correctness
- API endpoint functionality
- Data validation

### **Integration Tests:**
- Frontend-backend integration
- End-to-end pathfinding workflow
- Data loading and processing

### **Performance Tests:**
- Large graph handling
- Response time benchmarks
- Memory usage optimization

## 📖 Documentation

### **For Developers:**
- API documentation
- Algorithm explanations
- Setup guides

### **For Users:**
- User manual
- FAQ
- Troubleshooting guide

## 🚀 Deployment

### **Development:**
```bash
python app.py
# Access at http://127.0.0.1:5000
```

### **Production:**
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## 🤝 Contributing

1. Clone repo và create feature branch
2. Implement feature theo assigned task
3. Write tests và documentation
4. Submit pull request
5. Code review và merge

## 📞 Contact & Support

- **Team Lead:** [Your Name]
- **Repository:** [GitHub URL]
- **Documentation:** [Wiki URL]

---

## 🎯 Task Assignment Template

Khi assign tasks, sử dụng format:

```markdown
### [Member Name] - [Role]
**Sprint:** Week X
**Tasks:**
- [ ] **TaskID** Task description
  - Subtask 1
  - Subtask 2
  - Expected completion: [Date]
  - Dependencies: [Other tasks]

**Priority:** High/Medium/Low
**Estimated hours:** X hours
```

Good luck team! 🚀