import requests
import json

base_url = "https://regions-test.2gis.com/1.0/regions?"


def get_response(url):
    try:
        response = requests.get(url)                                            # Получаем ответ по указанному URL
        response.raise_for_status(),                                            # Проверяем успешность запроса
        parsed_json = response.json()                                           # Парсим JSON-ответ
        return parsed_json                                                      # Возвращаем распарсенный JSON
    except json.decoder.JSONDecodeError:
        assert False, "Error: Response is not in JSON format"
