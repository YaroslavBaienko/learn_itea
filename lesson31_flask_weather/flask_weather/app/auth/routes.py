import os
import imghdr
import datetime
from time import time
from flask import render_template, flash, redirect, url_for, request, current_app, abort
from flask_login import login_required, logout_user, login_user, current_user
from werkzeug.utils import secure_filename

from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm
from app.auth.models import User, Profile
from app.auth.utils import get_avatar, check_permissions


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
            user.last_visit = datetime.datetime.now()
            user.save()

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
        profile = Profile(avatar=get_avatar(form.email.data.lower()))
        profile.save()
        user = User(
            email=form.email.data.lower(),
            name=form.username.data,
            password=form.password.data,
            role=1,
            profile=profile.id
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


@auth.route('/profile/<int:user_id>')
@login_required
def show_profile(user_id):
    user = User.select().where(User.id == user_id).first()
    if not user:
        abort(404)

    if check_permissions(current_user.id):
        return render_template(
            'auth/profile.html',
            title=f'Profile {user.name}',
            user=user
        )

    if user.id != current_user.id:
        flash('You don\'t have access to this page')
        return redirect(url_for('main.index'))

    return render_template(
        'auth/profile.html',
        title=f'Profile {current_user.name}',
        user=user
    )


@auth.route('/profile/upload/avatar/<int:user_id>', methods=['POST'])
@login_required
def upload_avatar(user_id):
    if request.method == 'POST':
        user = User.select().where(User.id == user_id).first()
        filename = request.files['avatar'].filename
        if filename:
            filename = f'{time()}_{secure_filename(filename)}'
            path_to_file = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            request.files['avatar'].save(path_to_file)
            image_type = imghdr.what(path_to_file)

            if image_type not in current_app.config['ALLOWED_EXTENSIONS']:
                os.remove(path_to_file)
                flash(f'{filename} is not allowed image type')
                return redirect(url_for('auth.show_profile', user_id=user.id))

            url_to_avatar = current_app.config['UPLOAD_URL'] + filename
            profile = Profile.select().where(Profile.id == user.profile.id).first()
            profile.avatar = url_to_avatar
            profile.save()

            flash(f'{filename} uploaded')
            return redirect(url_for('auth.show_profile', user_id=user.id))

    flash('Nothing to upload')
    return redirect(url_for('auth.show_profile', user_id=user.id))


@auth.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
