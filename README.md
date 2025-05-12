# 中文 RAG + LLM 問答系統（離線部署版）

本專案是一套使用全開源技術構建的中文智慧問答系統，採用 Retrieval-Augmented Generation（RAG）架構，並可完全離線部署於 CPU-only 環境，適合企業內部部署、教育訓練或安全場域應用。

---

## 📦 專案特色

- 支援繁體中文與簡體中文語意理解與問答
- 使用 BGE-small-zh 建立語意向量檢索庫（FAISS）
- 搭配 llama.cpp 執行經指令微調的中文開源 LLM（Mistral-7B）
- 支援 Docker Compose 一鍵部署
- RESTful API 支援 `/ask` 問答與 `/prepare` 新資料上傳
- 問答記錄自動寫入 `logs/api_history.log`
- 支援 Top-K 調整、異常處理與 CORS

---

## 🛠️ 技術堆疊與授權

| 組件 | 功能 | 授權 |
|------|------|--------|
| **FAISS** | 向量資料庫 | MIT |
| **llama.cpp** | 模型執行引擎 | MIT |
| **Mistral-7B 中文微調** | LLM | Apache 2.0 |
| **BGE-small-zh** | 中文向量模型 | Apache 2.0 |
| **Flask** | API 伺服器 | BSD |
| **sentence-transformers** | 向量處理 | Apache 2.0 |

詳見 [`LICENSE.txt`](LICENSE.txt) 與 [`NOTICE.txt`](NOTICE.txt)

---

## 📁 專案結構

```
rag-llm-project/
├── data/                 # 問答資料與向量庫
│   ├── simple_qa_dataset.csv
│   ├── knowledge.index
│   └── knowledge_texts.pkl
├── models/               # 放置 GGUF 模型
│   └── mistral-7b-instruct.gguf
├── scripts/              # 處理與 API 程式
│   ├── prepare_data.py
│   └── api_server.py
├── logs/                 # 問答記錄
│   └── api_history.log
├── Dockerfile
├── docker-compose.yml
├── LICENSE.txt
└── NOTICE.txt
```

---

## 🚀 快速啟動

```bash
docker-compose up --build
```

預設會啟動在 `http://localhost:8000`

---

## 📮 API 使用說明

### 問答 `/ask`

```
POST /ask
{
  "question": "什麼是人工智慧？",
  "top_k": 3
}
```

回應：
```json
{
  "question": "...",
  "answer": "..."
}
```

### 新資料上傳 `/prepare`

```
POST /prepare
{
  "csv_file": "your_file.csv"
}
```

---

## ✅ 適用情境

- 機構內部知識查詢系統
- 客服訓練問答系統
- 離線語意問答應用
- 私有資料庫語意搜尋

---

## 🙏 致謝

感謝以下開源貢獻者社群：

- [BAAI](https://huggingface.co/BAAI)
- [Mistral AI](https://mistral.ai)
- [CH-UP](https://huggingface.co/CH-UP)
- [llama.cpp 開發者](https://github.com/ggerganov/llama.cpp)
- [FAISS 團隊](https://github.com/facebookresearch/faiss)

本專案遵循開源精神，歡迎 Fork 與改善。
