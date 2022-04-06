from dataclasses import dataclass
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    confirmacao = PasswordField('Confirmaçao da Senha', validators=[DataRequired(), equal_to('senha')])
    botao_submit = SubmitField('Criar Conta')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    botao_login = SubmitField('Fazer Login')