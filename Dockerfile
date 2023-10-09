 # Указываем базовый образ, который будет использоваться для контейнера
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /otokono_sekai

ENV PYTHONDONTWRITEBYTECODE 1 \
PYTHONUNBUFFERED 1

# Копируем файлы зависимостей в контейнер
COPY requirements.txt req.txt

# Устанавливаем зависимости
RUN pip install -r req.txt

RUN apt-get update \
    && apt-get install netcat -y \

RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y

# Копируем исходный код в контейнер
COPY . .
