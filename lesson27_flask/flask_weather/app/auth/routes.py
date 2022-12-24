from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, logout_user, login_user, current_user

from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm
from app.auth.models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    form = LoginForm()
    form.next.label.text = ''

    if request.method == 'GET':
        next = request.args.get('next')
        form.next.data = next

    if current_user.is_authenticated:
        flash('You are already logged in.')
        return redirect(url_for('main.index'))

    if form.validate_on_submit():
        user = User.select().where(User.email == form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = form.next.data
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password.')

    return render_template(
        'auth/login.html',
        form=form
    )


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Register login"""
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            name=form.username.data,
            password=form.password.data,
            role=1
        )
        user.save()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template(
        'auth/register.html',
        form=form
    )


@auth.route('/logout')
@login_required
def logout():
    """User login"""
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
