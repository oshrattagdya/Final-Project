import pytest
import requests


def test_api_addUsers():
    url = 'https://qa-api.trado.co.il/api/user/create'
    myobj = {"firstName":"sbh",
             "lastName":"ss",
             "email":"d@j.com",
             "phone":"1912222224",
             "storeIds":["4jp555dl46qzoyz"]
             }
    x = requests.post(url, json=myobj)
    print(x.text)
    assert x.status_code == 200


def test_api_updateUsers():
    url = 'https://qa-api.trado.co.il/api/user/update'
    myobj = {"firstName":"da",
             "lastName":"ss",
             "email":"d@j.com",
             "phone":"1912222226"
             }
    x = requests.post(url, json=myobj)
    print(x.text)
    assert x.status_code == 200