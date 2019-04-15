from flask import Flask, render_template
app = Flask(__name__)

posts = [
    { 'author': 'Corey Shave',
      'title': 'Something random',
      'content': 'first post content',
      'date': '2018-01-05'
    },
    { 'author': 'Joe bill',
      'title': 'Something random',
      'content': 'second post content',
      'date': '2018-03-05'
    }
]

@app.route('/about')
def about_page():
    return render_template('home.html', posts=posts)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', title='Home page')