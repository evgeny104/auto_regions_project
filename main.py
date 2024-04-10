import json
import requests
from json_object import error_country_code

'''def test_total_count():     # Функция проверяет -строку- "total", общее количество регионов в базе 22
    res = requests.get('https://regions-test.2gis.com/1.0/regions?page_size=5')
    body = json.loads(res.text)
    assert body["total"] == 22


def test_region_q():        # Функция проверяет поиск по наванию региона "Минимум -3 символа"
    res = requests.get('https://regions-test.2gis.com/1.0/regions?q=тау')
    body = json.loads(res.text)
    assert (body["items"][0]["name"]) == "Актау"


def test_region_q_register():        # Функция проверяет поиск по названию региона "Регистр не имеет значения"
    res = requests.get('https://regions-test.2gis.com/1.0/regions?q=СквА')
    body = json.loads(res.text)
    assert (body["items"][0]["name"]) == "Москва"


def test_region_q_allignore():      # Функция проверяет поиск по названию региона "все остальные параметры игнорируются"
    res = requests.get('https://regions-test.2gis.com/1.0/regions?q=УфА&country_code=cz&page=1&page_size=15')
    body = json.loads(res.text)
    assert (body["total"]) == 22
    assert (body["items"][0]["id"]) == 17
    assert (body["items"][0]["name"]) == "Уфа"
    assert (body["items"][0]["code"]) == "ufa"
    assert (body["items"][0]["country"]["name"]) == "Россия"
    assert (body["items"][0]["country"]["code"]) == "ru"'''


def test_country_code_ru():  # № Test 502,2
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=ru'
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'ru' for code in country_codes), f"Not all country codes are 'ru': {country_codes}"


def test_country_code_kg():  # № Test 502,3
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=kg'
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'kg' for code in country_codes), f"Not all country codes are 'kg': {country_codes}"


def test_country_code_kz():  # № Test 502,4
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=kz'
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'kz' for code in country_codes), f"Not all country codes are 'kz': {country_codes}"


def test_country_code_cz():  # № Test 502,5
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=cz'
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "list of country codes, not empty"
    assert all(code == 'cz' for code in country_codes), f"Not all country codes are 'cz': {country_codes}"


def test_country_code_test():  # № Test 502,6
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=test'
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    assert data, "list of country codes, not empty"
    assert error_country_code['error']['message'] == data['error']['message']
