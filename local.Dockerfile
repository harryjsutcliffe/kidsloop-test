# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /src
COPY . .

CMD ["python3", "-m", "robot"]