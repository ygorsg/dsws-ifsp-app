# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, make_response, redirect, abort
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    return '<p>Seu navegador é {}</p>'.format(user_agent)

@app.route('/codigostatusdiferente')
def codigostatusdiferente():
    resp = make_response("Bad request", 400)
    resp.headers['X'] = 'Y'
    return resp

@app.route('/objetoresposta')
def objetoresposta():
    resp = make_response('<h1>This document carries a cookie!</h1>')
    resp.set_cookie('Cookie','Ygor')
    return resp

@app.route('/redirecionamento')
def redirecionamento():
    return redirect("https://ptb.ifsp.edu.br/", code=302)

@app.route('/abortar')
def abortar():
    abort(404)