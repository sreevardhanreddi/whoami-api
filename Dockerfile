# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . /app

# install python dependencies for the app
RUN pip3 install -r /app/requirements.txt

# expose port for the app
EXPOSE 8000

# run the app
ENTRYPOINT [ "python", "main.py" ]