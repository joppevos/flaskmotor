
from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '53b95a20e6ea0bb89ec81dd80b54190d'

motoren = ['hayabusa', 'bmw1200gs']


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        choice = get_motorcycle(int(form.dick.data), int(form.age.data))
        return render_template('motor_choice.html', form=form, motor=motoren[choice])
    return render_template('login.html', form=form)


def get_motorcycle(dick, age):
    if age > 40:
        return 1
    else:
        return 0


if __name__== '__main__':
    app.run(debug=True)
