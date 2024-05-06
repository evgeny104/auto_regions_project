from env_vars.config import URL
from settings.module.parsed_json import (
    get_response, check_status_code)
from settings.params.api_errors import (
    error_country, error_page, error_page_size)


def test_validate_region_list():
    # Test №500,1 Let's check that by default it returns a list of regions in JSON format.

    url = f"{URL}country_code=kg"
    response, parsed_json = get_response(url)
    check_status_code(response)

    assert 'total' in parsed_json
    assert parsed_json['total'] > 0

    # Checking elements "items" in list
    for region in parsed_json['items']:

        # Checking all elements in array "items".
        assert 'id' in region
        assert 'name' in region
        assert 'code' in region
        assert 'country' in region

        country = region['country']
        assert 'name' in country
        assert 'code' in country


def test_code_page():
    # Test №502.1 Checking start page with page param -> page=1.

    url = f"{URL}"
    response, parsed_json = get_response(url)
    check_status_code(response)

    # еще вызов
    url = f"{URL}page=1"
    response, parsed_page = get_response(url)
    check_status_code(response)

    assert parsed_json == parsed_page, \
        "Error:params 'page=1' wasn't loaded correctly"


def test_code_ru():
    # Test 502.2: Valid data from the query parameter countryCode: ru.

    url = f"{URL}country_code=ru"
    response, parsed_json = get_response(url)
    check_status_code(response)  # Check sataus code

    country_codes = []

    for item in parsed_json['items']:
        country_code = item['country']['code']
        country_codes.append(country_code)

    if country_codes:
        # Checking compliance of country codes "ru"
        country_codes_match = []
        for code in country_codes:
            country_codes_match.append(code == 'ru')

        # Checking for incorrect country codes
        incorrect_codes = []
        for code, match in zip(country_codes, country_codes_match):
            if not match:
                incorrect_codes.append(code)

        assert not incorrect_codes, f"Error: not all country codes are 'ru': {incorrect_codes}"
    else:
        assert False, "Error: no country codes found"


def test_code_kg():
    # № Case 502.3 Valid data, from the query parameter country_code: kg.

    url = f"{URL}country_code=kg"
    response, parsed_json = get_response(url)
    check_status_code(response)  # Check sataus code

    country_codes = []
    for item in parsed_json['items']:
        country_code = item['country']['code']
        country_codes.append(country_code)

    if country_codes:
        # Checking compliance of country codes "kg"
        country_codes_match = []
        for code in country_codes:
            country_codes_match.append(code == 'kg')

        # Checking for incorrect country codes
        incorrect_codes = []
        for code, match in zip(country_codes, country_codes_match):
            if not match:
                incorrect_codes.append(code)

        assert not incorrect_codes, f"Error: not all country codes are 'kg': {incorrect_codes}"
    else:
        assert False, "Error: no country codes found"


def test_code_kz():
    # № Case 502,4 Valid data. from the query parameter coutru_code: kz.

    url = f"{URL}country_code=kz"
    response, parsed_json = get_response(url)
    check_status_code(response)  # Check sataus code

    country_codes = []
    for item in parsed_json['items']:
        country_code = item['country']['code']
        country_codes.append(country_code)

    if country_codes:
        # Checking compliance of country codes "kg"
        country_codes_match = []
        for code in country_codes:
            country_codes_match.append(code == 'kz')

        # Checking for incorrect country codes
        incorrect_codes = []
        for code, match in zip(country_codes, country_codes_match):
            if not match:
                incorrect_codes.append(code)

        assert not incorrect_codes, f"Error: not all country codes are 'kz': {incorrect_codes}"
    else:
        assert False, "Error: no country codes found"


