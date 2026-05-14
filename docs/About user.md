# AI 后端工程能力发展规划

本文档记录个人面向 AI 工程与后端开发方向的能力建设目标。内容用于为后续学习计划、项目规划和 AI 协作提供上下文参考。

## 1. 职业目标

目标岗位方向：

- AI Engineer / LLM Application Engineer
- Backend Engineer

核心能力目标是具备独立设计、开发、部署和维护完整 AI 产品的工程能力。能力组合包括 Python、API 设计、数据库、Docker、LLM API、RAG、项目交付和系统稳定性建设。

## 2. 能力模型

| 能力域 | 目标 |
| --- | --- |
| 后端开发 | 能设计和实现稳定的 Web API、认证、文件、任务和数据服务 |
| AI 工程 | 能基于 LLM API、RAG、Agent Workflow 构建可用 AI 应用 |
| 数据系统 | 能设计数据库 Schema、索引、事务和向量检索方案 |
| 工程化 | 能完成环境配置、日志、错误处理、部署和运维 |
| 产品交付 | 能围绕真实使用场景完成闭环项目 |
| AI 协作 | 能使用 Cursor、Codex、Copilot 等工具进行需求拆解、代码生成和 Review |

## 3. 后端基础能力

### 3.1 Python

Python 是后端和 AI 工程方向的基础语言，应重点掌握：

- 面向对象编程。
- `async` / `await` 异步模型。
- 类型标注与数据模型。
- 包管理和虚拟环境。
- logging 与错误处理。
- 装饰器、生成器、多线程和多进程基础。

建议优先使用的技术栈：

- FastAPI
- uvicorn
- pydantic
- SQLAlchemy

### 3.2 API 设计

后端开发的核心工作之一是设计和实现可维护的 API。应掌握：

- RESTful API 设计。
- HTTP Method 与状态码。
- JSON 请求和响应结构。
- JWT 登录认证。
- 文件上传。
- WebSocket。
- OpenAPI / Swagger 文档。

重点是能够设计稳定的 API 契约，而不仅是调用已有接口。

### 3.3 数据库

优先学习 PostgreSQL，并结合 pgvector 建设 AI 项目所需的数据能力。

重点能力：

- SQL。
- Join。
- Index。
- Transaction。
- Schema Design。
- ORM。
- pgvector。

PostgreSQL 适合作为 AI 应用的主数据库，既能承担业务数据存储，也能通过 pgvector 支持向量检索。

### 3.4 Redis

Redis 应作为后端工程能力的一部分掌握，重点场景包括：

- 缓存。
- Session。
- Rate Limit。
- 消息队列。
- 临时状态存储。

### 3.5 Linux 与 Docker

能够在服务器环境中部署和排查应用是后端工程能力的重要组成部分。

Linux 基础：

- 常用命令。
- SSH。
- 进程管理。
- 端口排查。
- systemctl。
- nginx 基础配置。

Docker 基础：

- Dockerfile。
- docker compose。
- 容器化部署。
- 服务依赖编排。

### 3.6 Git

必须熟练掌握：

- branch。
- merge。
- rebase。
- Pull Request。
- conflict 处理。

## 4. AI 工程能力

### 4.1 LLM API

应熟悉主流模型平台的 API 使用方式：

- OpenAI Platform。
- Anthropic。
- Google AI Studio。

重点能力包括：

- Streaming。
- Tool Calling。
- Structured Output。
- Function Calling。
- System Prompt。
- Token 管理。

### 4.2 Prompt Engineering

Prompt Engineering 应服务于系统设计，而不是依赖单句提示词技巧。重点关注：

- 上下文设计。
- 输出约束。
- Tool Routing。
- Agent Workflow。
- RAG。
- 状态与记忆管理。

### 4.3 RAG

RAG 是 AI 应用工程中的核心能力。需要理解完整检索链路：

- Embedding。
- Chunking。
- Reranking。
- Vector Database。
- Retrieval Pipeline。
- Prompt 拼接。
- Sources 引用。

可使用 LangChain 和 LlamaIndex 提高开发效率，但应优先理解底层流程和数据结构。

### 4.4 向量数据库

优先掌握：

- pgvector。
- Qdrant。

个人项目阶段可优先采用 PostgreSQL + pgvector，减少系统复杂度并保持部署简单。

### 4.5 Agent Workflow

AI 工程能力不应停留在模型调用层，应逐步掌握：

