# LocalMind 模块化开发路线图

## 1. 文档目的

本文档定义 LocalMind 的模块化开发顺序、每个模块的交付内容和验收标准。目标是在个人开发和 AI 协作场景下，保持项目始终处于可运行、可测试、可迭代的状态。

## 2. 开发原则

- 每个阶段完成后系统必须可运行。
- 优先交付 MVP，避免提前引入复杂架构。
- 每个模块必须具备明确的接口、返回结果和本地验证方式。
- 先完成最小可用 RAG 系统，再扩展 Provider、Streaming、日志和部署能力。
- 第一版不引入微服务、Kubernetes、多 Agent、复杂权限和分布式架构。

## 3. 模块总览

| 模块 | 名称 | 目标 |
| --- | --- | --- |
| 0 | 项目初始化 | 建立基础目录、依赖和 FastAPI 运行环境 |
| 1 | FastAPI 基础 API | 建立路由、统一响应和错误处理 |
| 2 | Chat API | 实现 OpenAI-compatible Chat API |
| 3 | 数据库系统 | 接入 PostgreSQL 和基础表结构 |
| 4 | 文件上传 | 支持文档上传和元数据入库 |
| 5 | RAG 文本处理 | 完成解析、清洗和 chunking |
| 6 | Embedding + pgvector | 生成向量并支持相似度检索 |
| 7 | RAG Query | 基于知识库回答问题并返回来源 |
| 8 | Provider Adapter | 支持多模型厂商适配 |
| 9 | Streaming | 支持流式响应 |
| 10 | 日志与配置 | 建立配置管理和日志体系 |
| 11 | Docker 部署 | 提供容器化运行环境 |
| 12 | 前端 | 提供聊天和文件上传界面 |

## 4. 开发顺序

MVP 阶段优先完成最小可用 RAG 链路，开发顺序为模块 0 到模块 7。能力扩展阶段依次建设模块 8 到模块 11。前端模块 12 放在后端链路稳定后按需建设。

## 5. 模块详细计划

### 5.1 模块 0：项目初始化

目标：

- 建立正式项目目录结构。
- 配置 Python 环境。
- 启动最小 FastAPI 服务。
- 建立项目文档目录。

交付内容：

- 项目根目录。
- `.gitignore`。
- `backend/` 目录。
- `backend/app/` 应用目录。
- `backend/requirements.txt`。
- `backend/.env.example`。
- `backend/Dockerfile`。
- `backend/main.py`。
- `docs/` 文档目录。
- `uploads/` 上传文件目录。
- `uploads/.gitkeep`。
- `README.md`。
- `docker-compose.yml`。
- FastAPI 根接口。

建议结构：

```
LocalMind/
├── .gitignore
├── backend/
│   ├── app/
│   │   └── __init__.py
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── docs/
│   ├── LocalMind_Product_Spec.md
│   ├── LocalMind_System_Design.md
│   ├── Specification.md
│   ├── About user.md
│   ├── product_spec.md
│   ├── system_design.md
│   ├── api_spec.md
│   ├── database_schema.md
│   └── deployment.md
├── uploads/
│   └── .gitkeep
├── README.md
└── docker-compose.yml
```

`docs/` 目录用于存放项目设计和交付文档，避免规格说明、系统设计、API 设计和部署说明散落在项目根目录。模块 0 阶段只需要建立文档文件占位，后续模块逐步补全内容。

`.gitignore` 需要覆盖 Python 缓存、虚拟环境、本地环境变量和运行日志，避免将 `__pycache__/`、`.venv/`、`.env`、`*.log` 等本地生成内容提交到仓库。

`uploads/.gitkeep` 用于让 Git 跟踪空的上传目录。`backend/Dockerfile` 与根目录 `docker-compose.yml` 保持配套，确保容器化运行入口不是无效占位。

基础接口：

```http
GET /
```

响应：

```json
{
  "status": "ok"
}
```

验收标准：

- Python 虚拟环境已创建。
- `backend/requirements.txt` 依赖已安装。
- uvicorn 能正常启动。
- `localhost:8000` 可访问。
- Swagger 页面可打开。
- 项目已完成 Git 初始化。
- `.gitignore` 已忽略虚拟环境、Python 缓存、环境变量文件和运行日志。
- `docs/` 目录已创建，并包含产品规格、系统设计、API 设计、数据库设计和部署说明的占位文档。
- `uploads/` 目录已创建，并通过 `.gitkeep` 纳入版本控制。
- `backend/Dockerfile` 与 `docker-compose.yml` 已创建，具备后续容器化运行基础。

### 5.2 模块 1：FastAPI 基础 API

目标：

- 建立 API 路由体系。
- 建立统一响应结构。
- 建立异常处理机制。

交付内容：

- `app/api/` 路由目录。
- 统一响应格式。
- 404、500、validation error 异常处理。
- Health Check 接口。

统一响应示例：

```json
{
  "success": true,
  "data": {},
  "message": "ok"
}
```

Health Check：

```http
GET /health
```

验收标准：

- API 分层结构清晰。
- Swagger 可展示接口。
- 错误响应为统一 JSON 结构。
- Health Check 返回正常。

### 5.3 模块 2：OpenAI-compatible Chat API

目标：

- 实现基础 Chat Completion 能力。
- 对外保持 OpenAI-compatible 响应格式。

接口：

```http
POST /v1/chat/completions
```

请求示例：

```json
{
  "model": "gpt-4.1-mini",
  "messages": [],
  "stream": false
}
```

