from flask import Flask  # Импортируем класс

app = Flask(__name__)  # Создаем экземпляр класса - наше приложение

@app.route('/user/<username>')  # URL по которому будет запускаться функция
def show_user_profile(username):
    return f"User: {username}"

@app.route('/post/<int:post_id>')  # Используется конвертер - показывает какой тип данных принимает функция в качестве аргумента
def show_post(post_id):
    return f'Post: {post_id}'

if __name__ == "__main__":
    app.run(debug=True)  # Включается режим отладки !Не использовать в реальных "боевых" проектах
