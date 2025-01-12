FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /

RUN pip install -r /requirements.txt --no-cache-dir

COPY . .

RUN pip install gunicorn

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]



