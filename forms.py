from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError, InputRequired


def validate_digit(form, field):
    try:
        val = int(field.data)
    except ValueError:
        message = field.gettext("Please enter a number")
        # field.errors.append("Please enter a number")
        raise ValidationError("Please enter a number")


class LoginForm(FlaskForm):
    age    = IntegerField('age', validators=[InputRequired(), validate_digit])
    amount    = IntegerField('amount', validators=[InputRequired(), validate_digit])
    dick    = IntegerField('dick', validators=[InputRequired(), validate_digit])
    submit = SubmitField('calculate')


