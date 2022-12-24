import re


def parse_range_from_paginator(html: str):
    """Parse range from html"""
    match_range = re.findall(r'<b>[0-9]+ - [0-9]+</b>', html).pop()
    start, stop = map(int, re.findall(r'[0-9]+', match_range))
    return start - 1, stop
