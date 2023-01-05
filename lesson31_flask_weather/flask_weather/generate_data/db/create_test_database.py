from app.auth.models import User, Profile, Role
from generate_data.main import main as generate_users_profiles
from generate_data.data.user_data import ROLES


def write_roles_to_db(roles):
    """Write roles to db"""
    roles_indexes = {}
    for role in roles:
        role_instance = Role(
            name=role
        )
        role_instance.save()
        roles_indexes['role'] = role_instance.id
    return roles_indexes


def write_profile_to_db(profile):
    """Write profile to db"""
    profile_instance = Profile(
        avatar=profile.avatar,
        info=profile.info
    )
    profile_instance.save()
    return profile.id


def write_user_to_db(user, profile_id, role_id):
    """Write profile to db"""
    user_instance = User(
        name=user.name,
        email=user.email,
        password=user.password,
        role=role_id,
        profile=profile_id
    )
    user_instance.save()


def create_db(db, users, profiles):
    """Fill database with test data"""
    db.create_tables([User, Profile])
    roles = write_roles_to_db(ROLES)
    for user, profile in zip(users, profiles):
        profile_id = write_profile_to_db(profile)
        role_id = roles[user.role]
        write_user_to_db(user, profile_id, role_id)


USERS, PROFILES = generate_users_profiles()
