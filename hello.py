from flask import Flask, request, make_response, redirect, abort
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Avaliação contínua: Aula 030</h1>
    <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/user/Ygor Gonçalves/PT3025411/IFSP">Identificação</a></li>
    <li><a href="/contextorequisicao">Contexto da requisição</a></li>
    </ul>
    """

@app.route('/user/<nome>/<prontuario>/<instituicao>')
def identificacao(nome,prontuario,instituicao):
    return f"""
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Aluno: {nome}</h2>
    <h2>Prontuário: {prontuario}</h2>
    <h2>Instituição: {instituicao}</h2>
    <p><a href="/">Voltar</a></p>
    """

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    # ip = request.remote_addr
    ip = request.environ['REMOTE_ADDR']
    # domain = request.url_root  exibe "http://ygor.pythonanywhere.com"
    domain = request.headers['Host'] # exibe "ygor.pythonanywhere.com"
    return f"""
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Seu navegador é: {user_agent}</h2>
    <h2>O Ip do computador remoto é: {ip}</h2>
    <h2>O O host da aplicação é: {domain}</h2>
    <p><a href="/">Voltar</a></p>
    """

# === AULA 01

#@app.route('/')
#def hello_world():
#    return '<h1>Hello World!</h1>'

#@app.route('/user/<name>')
#def user(name):
#    return '<h1>Hello, {}!</h1>'.format(name)

#@app.route('/contextorequisicao')
#def contextorequisicao():
#    user_agent = request.headers.get('User-Agent')
#    return '<p>Seu navegador é {}</p>'.format(user_agent)

#@app.route('/codigostatusdiferente')
#def codigostatusdiferente():
#    resp = make_response("Bad request", 400)
#    resp.headers['X'] = 'Y'
#    return resp

#@app.route('/objetoresposta')
#def objetoresposta():
#    resp = make_response('<h1>This document carries a cookie!</h1>')
#    resp.set_cookie('Cookie','Ygor')
#    return resp

#@app.route('/redirecionamento')
#def redirecionamento():
#    return redirect("https://ptb.ifsp.edu.br/", code=302)

#@app.route('/abortar')
#def abortar():
#    abort(404)