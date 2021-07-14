from fastapi import FastAPI, status, Request
import uvicorn
import os
from logging.config import dictConfig
import socket


app = FastAPI()


@app.get("/info", status_code=status.HTTP_200_OK)
def read_root():
    return {
        "Hello": "World",
        "message": "go to '/' , '/health' and '/error' endpoints to discover more.",
    }


@app.get("/", status_code=status.HTTP_200_OK)
def info(request: Request):
    res = {
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "remote-address": "{}:{}".format(request.client.host, request.client.port),
        "method": "{} {} {} {}".format(
            request.method,
            request.scope.get("path"),
            request.scope.get("scheme", "").upper(),
            request.scope.get("http_version"),
        ),
    }
    headers = dict(request.headers.items())
    res = {
        **res,
        **headers,
    }
    return res


@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return {"health": "OK"}


@app.get("/error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
def error():
    raise Exception("error endpoint check logs ...")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=bool(os.getenv("DEBUG")))
