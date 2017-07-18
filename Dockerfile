FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt .

RUN set -ex; \
    \
    pip install -r requirements.txt \
    && pip install \
      flask \
      charts \
      pandas \
      sqlparse \
      psycopg2 \
      xlsxwriter

