# Используем офицальный Python #
FROM python:3.9-slim

# Устанавливаем рабочию дерикторию #
WORKDIR /app/web/study/portal

# Копируем файл с зависимостями и устанавливаем их
# Это кэшируется, чтобы не переустанавливать зависимости при каждом изменении кода
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt



# Копируем все файлы проекта в рабочую директорию
COPY . .


# Открываем порт, на котором будет работать Gunicorn
EXPOSE 9000


# Команда для запуска приложения через Gunicorn
# main:app означает, что в файле main.py находится объект Flask с именем app
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:9000", "main:app"] 
