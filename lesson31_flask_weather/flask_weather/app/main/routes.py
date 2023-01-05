from flask import render_template, redirect, url_for, flash, request
from datetime import datetime
from flask_paginate import Pagination, get_page_parameter
from flask_login import login_required, current_user

from app.main import main
from app.main.forms import NameForm, GenerateDataForm
from app.auth.models import User
from generate_data.tools.generate_users import main as generate_data
from generate_data.data.user_data import emails_data
from app.main.utils import parse_range_from_paginator
from app.auth.utils import check_permissions


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


@main.route('/email/show')
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


@main.route('/email/edit/<int:user_id>')
@login_required
def edit_email(user_id):
    """Edit user"""
    if not check_permissions(current_user):
        flash('You don\'t have access to edit this item.', 'error')
        return redirect(url_for('main.index'))

    user = User.select().where(User.id == user_id).first()
    form = NameForm()
    if not user:
        flash(f'User with id: {user_id} not found. You can add user in this form.')
        return redirect(url_for('main.add_email'))

    form.id.data = user.id
    form.id.label.text = ''
    form.name.label.text = 'Edit this name'
    form.email.label.text = 'Edit this email'

    form.name.data = user.name
    form.email.data = user.email
    form.submit.label.text = 'Edit'

    return render_template(
        'main/edit_email.html',
        title=f'Edit user {user.name}',
        form=form
    )


@main.route('/email/update', methods=['GET', 'POST'])
def update_email():
    """Update user from form"""
    form = NameForm()
    if form.validate_on_submit():
        user_id = form.id.data
        user_name = form.name.data
        user_email = form.email.data

        user = User.select().where(User.id == user_id).first()
        user.name = user_name
        user.email = user_email
        try:
            user.save()
            flash(f'{user_name} updated')
        except Exception:
            flash(f'Email already added into database')

    return redirect(url_for('main.index'))


@main.route('/email/delete', methods=['POST'])
@login_required
def delete_emails():
    """Delete selected users"""
    if request.method == 'POST':
        if not check_permissions(current_user):
            flash('You don\'t have access to edit this item.', 'error')
            return redirect(url_for('main.index'))

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
