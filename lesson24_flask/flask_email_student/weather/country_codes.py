import json
from datapackage import Package


def get_codes(url: str):
    """Get countries codes from datapackage json"""
    package = Package(url)

    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            return resource.read()
    return None


def prepare_data_to_json(codes: list[list[str]]):
    """Prepare data to json"""
    json_data = []
    for country_code in codes:
        country = {
            'code': country_code[1],
            'name': country_code[0],
        }
        json_data.append(country)
    return json_data


def write_codes_data_to_json(json_data: list[dict[str]], filename: str = 'countries_codes.json'):
    """Write codes data to json file"""
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file)
    return True


def read_codes_data_to_json(filename: str):
    """Read code from json file"""
    with open(filename, 'r') as json_file:
        country_json = json.load(json_file)
    return country_json


def main(url: str):
    """Main controller"""
    codes = get_codes(url)
    if not codes:
        raise RuntimeError('Countries codes data not found')
    json_data = prepare_data_to_json(codes)
    write_json = write_codes_data_to_json(json_data)
    return write_json


URL_CODES_JSON = 'https://datahub.io/core/country-list/datapackage.json'
FILENAME = 'countries_codes.json'
print(read_codes_data_to_json(FILENAME))
