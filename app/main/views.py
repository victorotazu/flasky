from flask import render_template, session, redirect, url_for, flash, current_app
from datetime import datetime
from . import main
from .forms import NameForm
from .. import db
from ..models import User 
from ..email import send_email


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # Try to find a user by its username in the database
        user = User.query.filter_by(username=form.name.data).first()
        # If the user doesn't exist then register it
        if user is None:
            session['known'] = False
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            # Notice the change: app -> current_app. This works because the app
            # instance and the context are handled by the factory and the BP. 
            # @TODO: Confirm this.
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                 'mail/new_user', user=user)
        else:
            session['known'] = True
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        # Notice the change: index --> .index or main.index
        # This is because the views are under a specific blueprint
        # Can use the short version (.index) as long as there's a single BP
        return redirect(url_for('.index'))
    """
    ua = request.headers.get('User-Agent')
    return '<h1>Tu browser es:{}</h1>'.format(ua)
    """
    return render_template('index.html', current_time=datetime.utcnow(), 
    form=form, name=session.get('name'), known=session.get('known', False))


@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
