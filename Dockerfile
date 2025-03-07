FROM python:3-alpine3.15 AS base
LABEL key="Abhishek"
WORKDIR /flask-sysutil-project
COPY . /flask-sysutil-project
RUN apk add --virtual .build-deps gcc musl-dev linux-headers && pip install --no-cache-dir -r requirements.txt && apk del .build-deps
EXPOSE 5001
CMD [ "python","app.py" ]
