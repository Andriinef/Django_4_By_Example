# Взять официальный базовый образ Python платформы Docker
FROM python:3.10.6

ARG PIPENV_EXTRA_ARGS

# Задать переменные среды
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Задать рабочий каталог
WORKDIR /code

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

# Команда для запуска приложения
CMD ["pipenv", "run"]
