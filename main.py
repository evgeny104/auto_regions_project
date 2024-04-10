import json
import requests


def test_total_count():     # Функция проверяет -строку- "total", общее количество регионов в базе 22
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
    assert (body["items"][0]["country"]["code"]) == "ru"


def test_contre_code_ru():     # Функция проверяет  Код страны для фильтрации "ru"
    res = requests.get('https://regions-test.2gis.com/1.0/regions?country_code=ru')
    body = json.loads(res.text)
    assert body["items"][0]["country"]["name"] == "Россия"
    assert body["items"][0]["country"]["code"] == "ru"


def test_contre_code_kg():     # Код страны для фильтрации "kg"
    res = requests.get('https://regions-test.2gis.com/1.0/regions?country_code=kg')
    body = json.loads(res.text)
    print(body)
    assert body["items"][0]["country"]["name"] == "Кыргызстан"
    assert body["items"][0]["country"]["code"] == "kg"


def test_contre_code_kz():     # Код страны для фильтрации "kz"
    res = requests.get('https://regions-test.2gis.com/1.0/regions?country_code=kz')
    body = json.loads(res.text)
    assert body["items"][3]["country"]["name"] == "Казахстан"
    assert body["items"][3]["country"]["code"] == "kz"


def test_contre_code_cz():     # Код страны для фильтрации "cz"
    res = requests.get('https://regions-test.2gis.com/1.0/regions?country_code=cz')
    body = json.loads(res.text)
    assert body["items"][0]["country"]["name"] == "Чехия"
    assert body["items"][0]["country"]["code"] == "cz"


def test_region_q_empty_param():      # проверяет status cod empty param
    res = requests.get('https://regions-test.2gis.com/1.0/regions?')
    assert res.status_code == 200


test_total_count()
test_region_q()
test_region_q_register()
test_region_q_allignore()

test_contre_code_ru()
test_contre_code_kg()
test_contre_code_kz()
test_contre_code_cz()
test_region_q_empty_param()

