FROM python:3.7-slim-stretch

COPY . /app
WORKDIR /app

RUN pip install pipenv && pipenv install --system

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "hello.app:app"]