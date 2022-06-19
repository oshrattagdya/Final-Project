import pytest
import requests
from ..DB.BaseMongoDB2 import MongoDB
db = MongoDB("trado_qa", "products")

class TestProductAPI():

    def test_api_create_prodact_correctly(self):
        url = "https://qa-api.trado.co.il/api/product/create"

        myobj = {"barcode":"001995","name":"air-pods","price":500,
          "active":True,"expirationDate":"2022-06-22",
          "description":"change desc","priority":2,"sectionId":"u6z3rgrckkzoqiay",
          "departmentId":"xfdpjewkz59964t","storeId":"2p8ys40kl0eyvk1m","parallelImporter":'true',
          "units":{"unitsInCarton":"1","amount":"100","minimumOrderCartonsCount":"1"},
          "deliveryOrderPlace":{"city":"eilt","street":"sumsum","number":"2"},
          "contactInfo":{"contactNumber":"0556622111"},"fields":{}}

        response = requests.post(url, json=myobj)
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 20
        result = response.json()

        """assert with DB"""
        product_in_db = db.find({"name":"air-pods"})
        db_result = product_in_db["price"]
        myobj_result = myobj["price"]
        assert myobj_result == db_result




    def test_api_create_prodact_incorrectly_when_prodact_name_null(self):
        url = "https://qa-api.trado.co.il/api/product/create"

        myobj = {"barcode":"001927","price":500,
          "active":True,"expirationDate":"2022-06-22",
          "description":"change desc","priority":2,"sectionId":"u6z3rgrckkzoqiay",
          "departmentId":"xfdpjewkz59964t","storeId":"2p8ys40kl0eyvk1m","parallelImporter":'true',
          "units":{"unitsInCarton":"1","amount":"100","minimumOrderCartonsCount":"1"},
          "deliveryOrderPlace":{"city":"eilt","street":"sumsum","number":"2"},
          "contactInfo":{"contactNumber":"0556622111"},"fields":{}}

        response = requests.post(url, json=myobj)
        result = response.json()
        print(result)
        """assert with DB"""
        product_in_db = db.find({"barcode":"001927"})
        expected_result = None

        assert expected_result == product_in_db






    def test_api_update_prodact_correctly(self):
        status = True
        url = "https://qa-api.trado.co.il/api/product/update"
        myobj = {"barcode":"001994",
                 "name":"Charger",
                 "price":555,
                 "active":status,
                 "expirationDate":"2022-06-22T00:00:00.000Z",
                 "description":"52 inches",
                 "priority":1,"parallelImporter":False,
                 "units":{"unitsInCarton":"100","amount":"20","minimumOrderCartonsCount":"10"},
                 "deliveryOrderPlace":{"city":"lod","street":"tech","number":"100"},
                 "contactInfo":{"contactNumber":"0542259745"},
                 "id":"4jp555dl4kbaw8h","fields":{}
                 }

        response = requests.post(url, json=myobj)
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 20
        result = response.json()

        """assert with DB"""
        product_in_db = db.find({"name": "Charger"})
        db_result = product_in_db["active"]

        assert db_result == status





