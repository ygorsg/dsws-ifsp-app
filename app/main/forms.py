from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('Qual é o seu email (Envio de notificação do novo usuário)?', validators=[DataRequired()])
    submit = SubmitField('Submit')
