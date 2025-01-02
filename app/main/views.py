from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..email import send_email, send_simple_message
from . import main
from .forms import NameForm

@main.route('/', methods=['GET', 'POST'])
def index():
    users = User.query.all()
    form = NameForm()
    email = form.email.data
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data, role_id=3)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            print('Verificando variáveis de ambiente: Server log do PythonAnyWhere', flush=True)
            print('FLASKY_ADMIN: ' + str(current_app.config['FLASKY_ADMIN']), flush=True)
            print('URL: ' + str(current_app.config['API_URL']), flush=True)
            print('api: ' + str(current_app.config['API_KEY']), flush=True)
            print('from: ' + str(current_app.config['API_FROM']), flush=True)
            print('to: ' + str([current_app.config['FLASKY_ADMIN'], "flaskaulasweb@zohomail.com", email]), flush=True)
            print('subject: ' + str(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX']), flush=True)
            print('text: ' + "Novo usuário cadastrado: " + form.name.data, flush=True)

            if current_app.config['FLASKY_ADMIN']:
                print('Enviando mensagem...', flush=True)
                send_simple_message([email, current_app.config['FLASKY_ADMIN'], "flaskaulasweb@zohomail.com"], 'Novo usuário', form.name.data)
                print('Mensagem enviada...', flush=True)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False), users=users, email=email)
