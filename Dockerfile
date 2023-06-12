FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . /app/

EXPOSE 8000
CMD ["python", "test_iqeq/manage.py", "runserver", "0.0.0.0:8000"]

