FROM python:3-alpine

WORKDIR /code
COPY requirements.txt /code

RUN apk update && \
apk add --no-cache --virtual build-deps gcc python3-dev musl-dev && \
apk add postgresql-dev

RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000