import requests

'''def country_code_ru():  # №502.2 Сhecking the сoutru_code = ru Parameter.
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=ru'
    request = requests.get(url)
    if request.status_code == 100:
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


def country_code_kg():  # №502.3 Сhecking the сoutru_code = kg Parameter.
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=kg'
    request = requests.get(url)
    if request.status_code == 200:
        data = request.json()
        country_codes = [item['country']['code']
                         for item in data['items']]
        return country_codes
    else:
        # If the status code is != 200, display an error message
        print(f" Test №502.3 'Failed' status code != 200: Status code={request.status_code}")
        return None


result = country_code_kg()
if result is not None:
    count_ru = result.count('kg')
    if count_ru == len(result):
        print("Test №502.3 'Passed' all values in the list = 'kg'")
    else:
        print(f"Test №502.3 'Failed' not all values in the list = 'kg'\n{result}")


def country_code_kz():  # №502.4 Сhecking the сoutru_code = kg Parameter.
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=kz'
    request = requests.get(url)
    if request.status_code == 200:
        data = request.json()
        country_codes = [item['country']['code']
                         for item in data['items']]
        return country_codes
    else:
        # If the status code is != 200, display an error message
        print(f" Test №502.4 'Failed' status code != 200: Status code={request.status_code}")
        return None


result = country_code_kz()
if result is not None:
    count_ru = result.count('kz')
    if count_ru == len(result):
        print("Test №502.4 'Passed' all values in the list = 'kz'")
    else:
        print(f"Test №502.4 'Failed' not all values in the list = 'kz'\n{result}")'''


def test_country_code_ru():
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=ru'
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "No country codes returned"
    assert all(code == 'ru' for code in country_codes), f"Not all country codes are 'ru': {country_codes}"


def test_country_code_kg():
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=kg'
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "No country codes returned"
    assert all(code == 'kg' for code in country_codes), f"Not all country codes are 'kg': {country_codes}"