def test_code_cz():
    # № Case 502.5 Valid data from the query parameter coutru_code: cz.

    url = f"{URL}country_code=cz"
    response, parsed_json = get_response(url)
    check_status_code(response)  # Check sataus code

    country_codes = []
    for item in parsed_json['items']:
        country_code = item['country']['code']
        country_codes.append(country_code)

        # Checking compliance of country codes "kg"
    if country_codes:
        country_codes_match = []
        for code in country_codes:
            country_codes_match.append(code == 'cz')

            # Checking for invalid country codes
        incorrect_codes = []
        for code, match in zip(country_codes, country_codes_match):
            if not match:
                incorrect_codes.append(code)

        assert not incorrect_codes, f"Error: not all country codes are 'cz': {incorrect_codes}"
    else:
        assert False, "Error: no country codes found"


def test_negativ_country_code():
    # № Case 502.6 Negative case parameter coutru_code=test.

    url = f"{URL}country_code=test"
    response, parsed_json = get_response(url)
    check_status_code(response)  # Check sataus code

    assert ('error' in parsed_json
            and 'message' in parsed_json['error']
            and 'id' in parsed_json['error']
            ), \
        "Error: checking 'error' and 'message'""keys"

    assert error_country['error']['message'] == parsed_json['error']['message'], \
        "Error: spelling error in 'error' and 'message']"


def test_page_one():
    # Case 503.1 Valid case system accepts the parameter page=1

    url = f"{URL}country_code=ru"
    response, parsed_json = get_response(url)
    check_status_code(response)

    assert all(key in parsed_json
               for key in ['total', 'items']), \
        "Error: the response no contains 'total' and 'items' elements"
    # сравним две странички
    url = f"{URL}country_code=ru&page=1"
    response, parsed_page = get_response(url)
    check_status_code(response)

    assert parsed_json == parsed_page, \
        "Error: check that the minimum value = 1"


def test_page():
    # Case 503.2 Сheck that the default value = 1

    url = f"{URL}"
    response, parsed_json = get_response(url)
    check_status_code(response)

    assert parsed_json['total'], \
        "Error: checking the 'total' key in the JSON response"
    assert parsed_json['items'], \
        "Error: checking the 'items' key in the JSON response"

    url = f"{URL}page=1"
    response, parsed_page = get_response(url)
    check_status_code(response)
    assert parsed_json == parsed_page, \
        "Error: check that the default value = 1"


def test_pagination_page_size():
    # Case 503.3 Loading and comparing first letters of region codes from page 1 (page_size=10) and page 2(page_size=5).
    # Extract first letters of region codes from page 1

    url = f"{URL}page=1&page_size=10"
    response, parsed_json = get_response(url)
    check_status_code(response)
    size_ten = []

    for item in parsed_json['items']:
        first_letter = item['code'][0]
        size_ten.append(first_letter)

    del size_ten[:4], size_ten[-1]

    # Extract first letters of region codes from page 2.
    url = f"{URL}page=2&page_size=5"
    response, parsed_page = get_response(url)
    check_status_code(response)
    size_five = []

    for item in parsed_page['items']:
        first_letter = item['code'][0]
        size_five.append(first_letter)

    # Compare first letters from page 1 with those from page 2
    assert size_ten == size_five, "Page 2 loaded with errors"


def test_page_check():
    # Case 503,4 Negative parameter page = test.

    url = f"{URL}page=negative"
    response, parsed_json = get_response(url)
    check_status_code(response)

    assert ('error' in parsed_json
            and 'message' in parsed_json['error']
            and 'id'), \
        "Error: the response no contains 'error' and 'message' and 'id' elements"

    assert parsed_json['error']['message'] == error_page['negative_params']['error']["message"], \
        "Error: spelling error is in 'message'"


def test_page_negative():
    # Case 503.5 Negative case parameter page = -1.

    url = f"{URL}page=-1"
    response, parsed_json = get_response(url)
    check_status_code(response)

    # Checking that the response contains the expected keys
    error_message = error_page['above_zero']['error']['message']

    assert parsed_json.get('error', {}).get('message') == error_message, \
        f"Error: spelling error is in 'message'. Expected:"


def test_page_zero():
    # Case 503,5 Negative case, parameter page = 0.

    url = f"{URL}page=0"
    response, parsed_json = get_response(url)
    check_status_code(response)

    # Checking that the response contains the expected keys
    error_message = error_page['above_zero']['error']['message']

    assert parsed_json.get('error', {}).get('message') == error_message, \
        f"Error: spelling error is in 'message'. Expected:"


