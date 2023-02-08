FROM python:3.10.8-slim

WORKDIR /app

RUN apt update && apt install build-essential -y

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

ENV ENV $env

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
