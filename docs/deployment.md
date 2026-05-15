# Deployment Guide

本文档描述 LocalMind 的环境变量、启动命令、部署步骤和运行时验证方式。

## 当前范围

模块一支持本地 FastAPI 启动和基础 API 验证。生产部署、数据库服务和反向代理配置尚未纳入当前范围。

## 环境变量

定义在 `backend/.env.example`：

```env
APP_NAME=LocalMind
APP_ENV=development
API_HOST=127.0.0.1
API_PORT=8000
```

## 本地启动

在仓库根目录执行：

```powershell
cd backend
..\.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
```

打开：

```text
http://127.0.0.1:8000/docs
```

## Docker 启动

在仓库根目录执行：

```powershell
docker compose up --build
```

后端服务监听：

```text
http://127.0.0.1:8000
```

## 运行验证

```powershell
curl.exe http://127.0.0.1:8000/
curl.exe http://127.0.0.1:8000/health
curl.exe -i http://127.0.0.1:8000/not-exist
```

预期行为：

- `/` 返回统一成功响应。
- `/health` 返回统一成功响应。
- `/docs` 打开 Swagger UI。
- 未知路由返回统一 404 错误响应。
