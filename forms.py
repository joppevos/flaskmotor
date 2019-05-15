from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError, InputRequired


def validate_digit(form, field):
    try:
        val = int(field.data)
    except (ValueError, TypeError):
        # message = field.gettext("Please enter a number")
        field.errors[0] = ("Please enter a number")
        # raise ValidationError("Please enter a number")


class LoginForm(FlaskForm):
    age = IntegerField('age', validators=[InputRequired(), validate_digit])
    amount = IntegerField('amount', validators=[InputRequired(), validate_digit])
    typemotor = SelectField(u'Programming Language',
                            choices=[('Tour', 'Tour'), ('Sport', 'Sport'), ('Cruiser', 'Cruiser')])
    submit = SubmitField('Calculate!')
    dick = IntegerField('dick', validators=[InputRequired()])


