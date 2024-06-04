FROM python:3.12.3-alpine3.20
LABEL authors="Kinok0"
# Установить зависимости
RUN apk add --no-cache gcc g++ musl-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
# Копировать приложение и модели в контейнер
COPY . .
# Выставить порты
EXPOSE 5000
# Запустить приложение
CMD ["python3", "app.py"]