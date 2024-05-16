import requests
import json


def check_status_code(response):
    assert response.status_code == 200, \
        "Error: status_code != 200"


def get_response(url):
    try:
        response = requests.get(url)
        parsed_json = response.json()
        return response, parsed_json
    except json.decoder.JSONDecodeError:
        assert False, "Error: Response is not in JSON format"


