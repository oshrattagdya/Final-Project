import pytest
import requests


def test_api_addUsers():
    url = 'https://qa-api.trado.co.il/api/user/create'
    myobj = {"firstName":"sbchjh",
             "lastName":"ss",
             "email":"d@j.com",
             "phone":"1912222224",
             "storeIds":["4jp555dl46qzoyz"]
             }
    res = requests.post(url, json=myobj)
    status = res.json()
    assert res.status_code == 200


def test_api_addUsers_invalid_email():
    url = 'https://qa-api.trado.co.il/api/user/create'
    myobj = {"firstName":"sbchjh",
             "lastName":"avi",
             "email":"d@j",
             "phone":"1912222224",
             "storeIds":["4jp555dl46qzoyz"]
             }
    res = requests.post(url, json=myobj)
    status = res.json()
    print(status)
    x = status['message']
    assert x == "not unique"


def test_api_addUsers_invalid_storeID():
    url = 'https://qa-api.trado.co.il/api/user/create'
    myobj = {"firstName":"sbchjh",
             "lastName":"bs",
             "email":"d@jd.com",
             "phone":"1912222249",
             }
    res = requests.post(url, json=myobj)
    status = res.json()
    print(status)
    x = status['message']
    assert x == "not unique"



def test_api_updateUsers():
    url = 'https://qa-api.trado.co.il/api/user/update'
    myobj = {"firstName":"assad",
             "lastName":"ss",
             "email":"d@j.com",
             "phone":"1912222226"
             }
    x = requests.post(url, json=myobj)
    print(x.text)
    assert x.status_code == 200