from flask import Flask
from flask import escape, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    return '<h1>hello totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user(name):
    return 'user page %s' % escape(name)


@app.route('/test')
def test_for_url():
    print(url_for('hello'))
    print(url_for('user', name='guo1'))
    print(url_for('user', name='guo2'))
    print(url_for('test_for_url'))
    print(url_for('test_for_url', num=2))
    return 'test page'