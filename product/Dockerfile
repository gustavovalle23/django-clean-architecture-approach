FROM python:3.10.8-slim

WORKDIR /app

RUN apt update && apt install build-essential -y

RUN pip install --upgrade pip

COPY . .

ENV ENV $env

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]
