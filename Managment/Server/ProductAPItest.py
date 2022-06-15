import pytest
import requests


def test_api_upload_prodact_correctly():
    url = "https://qa-api.trado.co.il/api/product/create"
    myobj = {"barcode":"testagin",
             "name":"",
             "price":"45",
             "expirationDate":"",
             "sectionId":"4jp555dl4dvbcra",
             "departmentId":"u6z3r6pokm0lra0r",
             "storeId":"4jp555dl4e4w4q7",
             "units":{"unitsInCarton":"","amount":"0"},
             "deliveryOrderPlace":{"city":"","street":"","number":"-3"},
             "fields":{}}
    x = requests.post(url, json=myobj)
    print(x.status_code)
    assert x.status_code == 200