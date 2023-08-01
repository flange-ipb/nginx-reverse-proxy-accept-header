FROM python:3.11-bookworm

WORKDIR /django

COPY . .

RUN pip install -r requirements.txt

WORKDIR /django/project

RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
