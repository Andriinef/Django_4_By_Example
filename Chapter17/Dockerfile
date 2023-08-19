# Используйте официальный образ Python Docker в качестве базового образа.
FROM python:3.10.6

# Установить переменные среды
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Установить зависимости
RUN apt-get update \
    # зависимости для сборки пакетов Python и очистки неиспользуемых файлов
    && apt-get install -y build-essential \
    libcurl4-openssl-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем Pipfile и Pipfile.lock в контейнер
COPY Pipfile Pipfile.lock /code/

# Зависимости Python
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

RUN pipenv sync --system ${PIPENV_EXTRA_ARGS}


# Копировать материалы проекта
COPY ./ ./


# Установите точку входа для приложения (настройте по мере необходимости)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
