FROM python:3.12.1-bookworm

WORKDIR /app

COPY ./my_portfolio ./

COPY .env ./


RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r /app/requirements-linux.txt --no-cache-dir

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD ["sh", "-c", "gunicorn setup.wsgi:application --bind 0.0.0.0:8000"]