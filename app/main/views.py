from datetime import datetime

from flask import session, flash, redirect, url_for, render_template, current_app

from ..email import send_email
from .. import db
from ..models import User
from .forms import NameForm
from . import main


@main.route('/', methods=['Get', 'Post'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            flash('Looks like you NEW!')
            if current_app.config['DOFLASK_ADMIN']:
                send_email(current_app.config['DOFLASK_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
            flash('Looks like you OLD!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False),
                           current_time=datetime.utcnow())

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
