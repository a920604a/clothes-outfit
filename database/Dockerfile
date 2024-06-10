FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=closet
ENV MYSQL_USER=ccc
ENV MYSQL_PASSWORD=closet
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY schema/init.sql /docker-entrypoint-initdb.d/

