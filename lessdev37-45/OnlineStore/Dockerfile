# Используйте официальный образ Python как родительский образ
FROM python:3.10

# Установите рабочую директорию в контейнере
WORKDIR /app

# Скопируйте файлы зависимостей в контейнер
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте остальную часть вашего приложения в контейнер
COPY . .

# Сделайте порт 8000 доступным для мира вне контейнера
EXPOSE 8000

# Определите переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Запустите приложение при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
