import random
from typing import List

from app.auth.utils import get_avatar
from generate_data.tools.generate_users import UsersDTO, main as generate_users
from generate_data.data.user_data import emails_data
from generate_data.data.profile_data import ProfileDTO, POSITIONS


def generate_profile(users: UsersDTO, positions: List[str]):
    """Generate profiles"""
    profiles = []
    for user in users:
        avatar = get_avatar(user.email)
        info = random.choice(positions)
        profiles.append(ProfileDTO(info, avatar))
    return profiles


def main():
    """Return profiles and users"""
    users = generate_users(emails_data)
    profiles = generate_profile(users, POSITIONS)
    return users, profiles
