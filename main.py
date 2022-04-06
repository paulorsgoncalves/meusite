from flask import Flask, render_template

app = Flask(__name__)

lista_usuarios = ['Paulo', 'Roberto', 'Livia', 'Teresinha']

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

if __name__ == '__main__':
    app.run(debug=True)
    
    