交付内容：

- 请求 Schema。
- OpenAI API 调用封装。
- OpenAI-compatible 响应转换。
- 基础错误处理。

验收标准：

- Postman 可调用。
- Swagger 可测试。
- 模型能返回结果。
- 响应格式兼容 OpenAI。

### 5.4 模块 3：数据库系统

目标：

- 接入 PostgreSQL。
- 建立基础数据表和迁移机制。

交付内容：

- SQLAlchemy。
- asyncpg。
- 数据库连接配置。
- Alembic migration。
- 基础表：`users`、`chat_sessions`、`chat_messages`。

验收标准：

- PostgreSQL 连接正常。
- migration 可执行。
- 数据可写入和读取。
- 基础 CRUD 正常。

### 5.5 模块 4：文件上传系统

目标：

- 支持 PDF、txt、Markdown 文件上传。
- 保存文件元数据。

接口：

```http
POST /documents/upload
```

交付内容：

- 上传接口。
- `uploads/` 文件目录。
- 文件名、大小、路径等 metadata 入库。
- 文件列表查询能力。

验收标准：

- 文件上传成功。
- 文件可持久化保存。
- metadata 正常写入数据库。
- 可查询文件列表。

### 5.6 模块 5：RAG 文本处理系统

目标：

- 解析文档。
- 清洗文本。
- 生成可检索文本块。

交付内容：

- PDF Parser，建议使用 `pymupdf`。
- 文本清洗函数。
- Chunking 策略。
- chunk metadata：`chunk_index`、`source`、`document_id`。

验收标准：

- PDF 可提取文本。
- 文本切块结果稳定。
- chunk 可写入数据库。
- chunk 与原始文档可追溯。

### 5.7 模块 6：Embedding + pgvector

目标：

- 生成文本向量。
- 存储向量。
- 支持相似度检索。

交付内容：

- pgvector 扩展。
- `embeddings` 表。
- Embedding API 调用封装。
- 向量写入逻辑。
- similarity search 查询。

验收标准：

- Embedding 生成正常。
- 向量可写入数据库。
- similarity search 可返回相关结果。
- 查询结果包含原始 chunk 引用。

### 5.8 模块 7：RAG Query 系统

目标：

- 提供完整知识库问答能力。

接口：

```http
POST /v1/rag/query
```

交付内容：

- 问题 Embedding。
- top-k retrieval。
- Prompt 拼接。
- LLM 调用。
- sources 返回。

验收标准：

- 能基于文档回答问题。
- 能返回引用来源。
- retrieval 结果基本准确。
- 无相关内容时有明确 fallback。

### 5.9 模块 8：Provider Adapter 层

目标：

- 支持多模型厂商接入。
- 保持外部接口稳定。

交付内容：

- `BaseProvider` 抽象接口。
- `OpenAIProvider`。
- `DeepSeekProvider`。
- `QwenProvider`。
- `ModelRouter`。

路由输入示例：

```json
{
  "model": "deepseek-chat"
}
```

验收标准：

- 多模型可切换。
- 外部请求格式不变。
- Provider 可扩展。
- 模型调用错误能被统一处理。

### 5.10 模块 9：Streaming

目标：

- 支持 Chat API 流式输出。

请求参数：

```json
{
  "stream": true
}
```

交付内容：

- SSE 或 StreamingResponse。
- token chunk 增量返回。
- 流式错误处理。

验收标准：

- AI 回复可边生成边返回。
- 前端可实时显示。
- 连接中断时服务端能正确释放资源。

### 5.11 模块 10：日志与配置系统

目标：

- 建立统一配置入口。
- 建立请求日志和错误日志体系。

交付内容：

- `.env`。
- Settings 类。
- request logging。
- error logging。
- 配置校验。

验收标准：

- 配置集中管理。
- 敏感配置不硬编码。
- 错误可追踪。
- 日志可用于定位请求链路。

### 5.12 模块 11：Docker 部署

目标：

- 提供容器化运行方式。

交付内容：

- Dockerfile。
- docker-compose。
- PostgreSQL 容器。
- backend 容器。
- pgvector 配置。

验收标准：

- `docker compose up` 可启动服务。
- API 可正常访问。
- 后端可连接数据库。
- 数据卷和环境变量配置清晰。

### 5.13 模块 12：前端

目标：

- 提供基础 AI Chat 和文件上传界面。

建议技术栈：

- Next.js。
- Tailwind CSS。

交付内容：

- 聊天页面。
- 文件上传页面。
- Streaming 显示。
- API 调用封装。

验收标准：

- 可完成聊天。
- 可上传文档。
- 可展示流式输出。
- 错误状态有明确提示。

## 6. 交付策略

第一阶段以本地稳定运行和完整链路为目标。优先完成后端、数据库、文档处理和 RAG 查询，不提前引入复杂部署和多模型系统。

第二阶段围绕可扩展性建设 Provider Adapter、Streaming、日志和 Docker 部署，确保系统具备持续演进能力。

第三阶段根据实际使用需求建设前端，避免前端先行导致后端能力不完整。

## 7. 最终交付目标

最终系统应具备以下能力：

- OpenAI-compatible AI Gateway。
- RAG Knowledge Base。
- 可扩展 Provider Adapter。
- PostgreSQL + pgvector 向量检索。
- 可观测日志与配置管理。
- 本地和容器化部署能力。

完成以上能力后，LocalMind 可作为后续 AI Chat、知识库问答、多模型应用和 AI Agent 项目的基础后端。
