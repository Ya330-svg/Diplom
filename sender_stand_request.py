import requests
# Теперь импортируем переменные из Configuration
from Config import BASE_URL, CREATE_ORDER_ENDPOINT, GET_ORDER_BY_TRACK_ENDPOINT

# Функция для создания заказа
def create_order(data):
    url = BASE_URL + CREATE_ORDER_ENDPOINT
    response = requests.post(url, json=data)
    return response

# Функция для получения заказа по трекеру
def get_order_by_track(track):
    url = BASE_URL + GET_ORDER_BY_TRACK_ENDPOINT + str(track)
    response = requests.get(url)
    return response


