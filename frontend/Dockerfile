# 使用官方的 Nginx 作為基底映像
FROM nginx:stable

# 設置作者信息
LABEL maintainer="a920604a@gmail.com"

# 將本地的 nginx.conf 配置文件複製到 Nginx 預設配置目錄中
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# 將 dist 資料夾中的內容複製到 Nginx 的靜態文件目錄中
COPY app/dist/ /usr/share/nginx/html/

# 預設情況下，nginx:stable 映像已經設置了 EXPOSE 80

# CMD 指令不需要特別定義，因為父映像 nginx:stable 已經包含了啟動 Nginx 的配置