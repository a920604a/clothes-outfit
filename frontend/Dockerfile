# 使用 node 來建置前端應用
FROM node:18 AS build

# 設定工作目錄
WORKDIR /app

# 複製 package.json 和 package-lock.json
COPY app/package*.json ./


# 安裝相依套件
RUN npm install

# 複製專案檔案
COPY app/. . 

# 編譯專案
RUN npm run build

# 用 nginx 提供服務
FROM nginx:alpine
# 複製建置後的檔案到 nginx html 資料夾
COPY --from=build /app/dist  /usr/share/nginx/html


# 替代 nginx 預設設定
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 開放端口
EXPOSE 80

# 啟動 nginx
CMD ["nginx", "-g", "daemon off;"]