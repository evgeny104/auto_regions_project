import requests
from utils import (
    base_url, check_status_code
)
from error_params import (
    error_country, error_page,
    error_page_size
)


# Test №500,1 Let's check that by default it returns a list of regions in JSON format.
def test_validate_region_list():

    url = f"{base_url}"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)
    # Проверяем, что регионов в списке больше нуля
    assert 'total' in parsed_json
    assert parsed_json['total'] > 0

    # Проверяем, что есть ключ 'items' и он является списком
    assert 'items' in parsed_json
    assert isinstance(parsed_json['items'], list)

    # Проверяем каждый элемент в списке
    for region in parsed_json['items']:
        # Проверяем наличие необходимых ключей в каждом элементе
        assert 'id' in region
        assert 'name' in region
        assert 'code' in region
        assert 'country' in region

        # Проверяем, что ключ 'country' содержит нужные подключи
        country = region['country']
        assert 'name' in country
        assert 'code' in country


def test_countryCode_page():
    # Test №502,1 Let's weld the start page and page where param page=1.

    url = f"{base_url}"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)

    urlpage = f"{base_url}page=1"
    respons = requests.get(urlpage)
    page_data = respons.json()

    assert parsed_json == page_data, \
        "Error:params 'page=1' wasn't loaded correctly"


def test_countryCode_ru():
    # № Test 502,2 Valid data, from the query parameter coutru_code: ru.
    url = f"{base_url}country_code=ru"
    respons = requests.get(url)
    # Checking the response in json format
    try:
        parsed_json = respons.json()
    except ValueError:
        assert False, "Error: response is not in JSON format"

    check_status_code(respons)

    country_codes = []
    for item in parsed_json['items']:
        country_code = item['country']['code']
        country_codes.append(country_code)

    if country_codes:
        # Checking compliance of country codes "ru"
        country_codes_match = []
        for code in country_codes:
            country_codes_match.append(code == 'ru')

        assert all(country_codes_match), \
            f"Error: not all country codes are = ru: {country_codes}"
    else:
        assert False, "Error: no country codes found"


def test_countryCode_kg():
    # № Test 502,3 Valid data, from the query parameter country_code: kg.
    url = f"{base_url}country_code=kg"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)

    country_codes = [
        item['country']['code']
        for item in parsed_json['items']
    ]

    if country_codes:
        # Checking compliance of country codes "kg"
        country_codes_match = [
            code == 'kg'
            for code in country_codes
        ]
        assert all(country_codes_match), \
            f"Error: not all country codes are = kg: {country_codes}"
    else:
        assert False, "Error: no country codes found"


def test_countryCode_kz():
    # № Test 502,4 Valid data, from the query parameter coutru_code: kz.
    url = f"{base_url}country_code=kz"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)

    country_codes = [
        item['country']['code']
        for item in parsed_json['items']
    ]
    if country_codes:
        # Checking compliance of country codes "kg"
        country_codes_match = [
            code == 'kz'
            for code in country_codes
        ]
        assert all(country_codes_match), \
            f"Error: not all country codes are = kz: {country_codes}"
    else:
        assert False, "Error: no country codes found"


def test_countryCode_cz():
    # № Test 502,5 Valid data, from the query parameter coutru_code: cz.
    url = f"{base_url}country_code=cz"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)

    country_codes = [
        item['country']['code']
        for item in parsed_json['items']
    ]

    if country_codes:
        # Checking compliance of country codes "cz"
        country_codes_match = [
            code == 'cz'
            for code in country_codes
        ]
        assert all(country_codes_match), \
            f"Error: not all country codes are = cz: {country_codes}"
    else:
        assert False, "Error: no country codes found"


def test_negativeCase_countryCode():
    # № Test 502,6 Negative case, parameter coutru_code=test.
    url = f"{base_url}country_code=test"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)

    assert ('error' in parsed_json
            and 'message' in parsed_json['error']
            and 'id' in parsed_json['error']), \
        "Error: checking 'error' and 'message'""keys"

    assert error_country['error']['message'] == parsed_json['error']['message'], \
        "Error: spelling error in 'error' and 'message']"


def test_pageMin():  # № 503.1 Valid case, system accepts the parameter page=1
    url = f"{base_url}country_code=ru"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)

    assert all(key in parsed_json
               for key in ['total', 'items']), \
        "Error: the response no contains 'total' and 'items' elements"

    url = f"{base_url}country_code=ru&page=1"
    respons_page = requests.get(url)
    res_page = respons_page.json()
    assert parsed_json == res_page, \
        "Error: check that the minimum value = 1"


def test_pageDefault():  # № 503.2 Сheck that the default value =1
    url = f"{base_url}"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)

    assert parsed_json['total'], \
        "Error: checking the 'total' key in the JSON response"
    assert parsed_json['items'], \
        "Error: checking the 'items' key in the JSON response"

    url = f"{base_url}page=1"
    respons = requests.get(url)
    res_page = respons.json()
    assert parsed_json == res_page, \
        "Error: check that the default value = 1"


def test_page2():
    # Test for loading and comparing first letters of region codes from page 1 (page_size=10) and page 2(page_size=5).

    # Make GET request for page 1 with page_size=10
    url_page1 = f"{base_url}page=1&page_size=10"
    respons_page1 = requests.get(url_page1)
    parsed_json_page1 = respons_page1.json()

    check_status_code(respons_page1)

    # Extract first letters of region codes from page 1
    first_letters = []
    for item in parsed_json_page1['items']:
        first_letter = item['code'][0]
        first_letters.append(first_letter)
    # Remove all values except the first 5 from the list
    del first_letters[:4], first_letters[-1]

    # Make GET request for page 2 with page_size=5
    url_page2 = f"{base_url}page=2&page_size=5"
    respons_page2 = requests.get(url_page2)
    parsed_json_page2 = respons_page2.json()

    check_status_code(respons_page2)

    # Extract first letters of region codes from page 2
    first_letters_page2 = []
    for item in parsed_json_page2['items']:
        first_letter = item['code'][0]
        first_letters_page2.append(first_letter)

    # Compare first letters from page 1 with those from page 2
    assert first_letters == first_letters_page2, "Page 2 loaded with errors"


