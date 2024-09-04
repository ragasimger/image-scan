FROM python:3.11.9-alpine3.20

WORKDIR /image_scan
COPY requirements.txt /image_scan/

RUN apk update && apk add --no-cache git gcc musl-dev \
    && pip install -r requirements.txt

COPY . /image_scan
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "sh", "entrypoint.sh" ]
