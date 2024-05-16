import pytest

"""
Check id and country_code.
"""


def check_country_code(parsed_json, value_param):
    country_codes = []
    for item in parsed_json['items']:
        country_code = item['country']['code']
        country_id = item['id']
        country_codes.append((country_id, country_code))

    if country_codes:
        for country_id, country_code in country_codes:
            if country_code != value_param:
                pytest.fail(f'Error-> id:{country_id}, сountry_code:"{country_code}"')
    else:
        pytest.fail("Error: The country_codes list is empty")
