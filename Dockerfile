FROM python:3.9

WORKDIR /var/app

COPY . /var/app/

RUN apt update && apt install -y libpq-dev python3-dev

RUN pip install -r requirements.txt

EXPOSE 8000

## ENTRYPOINT не указывается для того, чтобы можно было запускать и миграции и сам сервер