# pull official base image
FROM python:3.10.0
# set work directory
RUN apt-get update 
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
COPY pyproject.toml /
RUN curl -sSL https://install.python-poetry.org | python -
RUN PATH="$PATH:$HOME/.local/bin" && poetry self update
RUN PATH="$PATH:$HOME/.local/bin" && poetry config virtualenvs.create false
RUN PATH="$PATH:$HOME/.local/bin" && poetry install



COPY . .
