import requests
from config import error_country_code, base_url


def country_code_ru():  # №502.2 Сhecking the сoutru_code = ru Parameter.
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=ru'
    request = requests.get(url)
    if request.status_code == 200:
        data = request.json()
        country_codes = [item['country']['code']
                         for item in data['items']]
        return country_codes
    else:
        # If the status code is != 200, display an error message
        print(f" Test 'Failed' status code != 200: Status code={request.status_code}")
        return None


result = country_code_ru()
count_ru = result.count('ru')
if count_ru == len(result):
    print("Test №502.2 'Passed' all values in the list = 'ru'")
else:
    print(f"Test 'Failed' Not all values in the list = 'ru'")


def country_code_ru():  # № Test 502,2
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=ru'
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "No country codes returned"
    assert all(code == 'ru' for code in country_codes), f"Not all country codes are 'ru': {country_codes}"


def country_code_test():  # №502,6
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=test'
    request = requests.get(url)
    if request.status_code == 200:
        data = request.json()
        return data


result = country_code_test()
if error_country_code['error']['message'] == result['error']['message']:
    print("passed")
else:
    print("Failed")


def country_code_test():  # № Test 502,6
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=test'
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    assert data, "No country codes returned"
    assert error_country_code['error']['message'] == data['error']['message']


def country_code_page():  # № Test 502,1 A list of regions has been formed, starting from page 1
    url = f"{base_url}/1.0/regions"
    server_request = requests.get(url)
    if server_request.status_code == 200:
        response_data = server_request.json()
        return response_data


result = country_code_page()

urlpage = f"{base_url}/1.0/regions?page=2"
request = requests.get(urlpage)
data = request.json()

if result == data:  # let's compare two pages
    print("The lists are identical")
else:
    print("The lists are not identical")


def country_code_page():  # № Test №502,1 for Pytest
    url = f"{base_url}/1.0/regions"
    server_request = requests.get(url)
    assert server_request.status_code == 200, "Failed to fetch regions data"
    response_data = server_request.json()
    urlpage = f"{base_url}/1.0/regions?page=2"
    request = requests.get(urlpage)
    assert request.status_code == 200, "Failed to fetch regions data for page 1"
    data = request.json()
    assert response_data == data
