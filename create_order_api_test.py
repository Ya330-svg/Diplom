

import pytest
from sender_stand_request import create_order, get_order_by_track
from data import CREATE_ORDER_BODY


#Чижов Ян, 21-я когорта — Финальный проект. Инженер по тестированию плюс

# Тест на создание заказа и получение его по трекеру
def test_create_and_get_order():
    # Шаг 1: Создать заказ
    create_order_response = create_order(CREATE_ORDER_BODY)

    # Проверяем, что запрос создания заказа прошел успешно
    assert create_order_response.status_code == 201, f"Expected status code 201, but got {create_order_response.status_code}"

    # Шаг 2: Сохранить трекер заказа
    order_data = create_order_response.json()
    track = order_data.get("track")

    assert track is not None, "Track number was not returned in the response"

    # Шаг 3: Выполнить запрос на получение заказа по трекеру
    get_order_response = get_order_by_track(track)

    # Шаг 4: Проверить, что код ответа равен 200
    assert get_order_response.status_code == 200, f"Expected status code 200, but got {get_order_response.status_code}"
