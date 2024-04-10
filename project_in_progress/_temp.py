import requests
from json_object import error_country_code

'''def country_code_kg():  # №502.3 Сhecking the сoutru_code = kg Parameter.
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
        
 def test_country_code_kg():     # № Test 502,3
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=kg'
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    country_codes = [item['country']['code'] for item in data['items']]
    assert country_codes, "No country codes returned"
    assert all(code == 'kg' for code in country_codes), f"Not all country codes are 'kg': {country_codes}"


def test_country_code_test():       # №502,6
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=test'
    request = requests.get(url)
    if request.status_code == 200:
        data = request.json()
        return data


result = test_country_code_test()
if error_country_code['error']['message'] == result['error']['message']:
    print("passed")
else:
    print("Failed")


def test_country_code_test():  # № Test 502,6
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=test'
    request = requests.get(url)
    assert request.status_code == 200
    data = request.json()
    assert data, "No country codes returned"
    assert error_country_code['error']['message'] == data['error']['message']'''
