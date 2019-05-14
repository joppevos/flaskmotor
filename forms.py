from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class LoginForm(FlaskForm):
    age    = StringField('age', validators=[DataRequired()])
    amount    = StringField('amount', validators=[DataRequired()])
    dick    = StringField('dick', validators=[DataRequired()])
    submit = SubmitField('calculate')

    def validate_name(self, form):
        try:
            val = int(form)
        except ValueError:
            ValidationError("That's not an int!")
