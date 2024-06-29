# 使用官方的 Node.js 作為基底映像
FROM node:latest as build

LABEL maintainer="a920604a@gmail.com"
# 設置工作目錄
WORKDIR /app

# 複製 package.json 與 package-lock.json 來安裝依賴
COPY ./app/package.json ./app/package-lock.json ./

# 安裝依賴
RUN npm install

# 複製所有檔案到工作目錄
COPY ./app .

# 建構應用
RUN npm run build

# 第二階段，使用 Nginx 伺服已建構的靜態資源
FROM nginx:alpine

# 複製建構產物到 Nginx 的預設公共目錄
COPY --from=build /app/dist /usr/share/nginx/html

# 開放 Nginx 的預設端口
EXPOSE 80

# 設置 Nginx 的預設執行命令
CMD ["nginx", "-g", "daemon off;"]
