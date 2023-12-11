FROM python:3.12.1-bookworm
WORKDIR /app
COPY ./my_portfolio ./

RUN pip install --upgrade pip --no-cache-dir

RUN pip install -r /app/requirements.txt --no-cache-dir

RUN python manage.py makemigrations

RUN python manage.py migrate

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8000"]