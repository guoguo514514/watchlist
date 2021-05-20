from flask import Flask, render_template
from flask import escape, url_for

app = Flask(__name__)



@app.route('/index')
def index():
    return render_template('index.html', name=name, movies=movies)


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


name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

