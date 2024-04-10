import requests


def country_code_ru():
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=ru'
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    li = [item['country']['code']
          for item in data['items']]
    assert li.count('ru') == len(li)
    print("pass")


# run check functions country_code_ru():
country_code_ru()


def country_code_kg():
    url = 'https://regions-test.2gis.com/1.0/regions?country_code=kg'
    request = requests.get(url)
    if request.status_code == 200:
        data = request.json()
        country_codes = [item['country']['code']
                         for item in data['items']]
        return country_codes
    else:
        # If the status code is != 200, display an error message
        print(f"Error while receiving data. Status code: {request.status_code}")
        return None


result = country_code_kg()
count_ru = result.count('kg')

if count_ru == len(result):
    print("All values in the list = 'kg'")
else:
    print(f"{result}\nNot all values in the list = 'kg'")

# run check functions country_code_kg():
country_code_kg()


def country_code_ru():  # №502.2 Сhecking the сoutru_code = ru Parameter.
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
