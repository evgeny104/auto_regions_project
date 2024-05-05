import requests
import json


def check_status_code(response):
    assert response.status_code == 200, \
        "Error: status_code != 200"


def get_response(url):
    try:
        response = requests.get(url)  # Получаем ответ по указанному URL
        parsed_json = response.json()  # Парсим JSON-ответ
        return response, parsed_json  # Возвращаем распарсенный JSON
    except json.decoder.JSONDecodeError:
        assert False, "Error: Response is not in JSON format"
