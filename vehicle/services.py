import requests
from rest_framework import status


def convert_currencies(rub_price):
    url = 'https://api.currencyapi.com/v3/latest?apikey=cur_live_2DVdK18vwNvpVPygJvZFJsyLwcwwiI7aaM3F2U9o&currencies=RUB'
    response = requests.get(url)
    if response.status_code == status.HTTP_200_OK:
        data = response.json().get('data')
        usd_rate = data['RUB']['value']
        usd_price = rub_price / usd_rate

    return usd_price