def test_pageTest():
    # № Test 503,4 Negative case, parameter page = test.
    url = f"{base_url}page=test"
    respons = requests.get(url)
    try:
        parsed_json = respons.json()
    except ValueError:
        assert False, \
            "Response is not in JSON format"

    check_status_code(respons)

    assert ('error' in parsed_json
            and 'message' in parsed_json['error']
            and 'id'), \
        "Error: the response no contains 'error' and 'message' and 'id' elements"

    assert parsed_json['error']['message'] == error_page['negative_params']['error']["message"], \
        "Error: spelling error is in 'message'"


def test_negative_pageValue():
    # № Test 503,5 Negative case, parameter page = -1.
    url = f"{base_url}page=-1"
    respons = requests.get(url)

    try:
        parsed_json = respons.json()
    except ValueError:
        assert False, \
            "Error: response is not in JSON format"

    check_status_code(respons)

    # Checking that the response contains the expected keys
    error_message = error_page['above_zero']['error']['message']

    assert parsed_json.get('error', {}).get('message') == error_message, \
        f"Error: spelling error is in 'message'. Expected:"


def test_nagativ_page():
    # № Test 503,5 Negative case, parameter page = 0.
    url = f"{base_url}page=0"
    respons = requests.get(url)

    try:
        parsed_json = respons.json()
    except ValueError:
        assert False, \
            "Error: response is not in JSON format"

    check_status_code(respons)

    # Checking that the response contains the expected keys
    error_message = error_page['above_zero']['error']['message']

    assert parsed_json.get('error', {}).get('message') == error_message, \
        f"Error: spelling error is in 'message'. Expected:"


def test_pageSize_five():
    # № Test 504,1 check the parameter: page_size=5
    url = f"{base_url}country_code=ru&page_size=5"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)

    number_regions = []

    assert parsed_json['items'], \
        "the response no contains elements 'items'"

    for item in parsed_json['items']:
        number_regions.append(item)
    if number_regions:
        assert len(number_regions) == 5, \
            "error in the quantity of elements on the page"
    else:
        assert False, \
            "no country codes found"


def test_pageSize_ten():
    # № Test 504,2 check the parameter: page_size=10
    url = f"{base_url}country_code=ru&page_size=10"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)

    all_regions = []
    for item in parsed_json['items']:
        all_regions.append(item)

    non_ru_regions = [
        region for region in all_regions
        if region['country']['code'] != 'ru']

    assert len(all_regions) == 10, \
        "Error in the number of elements on the page"
    assert not non_ru_regions, \
        f"Error regions have country codes other than 'ru': {non_ru_regions}"


def test_pageSize_limit():
    # № Test 504,3 check the parameter page_size=15.
    url = f"{base_url}page_size=15"
    respons = requests.get(url)
    parsed_json = respons.json()
    number_regions = []

    check_status_code(respons)

    for item in parsed_json['items']:
        number_regions.append(item)

    assert len(number_regions) == 15, \
        "Error in the number of elements on the page"


def test_default_pageSize():
    # № Test 504,3 Default value page_zize = 15
    url = f"{base_url}"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)

    number_regions = []
    for item in parsed_json['items']:
        number_regions.append(item)

    all_repions = len(number_regions)

    assert all_repions == 15, \
        "Error default number of elements !=15"


# № Test 504,4 Negative case, parameter page != 5, 10, 15
def test_negative_pageSize():
    url = f"{base_url}page_size=2"
    respons = requests.get(url)

    try:
        parsed_json = respons.json()
    except ValueError:
        assert False, "Error: Response is not in JSON format"

    check_status_code(respons)

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


# The test 505.1 will compare the total number of regions in the database with the variable total.
def test_total_regions():
    unique_regions = set()
    pages = 1
    while True:
        url = f"{base_url}page={pages}"
        respons = requests.get(url)
        parsed_json = respons.json()
        check_status_code(respons)

        regions = parsed_json.get("items", [])
        if not regions:
            break
        else:
            for region in regions:
                unique_regions.add(region["id"])
            pages += 1

    # Calculate the total number of unique regions
    total_unique_regions = len(unique_regions)  # len counts the number of elements.
    assert total_unique_regions == parsed_json["total"], \
        (
            f"Error: param total='{parsed_json['total']} which doesn't correspond to the actual number'"
            f"{total_unique_regions}'Error: unique regions in the database"
        )


# Test 501,1 If the 'q parameter' is satisfied, all other parameters are ignored.
def test_param_q():
    url = f"{base_url}q=моСКва&country_code=kz&page=0&page_size=0"
    respons = requests.get(url)
    parsed_json = respons.json()

    check_status_code(respons)

    assert 'name' in parsed_json['items'][0], \
        "No 'name' key in the response"

    assert parsed_json['items'][0]['name'] == 'Москва', \
        "Error in 'param g' string for fuzzy search"


# Test 501,2

def test_negativ_q():
    url = f"{base_url}q="
    respons = requests.get(url)
    try:
        parsed_json = respons.json()
    except ValueError:
        assert False, "Error: Response is not in JSON format"

    check_status_code(respons)

    assert 'name' in parsed_json['items'][0], \
        "No 'items' key in the response"
    assert parsed_json['items'][0]['name'] == 'Новосибирск', \
        "Error in 'param g' string for fuzzy search"
