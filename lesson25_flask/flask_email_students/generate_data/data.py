from typing import NamedTuple, List


class EmailData(NamedTuple):
    names: List[str]
    surnames: List[str]
    top_level_domains: List[str]
    second_level_domains: List[str]


TOP_LEVEL_DOMAINS = ['biz', 'com', 'edu', 'gov', 'net', 'org']

SECOND_LEVEL_DOMAINS = ['google', 'facebook', 'instagram', 'amazon']

NAMES = ['James', 'Mary', 'Robert',	'Patricia', 'John',	'Jennifer',	'Michael', 'Linda',
         'David', 'Elizabeth', 'William', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica',
         'Thomas', 'Sarah', 'Charles', 'Karen']

SURNAMES = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
            'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
            'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin']

emails_data = EmailData(NAMES, SURNAMES, TOP_LEVEL_DOMAINS, SECOND_LEVEL_DOMAINS)
