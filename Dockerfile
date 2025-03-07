# syntax=docker/dockerfile:1

FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



COPY Biblioteca /Biblioteca
COPY scripts /scripts


WORKDIR /app

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

RUN useradd --create-home --uid 10001 appuser
USER appuser


EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]