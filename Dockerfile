FROM python:3.8-alpine

WORKDIR /app

COPY . /app

RUN pip3 install -r /app/requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python", "main.py" ]