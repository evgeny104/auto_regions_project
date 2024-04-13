import requests
from config import error_country_code, base_url


def test_country_code_page():  # № Test №502,1 for Pytest
    url = f"{base_url}/1.0/regions"
    server_request = requests.get(url)
    assert server_request.status_code == 200, "Failed to fetch regions data"
    response_data = server_request.json()
    urlpage = f"{base_url}/1.0/regions?page=1"
    request = requests.get(urlpage)
    assert request.status_code == 200, "Failed to fetch regions data for page 1"
    data = request.json()
    assert response_data == data


def test_country_code_ru():  # № Test 502,2
    url = f"{base_url}/1.0/regions?country_code=ru"
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'ru' for code in country_codes), f"Not all country codes are 'ru': {country_codes}"


def test_country_code_kg():  # № Test 502,3
    url = f"{base_url}/1.0/regions?country_code=kg"
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'kg' for code in country_codes), f"Not all country codes are 'kg': {country_codes}"


def test_country_code_kz():  # № Test 502,4
    url = f"{base_url}/1.0/regions?country_code=kz"
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'kz' for code in country_codes), f"Not all country codes are 'kz': {country_codes}"


def test_country_code_cz():  # № Test 502,5
    url = f"{base_url}/1.0/regions?country_code=cz"
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'cz' for code in country_codes), f"Not all country codes are 'cz': {country_codes}"


def test_country_code_test():  # № Test 502,6
    url = f"{base_url}/1.0/regions?country_code=test"
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    assert data, "list of country codes, not empty"
    assert error_country_code['error']['message'] == data['error']['message']
