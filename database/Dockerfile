FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD cheesecake
EXPOSE 3306
ADD db-setup.sql /docker-entrypoint-initdb.d
