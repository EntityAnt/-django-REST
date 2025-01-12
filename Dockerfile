FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /

RUN pip install -r /requirements.txt --no-cache-dir

COPY . .
CMD ["gunicorn", "vehicle.wsgi:application", "--bind", "0.0.0.0:8000"]



