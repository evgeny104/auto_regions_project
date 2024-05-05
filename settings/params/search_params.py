# page_size.py

import pytest


def process_page_size(page_size):
    """
    Обрабатывает параметр page_size для указания количества элементов на странице.
    """
    if page_size is None:
        return None
    # Проверяем, что page_size больше 0
    if page_size <= 0:
        raise ValueError("Page size must be greater than 0.")
    return page_size


@pytest.mark.parametrize("page_size, expected", [
    (10, 10),
    (20, 20),
    (-1, ValueError),
    (0, ValueError),
    (None, None)
])
def test_process_page_size(page_size, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            process_page_size(page_size)
    else:
        assert process_page_size(page_size) == expected
