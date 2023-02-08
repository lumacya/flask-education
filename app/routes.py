from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ivan Gibert'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Nice weather in Moscow'
        },
        {
            'author': {'username': 'Michael'},
            'body': 'The Puss in Boots 2 is awesome'
        },
        {
            'author': {'username': 'Ivan'},
            'body': "I'm studying flask"
        },
        {
            'author': {'username': 'Marcel'},
            'body': 'On my way to work'
        }
    ]
    return render_template('index.html', title='Home Page',user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
