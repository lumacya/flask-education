from flask import Flask  # Импортируем класс

app = Flask(__name__)  # Создаем экземпляр класса - наше приложение

@app.route('/')  # URL по которому будет запускаться функция
def index():
    return "Index Page"

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)  # Включается режим отладки !Не использовать в реальных "боевых" проектах
