# Python rasmidan foydalanamiz
FROM python:3.12

# Ishlash katalogini o'rnatamiz
WORKDIR /app

# Dastur kodini konteynerga nusxalaymiz
COPY . /app

# Dastur uchun zarur bo'lgan paketlarni o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# Portni ochamiz
EXPOSE 8000

# Dastur ishga tushiriladi
CMD ["python", "app.py"]
