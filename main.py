import requests
from config import base_url, error_country, error_page, error_page_size


def test_country_code_page():  # № Test №502,1 Let's check that regions from all countries are displayed by default.
    url = f"{base_url}/1.0/regions"
    server_request = requests.get(url)
    regions_data = server_request.json()

    assert server_request.status_code == 200

    urlpage = f"{base_url}/1.0/regions?page=1"
    request = requests.get(urlpage)
    page_data = request.json()

    assert request.status_code == 200, "Failed to fetch regions data for page 1"
    assert regions_data == page_data


def test_country_code_ru():  # № Test 502,2 Valid data, from the query parameter coutru_code: ru.
    url = f"{base_url}/1.0/regions?country_code=ru"
    request = requests.get(url)

    try:
        data = request.json()
    except ValueError:
        assert False, "Response is not in JSON format"

    country_codes = [item['country']['code'] for item in data['items']]

    assert request.status_code == 200
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'ru' for code in country_codes), f"Not all country codes are == ru : {country_codes}"


def test_country_code_kg():  # № Test 502,3 Valid data, from the query parameter coutru_code: kg.
    url = f"{base_url}/1.0/regions?country_code=kg"
    request = requests.get(url)
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]

    assert request.status_code == 200
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'kg' for code in country_codes), f"Not all country codes are == kg: {country_codes}"


def test_country_code_kz():  # № Test 502,4 Valid data, from the query parameter coutru_code: kz.
    url = f"{base_url}/1.0/regions?country_code=kz"
    request = requests.get(url)
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]

    assert request.status_code == 200
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'kz' for code in country_codes), f"Not all country codes are == kz: {country_codes}"


def test_country_code_cz():  # № Test 502,5 Valid data, from the query parameter coutru_code: kz.
    url = f"{base_url}/1.0/regions?country_code=cz"
    request = requests.get(url)
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]

    assert request.status_code == 200
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'cz' for code in country_codes), f"Not all country codes are == cz: {country_codes}"


def test_country_code_test():  # № Test 502,6 Negative case, parameter coutru_code=test.
    url = f"{base_url}/1.0/regions?country_code=test"
    request = requests.get(url)
    data = request.json()

    assert request.status_code == 200
    assert 'error' in data and 'message' in data['error'] and 'id' in data['error'], ("Checking 'error' and 'message' "
                                                                                      "keys")
    assert data, "list of country codes, not empty"
    assert error_country['error']['message'] == data['error']['message'], "Spelling error in 'error' and 'message']"


def test_page_min():  # № 503.1 Valid case, system accepts the parameter page=1
    url = f"{base_url}/1.0/regions?country_code=ru"
    request = requests.get(url)
    response_regions = request.json()
    assert request.status_code == 200
    assert all(key in response_regions for key in ['total', 'items']), "Check erorr 'total' and 'items' keys"

    url = f"{base_url}/1.0/regions?country_code=ru&page=1"
    server_request_page = requests.get(url)
    result_page1 = server_request_page.json()
    assert response_regions == result_page1, "Сheck that the minimum value = 1"


def test_page_default():  # № 503.2 Сheck that the default value =1
    url = f"{base_url}/1.0/regions"
    request = requests.get(url)
    data_regions = request.json()
    assert request.status_code == 200
    assert data_regions['total'], "Checking the 'total' key in the JSON response"
    assert data_regions['items'], "Checking the 'items' key in the JSON response"

    url = f"{base_url}/1.0/regions?page=1"
    request = requests.get(url)
    data_page = request.json()
    assert data_regions == data_page, "Сheck that the default value =1"


def test_page2():  # № 503.3 Сheck GET reques with the page=2 parameter.
    url = f"{base_url}/1.0/regions?page=1&page_size=10"
    request = requests.get(url)
    data = request.json()
    assert request.status_code == 200

    first_letters = []  # for loop variable

    for item in data['items']:  # Extracting the first letters of region codes from the page 1.
        first_letter = item['code'][0]  # Extract first letter
        first_letters.append(first_letter)

    del first_letters[:4], first_letters[-1]  # Remove all values from the list, page 1.

    url = f"{base_url}/1.0/regions?page=2&page_size=5"
    request = requests.get(url)
    data = request.json()
    assert request.status_code == 200
    first_letters_page2 = []  # for loop variable

    for item in data['items']:  # Extracting the first letters of region codes from the  page 2.
        first_letter = item['code'][0]  # Extract first letter
        first_letters_page2.append(first_letter)

    assert first_letters == first_letters_page2, "Page 2 loaded with error"


