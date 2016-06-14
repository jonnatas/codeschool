FROM python:3.4-slim

COPY freeze-requirements.txt /usr/

RUN apt-get update && apt-get install -y  sqlite3 \
                    npm \
                    gettext \
                    gcc

RUN pip install --upgrade pip

RUN pip install -r /usr/freeze-requirements.txt

RUN pip install --no-deps ejudge
RUN npm install -g bower

RUN apt-get install -y vim

EXPOSE 8000
