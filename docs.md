

# 👚 今天有衣服｜AI 衣服推薦平台

一個結合 **爬蟲 ETL、快取加速、後端 API、前端風格推薦 UI** 的服裝推薦系統，使用者可依據地點風格選擇服裝配色與性別推薦，呈現最適合的穿搭圖片與資訊。

---

## 🔧 技術架構

| 層級       | 技術                           | 功能                                 |
| -------- | ---------------------------- | ---------------------------------- |
| **前端**   | React + Tailwind CSS + Vite  | 提供地點風格選擇、顏色與性別篩選、分頁顯示              |
| **後端**   | FastAPI + SQLAlchemy + Redis | 提供 `/api/images` 查詢 API，具快取與資料查詢優化 |
| **資料來源** | Scrapy 管線爬蟲                  | 自動抓取 BEAMS 服飾資料，ETL 後寫入 MySQL      |
| **資料庫**  | MySQL                        | 儲存服飾與熱門貼文資料                        |
| **快取**   | Redis                        | 提供顏色與人氣資料快取，加速查詢                   |
| **部署**   | Docker Compose               | 一鍵啟動整合環境（前後端、DB、Cache）             |

---

## 🚀 專案啟動

```bash
# 啟動所有服務（前端、後端、資料庫、Redis）
docker-compose up --build
```

前端網址：[http://localhost:5173](http://localhost:5173)
後端 API：[http://localhost:8080/api/images](http://localhost:8080/api/images)

---

## 📸 使用流程

1. **選擇地點風格**
   👉 自動推導出推薦的顏色 palette

2. **選擇性別**
   👉 過濾服飾的性別屬性（M / W / 不限）

3. **選擇顏色**
   👉 顯示所有符合條件的穿搭圖片（含圖片 URL + 貼文連結）

4. **分頁切換**
   👉 分頁查詢支援 Redis 快取，可快速切換內容

---

## 🧠 特色亮點

* 🔁 **快取策略**：首頁熱門穿搭使用 Redis 快取，並預先快取後續頁數
* 🎯 **個性化推薦**：將地點風格轉換為顏色組合，提升推薦準確度
* 📦 **ETL 自動化流程**：

  * 使用 Scrapy 撰寫 Extract / Transform / Load 三段式 Pipeline
  * 支援帶有 hashtag 的額外處理流程

---

## 📂 專案結構

```bash
.
├── frontend/           # React + Tailwind 前端，含地點風格顏色推導與圖片展示
│   └── components/
│       └── LocationStyle.tsx  # 主元件（含樣式選擇與資料呈現）
├── backend/            # FastAPI 後端服務
│   ├── main.py         # 執行 Pipeline 抓取流程
│   ├── api/            # 提供 /images API 查詢
│   ├── utils/redis_utils.py  # Redis 快取邏輯
│   ├── frontend/fetch.py     # 資料查詢與快取核心邏輯
│   └── models/         # SQLAlchemy 定義 Clothes / Popularity
├── database/           # MySQL 初始與 Docker 設定
├── cache/              # Redis Docker 建置
├── docker-compose.yml  # 整合所有服務的部署設定
```

---

## 🔗 API 範例

```http
GET /api/images?color=black,white&gender=W&page=1&pageSize=12
```

### 回應格式：

```json
{
  "all_items": 136,
  "image_url": [...],
  "post_url": [...]
}
```

---

## 🗂 快取策略

* 查詢結果儲存於 Redis：

  * 熱門穿搭：`popularity:page1`
  * 選擇條件：`clothes:<color_key>:<gender>:pageX`
* 初次查詢自 DB 撈取，並快取未來幾頁資料
* TTL 由 `config.REDIS["EXPIRE"]` 控制（例如：3600 秒）

---

## 💡 延伸規劃

* ✨ 加入使用者個人化推薦機制（根據點擊記錄）
* 🔍 圖像搜尋（上傳圖片推薦類似風格）
* 📱 PWA 行動裝置最佳化版本
* 📝 後台管理推薦規則（新增風格與顏色對應表）

