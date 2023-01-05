import hashlib
from flask_login import LoginManager

from app.auth.models import User


def create_login_manager():
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    return login_manager


login_manager = create_login_manager()


@login_manager.user_loader
def load_user(user_id):
    """Load user"""
    return User.select().where(User.id == int(user_id)).first()


def check_permissions(current_user_id: int):
    user = User.select().where(User.id == current_user_id).first()
    if user.role.name != 'admin':
        return False
    return True


def get_avatar(email: str, size: int = 100):
    digest = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    url = f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'
    return url
