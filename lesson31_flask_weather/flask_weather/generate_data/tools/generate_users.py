import random
import secrets
import string
from random import shuffle, randint, choice
from typing import NamedTuple, List

from generate_data.data.user_data import EmailData, ROLES


class UsersDTO(NamedTuple):
    full_name: str
    email: str
    password: str
    role: str


def generate_full_names(data: EmailData):
    """Generate random full names"""
    names = data.names
    surnames = data.surnames
    shuffle(names)
    shuffle(surnames)
    full_names = [f'{name.lower()}_{surname.lower()}' for name, surname in zip(names, surnames)]
    return full_names


def generate_email_names(full_names: List[str]):
    """Generate nicknames"""
    email_names = []
    for full_name in full_names:
        name, surname = full_name.split('_')
        email_name = f'{name.lower()}_{surname.lower()}{randint(1000, 9999)}'
        password = generate_password()
        role = generate_role(ROLES)
        email_names.append(UsersDTO(full_name, email_name, password, role))
    return email_names


def generate_password(pass_len: int = 10):
    """Generate password"""
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(pass_len))
    return password


def generate_role(roles: List[str]):
    """Generate roles"""
    return random.choice(roles)


def generate_users(data: EmailData, email_names: List[UsersDTO]):
    """Generate emails"""
    emails = []
    top_level_domains = data.top_level_domains
    second_level_domains = data.second_level_domains
    for full_name, nickname, password, role in email_names:
        email = f'{nickname}@{choice(second_level_domains)}.{choice(top_level_domains)}'
        emails.append(UsersDTO(full_name, email, password, role))
    return emails


def main(data: EmailData):
    """Main controller"""
    full_names = generate_full_names(data)
    email_names = generate_email_names(full_names)
    emails = generate_users(data, email_names)
    return emails
