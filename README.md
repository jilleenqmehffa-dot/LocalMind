# LocalMind

LocalMind is an OpenAI-compatible AI Gateway and RAG Knowledge Base project.

## Project Structure

```text
backend/   Backend API service
docs/      Product, system, API, database, and deployment documentation
uploads/   Uploaded documents for local development
```

## Current Stage

模块一：FastAPI 基础 API 已完成。

已实现：

- FastAPI 应用入口
- API 路由结构
- 统一成功与错误响应格式
- HTTP、参数校验和内部异常的全局处理
- Health Check 接口

## 本地运行

```powershell
cd backend
..\.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
```

## 验证方式

```text
GET /        -> 统一成功响应
GET /health  -> 统一成功响应
GET /docs    -> Swagger UI
GET /missing -> 统一 404 错误响应
```
