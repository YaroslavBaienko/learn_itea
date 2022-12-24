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


