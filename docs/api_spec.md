# API Specification

本文档定义 LocalMind 的 API 契约、响应结构、鉴权规则和错误码。

## 当前范围

模块一实现 FastAPI 基础 API 层：

- 根接口
- Health Check 接口
- Swagger/OpenAPI 文档
- 统一成功响应
- 统一错误响应
- 全局异常处理

模块一暂未启用鉴权。

## 响应格式

### 成功响应

```json
{
  "success": true,
  "data": {},
  "message": "ok"
}
```

### 错误响应

```json
{
  "success": false,
  "data": {},
  "message": "Not Found",
  "error": {
    "code": "NOT_FOUND",
    "details": {}
  }
}
```

## 接口

### GET /

返回基础服务状态。

响应：

```json
{
  "success": true,
  "data": {
    "status": "ok"
  },
  "message": "ok"
}
```

### GET /health

返回健康检查状态。

响应：

```json
{
  "success": true,
  "data": {
    "status": "ok"
  },
  "message": "ok"
}
```

### GET /docs

返回 FastAPI 生成的 Swagger UI。

### GET /openapi.json

返回 FastAPI 生成的 OpenAPI Schema。

## 错误码

| HTTP 状态码 | 错误码 | 说明 |
| --- | --- | --- |
| 404 | `NOT_FOUND` | 路由或资源不存在 |
| 422 | `VALIDATION_ERROR` | 请求参数校验失败 |
| 500 | `INTERNAL_SERVER_ERROR` | 未预期的服务端错误 |
| 其他 HTTP 错误 | `HTTP_ERROR` | 通用 HTTP 错误 |
