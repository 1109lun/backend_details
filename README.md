# backend_details

本專案為一個前後端分離的待辦事項應用，前端使用 React、後端使用 FastAPI，資料庫為 PostgreSQL（可透過 Docker 啟動）。

---

## 🚀 快速啟動方式（開發環境）

### ✅ 1. 啟動後端（FastAPI）

進入後端專案資料夾：

```bash
cd todo-api
poetry install            
poetry run uvicorn main:app --reload
```