- Tool Use。
- Multi-step Reasoning。
- State Management。
- Memory。
- MCP。
- 多步骤任务编排。

## 5. 算法与数据结构

AI 工程岗位不需要以算法竞赛为目标，但需要具备稳定的基础编码能力。

建议范围：

- Easy 题型熟练。
- 常见 Medium 题型掌握。
- 二叉树、链表、哈希、BFS、DFS、动态规划基础。

学习目标是提升数据结构思维、Debug 能力和代码表达能力。

## 6. 项目能力

项目能力是 AI 工程岗位的核心竞争力。优先完成具有完整闭环的项目，而不是单点 Demo。

AI SaaS 项目方向：

- AI Chat。
- RAG 知识库。
- AI Agent。
- 多模型路由。
- PDF 问答。

后端项目方向：

- 用户系统。
- JWT 认证。
- 文件系统。
- 支付。
- WebSocket。
- 队列。

## 7. AI 辅助开发能力

Spec Coding 和 AI-assisted Coding 将成为重要工程能力。重点不是让 AI 直接生成代码，而是能够清晰描述目标、拆分任务、约束输出并审查结果。

常用工具：

- Cursor。
- Windsurf。
- GitHub Copilot。
- Codex。

重点能力：

- 需求描述。
- 任务拆解。
- 代码生成约束。
- AI 代码 Review。
- 迭代修正。

## 8. 工程化能力

工程化能力决定项目能否稳定运行和长期维护。

### 8.1 环境管理

- `.env`。
- secrets。
- 配置分层。
- 环境变量管理。

### 8.2 日志与监控

- logging。
- request tracing。
- error logging。
- 错误监控。

### 8.3 部署

- Linux 部署。
- Docker 部署。
- 云服务器部署。
- nginx 反向代理。

可选平台：

- AWS。
- Cloudflare。
- Railway。
- Render。

## 9. 前端基础

无需以成为前端工程师为目标，但需要具备完成 AI 产品原型和联调的基础能力：

- HTML。
- CSS。
- JavaScript。
- fetch。
- React 基础。
- Next.js。

AI SaaS 项目可优先采用 Next.js + FastAPI 组合。

## 10. 数据意识

AI 应用的质量高度依赖数据处理质量。需要重点理解：

- 数据清洗。
- Chunking。
- Embedding。
- Indexing。
- Metadata。
- 数据权限。
- 数据更新和失效。

## 11. 数学基础

AI 工程方向不需要以模型研究为主要目标，但应理解核心概念：

- Embedding。
- Attention。
- Token。

如未来转向模型训练、算法研究或 LLM Infra，则需要加强：

- 线性代数。
- 概率论。
- 深度学习。

## 12. 英语能力

AI 领域的一手资料主要来自英文文档和社区。建议长期阅读：

- GitHub。
- RFC。
- OpenAI Docs。
- Anthropic Docs。
- Hacker News。
- Reddit。

## 13. 风险与误区

应避免以下学习方式：

- 长期只刷教程，不做项目。
- 只学习 LangChain，不理解 RAG 原理。
- 只关注 Prompt，不建设工程能力。
- 只调用模型 API，不处理数据、日志、部署和错误。

真正需要投入的方向是系统设计、Workflow、Context、数据处理和工程稳定性。

## 14. 学习路线

### 阶段一：后端基础

1. Python
2. FastAPI
3. PostgreSQL
4. Redis
5. Docker
6. Git

### 阶段二：工程能力

1. 用户认证
2. 文件上传
3. WebSocket
4. 异步任务
5. 部署

### 阶段三：AI 工程

1. OpenAI API
2. Prompt 约束
3. RAG
4. LangChain / LlamaIndex
5. Agent
6. 向量数据库

### 阶段四：高级能力

1. Kubernetes
2. 微服务
3. CI/CD
4. 模型微调
5. MCP
6. 多 Agent 系统

## 15. 六个月执行计划

### 第 1-2 个月：后端与基础设施

- Python。
- FastAPI。
- PostgreSQL。
- Redis。
- Docker。

### 第 3 个月：后端工程能力

- JWT。
- WebSocket。
- async。
- Linux。
- nginx。

### 第 4-5 个月：AI 工程能力

- OpenAI API。
- RAG。
- pgvector。
- LangChain / LlamaIndex。

### 第 6 个月：项目交付

- 完成 AI SaaS、AI Agent 或 AI 知识库项目。
- 部署上线。
- 发布 GitHub 仓库。
- 编写 README。
- 准备 Demo。
