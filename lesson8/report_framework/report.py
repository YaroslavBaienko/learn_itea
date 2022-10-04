"""
Report module of Monaco racing
Show list of drivers and optinal order
Shows statistic about driver
"""
from pathlib import Path
import os
import re
from datetime import datetime

import racing_data
from report_framework.file_handler import read_data_from_file


def get_data_from_files(folder: str):
    """Get racing data from folder"""
    if not isinstance(folder, str):
        raise TypeError('Input data must be string')

    path_to_start = os.path.join(folder, 'start.log')
    path_to_end = os.path.join(folder, 'end.log')
    path_to_abbr = os.path.join(folder, 'abbreviations.txt')

    start_log = sorted(read_data_from_file(path_to_start))
    end_log = sorted(read_data_from_file(path_to_end))
    abbr = sorted(read_data_from_file(path_to_abbr))

    return start_log, end_log, abbr


def parse_data_from_log(data: list[str]):
    """Parse data from start.log and end.log"""
    racers = {}
    datetime_format = "%Y-%m-%d %H:%M:%S.%f"
    for race in data:
        racer_abbr = re.findall(r'^[A-Z]{3}', race)
        racer_date = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', race)
        racer_time = re.findall(r'[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}$', race)

        if not all((racer_abbr, racer_date, racer_time)):
            raise ValueError('Wrong data in start.log|end.log')
        racer_abbr = racer_abbr.pop()
        racer_date = racer_date.pop()
        racer_time = racer_time.pop()

        race_datetime = datetime.strptime(f'{racer_date} {racer_time}', datetime_format)
        racers[racer_abbr] = race_datetime
    return racers


def parse_data_from_abbr(abbrs: list):
    """Parse data from abbreviations.txt"""
    abbrs_map = {}
    for line in abbrs:
        abbr, driver, company = line.split('_')
        abbrs_map[abbr] = driver, company
    return abbrs_map


def calc_results(start_data: dict[str: datetime], end_data: dict[str: datetime]):
    """Calc race results"""
    race_results = {}
    for racer, race_datetime in end_data.items():
        start_time = start_data[racer]
        end_time = race_datetime
        race_result = end_time - start_time
        race_results[racer] = str(race_result)
    return race_results


def main(folder: str):
    """Main controller"""
    start_log, end_log, abbr = get_data_from_files(folder)

    start_data = parse_data_from_log(start_log)
    end_data = parse_data_from_log(end_log)
    abbr_data = parse_data_from_abbr(abbr)

    race_results = calc_results(start_data, end_data)
    print(race_results)


if __name__ == '__main__':
    folder = str(Path(racing_data.__file__).parent.absolute())
    main(folder)
