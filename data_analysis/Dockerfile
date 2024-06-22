# 使用官方的Python映像作為基礎映像
FROM python:3.9.6-slim

# 確保apt包是最新的
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 設置工作目錄
WORKDIR /app

# 複製應用程序所需文件
COPY requirements.txt /app/
COPY . /app

# 安裝依賴項
RUN pip install --no-cache-dir -r requirements.txt

# 啟動Streamlit應用程序
CMD ["streamlit", "run", "app/clothes_app.py", "--server.port", "8501"]
