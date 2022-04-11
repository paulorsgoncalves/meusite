from flask import Flask, render_template, url_for, request, flash, redirect
from sitepaulo.forms import FormLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy
from sitepaulo.models import Usuario, Post

app = Flask(__name__)

lista_usuarios = ['Paulo', 'Roberto', 'Livia', 'Teresinha']

app.config['SECRET_KEY'] = 'e649fa424ae88f4de15c8126a1ef2f33'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
