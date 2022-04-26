import requests


def crypto(val):
    response = requests.get('https://bitpay.com/api/rates')
    data = response.json()
    for index, value in enumerate(data):
        if data[index]["code"] == val:
            return str(data[index]["rate"])
