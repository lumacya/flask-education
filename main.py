from flask import Flask  # Импортируем класс

app = Flask(__name__)  # Создаем экземпляр класса - наше приложение

@app.route("/")  # Декоратор указывающий по какому URL запускать функцию
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
