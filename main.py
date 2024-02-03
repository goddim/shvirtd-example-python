from flask import Flask
from flask import request
import os
import mysql.connector
from datetime import datetime

app = Flask(__name__)
db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_database = os.environ.get('DB_NAME')

# Подключение к базе данных MySQL
db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database,
    autocommit=True
)

@app.route('/')
def index():
    # Получение IP-адреса пользователя
    ip_address = request.headers.get('X-Forwarded-For')

    # Создание объекта cursor
    cursor = db.cursor()

    # Запись в базу данных
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    query = "INSERT INTO requests (request_date, request_ip) VALUES (%s, %s)"
    values = (current_time, ip_address)
    cursor.execute(query, values)
    db.commit()

    # Закрытие объекта cursor
    cursor.close()

    return f'TIME: {current_time}, IP: {ip_address}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
