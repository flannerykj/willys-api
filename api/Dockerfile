# My Site
# Version: 1.0

FROM python:3.6
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    mysql-server \
    libffi-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools \
    vim

RUN pip install -U pipenv
ADD docker-entrypoint.sh /
RUN ["chmod", "+x", "/docker-entrypoint.sh"]
# RUN pipenv install --system
# Server
EXPOSE 8000
STOPSIGNAL SIGINT
# CMD cd /app
# && pipenv install --system && python manage.py runserver 0.0.0.0:8000
ENTRYPOINT ["/docker-entrypoint.sh"]
