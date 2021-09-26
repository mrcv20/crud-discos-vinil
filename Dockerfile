FROM python:3.8.10-alpine
WORKDIR /app

ENV FLASK_APP=app/run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production
ENV FLASK_DEBUG=1

RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
RUN apk add build-base    

COPY app/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]