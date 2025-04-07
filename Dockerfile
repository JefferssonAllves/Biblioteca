# syntax=docker/dockerfile:1

FROM python:3.12.9-slim as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



COPY Biblioteca /Biblioteca
COPY scripts /scripts


WORKDIR /Biblioteca

RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev-compat \
    libmariadb-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

ENV PATH="/scripts:/venv/bin:$PATH"
EXPOSE 8000

CMD ["commands.sh"]