def test_page_negative():  # № Test 503,4 Negative case, parameter page = test.
    url = f"{base_url}/1.0/regions?page=test"
    request = requests.get(url)

    try:
        data = request.json()
    except ValueError:
        assert False, "Response is not in JSON format"

    assert request.status_code == 200
    assert 'error' in data and 'message' in data['error'] and 'id', "Check erorr 'error' and 'message' and 'id' keys"
    assert data['error']['message'] == error_page['negative_params']['error']['message'], ("Spelling error is in "
                                                                                           "'message'")


def test_page_above_zero():  # № Test 503,5 Negative case, parameter page = -1.
    url = f"{base_url}/1.0/regions?page=-1"
    request = requests.get(url)

    try:
        data = request.json()
    except ValueError:
        assert False, "Response is not in JSON format"

    assert request.status_code == 200
    assert 'error' in data and 'message' in data['error'] and 'id', "Check erorr 'error' and 'message' and 'id' keys"
    assert data['error']['message'] == error_page['above_zero']['error']['message'], ("Spelling error is in "
                                                                                      "'message'")


def test_page_zero():  # № Test 503,5 Negative case, parameter page = 0.
    url = f"{base_url}/1.0/regions?page=0"
    request = requests.get(url)

    try:
        data = request.json()
    except ValueError:
        assert False, "Response is not in JSON format"

    assert request.status_code == 200
    assert 'error' in data and 'message' in data['error'] and 'id', "Check erorr 'error' and 'message' and 'id' keys"
    assert data['error']['message'] == error_page['above_zero']['error']['message'], ("Spelling error is in "
                                                                                      "'message'")


def test_page_size_five():  # № Test 504,1 Can accept significant 5
    url = f"{base_url}/1.0/regions?country_code=ru&page_size=5"
    request = requests.get(url)
    data = request.json()
    number_regions = []  # for loop variable

    assert request.status_code == 200
    for item in data['items']:
        number_regions.append(item)

    assert len(number_regions) == 5, "Error in the number of elements on the page"


def test_page_size_ten():  # № Test 504,2 Can accept significant 10
    url = f"{base_url}/1.0/regions?country_code=ru&page_size=10"
    request = requests.get(url)
    data = request.json()
    number_regions = []  # for loop variable
    country_codes = [item['country']['code'] for item in data['items']]

    assert request.status_code == 200

    for item in data['items']:
        number_regions.append(item)

    assert len(number_regions) == 10, "Error in the number of elements on the page"
    assert all(code == 'ru' for code in country_codes), f"Not all country codes are == ru : {country_codes}"


def test_page_size_fifteen():  # № Test 504,3 Can accept significant 15
    url = f"{base_url}/1.0/regions?page_size=15"
    request = requests.get(url)
    data = request.json()
    number_regions = []  # for loop variable
    assert request.status_code == 200

    for item in data['items']:
        number_regions.append(item)

    assert len(number_regions) == 15, "Error in the number of elements on the page"


def test_page_size_default():  # № Test 504,3 Default value = 15
    url = f"{base_url}/1.0/regions?country_code=ru"
    request = requests.get(url)
    data = request.json()
    number_regions = []  # for loop variable

    assert request.status_code == 200

    for item in data['items']:
        number_regions.append(item)

    assert len(number_regions) == 15, "Default value != 15"


def test_page_size_params_two():  # № Test 504,4 Negative case, parameter page != 5, 10, 15
    url = f"{base_url}/1.0/regions?page_size=2"
    request = requests.get(url)

    try:
        data = request.json()
    except ValueError:
        assert False, "Response is not in JSON format"

    assert request.status_code == 200
    assert 'error' in data and 'message' in data['error'] and 'id', "Check erorr 'error' and 'message' and 'id' keys"
    assert data['error']['message'] == error_page_size['error']['message'], ("Spelling error is in "
                                                                             "'message'")


def test_total_regions_count():
    page_url = f"{base_url}/1.0/regions"
    unique_regions = set()  # Create an empty set to store unique regions
    page = 1

    while True:
        url = f"{page_url}?page={page}"
        response = requests.get(url)
        assert response.status_code == 200, f"Failed to retrieve data from the server at page {page}"

        data = response.json()
        regions = data.get("items", [])

        if not regions:
            break

        unique_regions.update(region["id"] for region in regions)
        page += 1

    total_count = len(unique_regions)
    assert total_count == data[
        "total"], f"Total count '{data['total']}' does not match the actual count '{total_count}' of unique regions"