def test_page_size_five():
    # Case 504.1 Check the parameter: page_size=5

    url = f"{URL}country_code=ru&page_size=5"
    response, parsed_json = get_response(url)
    check_status_code(response)

    assert parsed_json['items'], \
        "Error: response not contains elements 'items'"

    number_regions = []
    for item in parsed_json['items']:
        number_regions.append(item)

    if number_regions:
        assert len(number_regions) == 5, \
            "Error: in the quantity of elements on the page"
    else:
        assert False, \
            "Error: no country codes found"


def test_pageSize_ten():
    # Case 504.2 Check the parameter: page_size=10

    url = f"{URL}country_code=ru&page_size=10"
    response, parsed_json = get_response(url)
    check_status_code(response)

    all_regions = []
    for item in parsed_json['items']:
        all_regions.append(item)

    non_ru_regions = [
        region for region in all_regions
        if region['country']['code'] != 'ru']

    assert len(all_regions) == 10, \
        "Error: in the number of elements on the page"
    assert not non_ru_regions, \
        f"Error: regions have country codes other than 'ru': {non_ru_regions}"


def test_page_size_limit():
    # Case 504.3 Check the parameter page_size=15.

    url = f"{URL}page_size=15"
    response, parsed_json = get_response(url)
    check_status_code(response)

    number_regions = []
    for item in parsed_json['items']:
        number_regions.append(item)

    assert len(number_regions) == 15, \
        "Error in the number of elements on the page"


def test_page_size_fifteen():
    # Case 504.3 Default value page_zize = 15

    url = f"{URL}"
    response, parsed_json = get_response(url)
    check_status_code(response)

    number_regions = []
    for item in parsed_json['items']:
        number_regions.append(item)

    all_repions = len(number_regions)

    assert all_repions == 15, \
        "Error default number of elements !=15"


def test_negative_page_size():
    # Case 504.4 Negative case parameter page != 5, 10, 15

    url = f"{URL}page_size=2"
    response, parsed_json = get_response(url)
    check_status_code(response)

    if 'error' not in parsed_json:
        assert False, \
            "Error: missing key element 'error'"
    else:
        if 'message' not in parsed_json['error']:
            assert False, \
                "Error: missing key element 'message'"
        if 'id' not in parsed_json['error']:
            assert False, \
                "Error: missing key element 'id'"

    assert parsed_json['error']['message'] == error_page_size['error']['message'], \
        "Spelling error is in 'message'"


def test_unique_regions():
    # Case 505.1 Will compare the total number of regions in the database with the variable total.

    pages = 1
    unique_regions = set()
    while True:
        url = f"{URL}page={pages}"
        response, parsed_json = get_response(url)
        check_status_code(response)
        regions = parsed_json.get("items", [])

        if not regions:
            break
        else:
            for region in regions:
                unique_regions.add(region["id"])
            pages += 1

    # Calculate the total number of unique regions
    # len counts the number of elements.
    all_regions = len(unique_regions)

    assert all_regions == parsed_json["total"], \
        (
            f"Error: param total='{parsed_json['total']} which doesn't correspond to the actual number'"
            f"{all_regions}'Error: unique regions in the database"
        )


def test_param_q():
    # Case 501.1 If parameter "q" is satisfied, all other parameters are ignored.

    url = f"{URL}q=моСКва&country_code=kz&page=0&page_size=0"
    response, parsed_json = get_response(url)
    check_status_code(response)

    assert 'name' in parsed_json['items'][0], \
        "No 'name' key in the response"

    assert parsed_json['items'][0]['name'] == 'Москва', \
        "Error in 'param g' string for fuzzy search"


# Test 501,2

def test_negativ_q():
    url = f"{URL}q="
    response, parsed_json = get_response(url)
    check_status_code(response)

    assert 'name' in parsed_json['items'][0], \
        "No 'items' key in the response"
    assert parsed_json['items'][0]['name'] == 'Новосибирск', \
        "Error in 'param g' string for fuzzy search"

