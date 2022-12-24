from random import shuffle, randint, choice
from typing import NamedTuple, List

from generate_data.data import EmailData


class EmailNames(NamedTuple):
    full_name: str
    email_name: str


def generate_full_names(data: EmailData):
    """Generate random full names"""
    names = data.names
    surnames = data.surnames
    shuffle(names)
    shuffle(surnames)
    full_names = [f'{name} {surname}' for name, surname in zip(names, surnames)]
    return full_names


def generate_email_names(full_names: List[str]):
    """Generate nicknames"""
    email_names = []
    for full_name in full_names:
        name, surname = full_name.split(' ')
        email_name = f'{name.lower()}_{surname.lower()}{randint(1000, 9999)}'
        email_names.append(EmailNames(full_name, email_name))
    return email_names


def generate_emails(data: EmailData, email_names: List[EmailNames]):
    """Generate emails"""
    emails = []
    top_level_domains = data.top_level_domains
    second_level_domains = data.second_level_domains
    for full_name, nickname in email_names:
        email = f'{nickname}@{choice(second_level_domains)}.{choice(top_level_domains)}'
        emails.append(EmailNames(full_name, email))
    return emails


def main(data: EmailData):
    """Main controller"""
    full_names = generate_full_names(data)
    email_names = generate_email_names(full_names)
    emails = generate_emails(data, email_names)
    return emails
