from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ivan'}
    return render_template('index.html', title='Home Page',user=user)
