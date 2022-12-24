from flask import render_template, redirect, url_for, flash, request
from datetime import datetime
from flask_paginate import Pagination, get_page_parameter

from app.main import main
from app.main.forms import NameForm, GenerateDataForm
from app.main.models import User
from generate_data.main import main as generate_data
from generate_data.data import emails_data
from app.main.utils import parse_range_from_paginator


@main.route('/', methods=['POST', 'GET'])
def index():
    """Home page"""
    form = GenerateDataForm()

    if form.validate_on_submit():
        if not User.select():
            emails = generate_data(emails_data)
            for name, email in emails:
                user = User(name=name, email=email)
                user.save()
            flash('Database filled with test data')
        else:
            flash('Database is not empty')

    return render_template(
        'index.html',
        title='Home page',
        current_time=datetime.utcnow(),
        form=form
    )


@main.route('/email', methods=['POST', 'GET'])
def add_email():
    """Add name and email form page"""
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = f'User with name {name} already registered'
        if not User.select().where(User.email == email):
            user = User(name=name, email=email)
            user.save()
            message = f'User with name {name} just registered'

        flash(message)
        return redirect(url_for('main.add_email'))

    return render_template(
        'main/email.html',
        title='Register user',
        form=form
    )


@main.route('/show_emails')
def show_emails():
    """Show user information"""
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)

    users = User.select()
    pagination = Pagination(page=page, total=users.count(), search=search, record_name='users')
    start, stop = parse_range_from_paginator(pagination.info)
    return render_template(
        'main/show_emails.html',
        title='Show users',
        users=users[start:stop],
        pagination=pagination,
    )


@main.route('/delete_emails', methods=['POST'])
def delete_emails():
    """Delete selected users"""
    if request.method == 'POST':
        message = 'Deleted: '
        selectors = list(map(int, request.form.getlist('selectors')))

        if not selectors:
            flash('Nothing to delete')
            return redirect(url_for('main.show_emails'))

        for selector in selectors:
            user = User.get(User.id == selector)
            message += f'{user.email} '
            user.delete_instance()

        flash(message)
        return redirect(url_for('main.show_emails'))
