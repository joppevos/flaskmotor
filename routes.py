from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, validate_digit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '53b95a20e6ea0bb89ec81dd80b54190d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    age = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.String(50), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(300), unique=True, nullable=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.text}'"


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        motor = get_motorcycle(dick=int(form.dick.data), age=int(form.age.data), budget=int(form.amount.data))
        return render_template('login.html', form=form, answer=True, motor=motor)
    return render_template('login.html', form=form, answer=False)


def get_motorcycle(dick, age, budget):
    if dick <= 15:
        if age >= 35:
            if budget >= 10000:
                'small_old_rich'
                return 'bmwgs'
            else:
                'small_old_poor'
                return 'hondashadow'

        elif age < 35:
            if budget >= 10000:
                return 'triumph'
            else:
                return 'hayabusa'

    elif dick > 15:
        if age >= 35:
            if budget >= 10000:
                return 'honda goldwing'
            else:
                return 'tjhis'

        else:
            if budget >= 10000:
                return 'wr450r'
            else:
                return 'honda vtr'



if __name__ == '__main__':
    app.run(debug=True)
