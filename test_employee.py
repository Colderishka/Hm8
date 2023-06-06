import requests

BaseUrl = 'https://x-clients-be.onrender.com'

#[GET] /employee
def test_get_employee(): 

    resp = requests.get(BaseUrl + '/employee?company=6')
    resp_body = resp.json()
    first_employee = resp_body[0]
   
    assert first_employee["firstName"] == "Иван"
    assert resp.status_code == 200

#[POST] /employee
def test_create_employee():

    for_auth = {
        'username' : 'donatello',
        'password' : 'does-machines'
    }

    employee = {
        "companyId": 6,
        "firstName": "Виктор",
        "lastName": "Павлович",
        "middleName": "",
        "phone": "222231314",
        "url": ""
}

   #авторизация
    resp = requests.post(BaseUrl + '/auth/login', json=for_auth)
    token = resp.json()["userToken"]

    #создание работника
    my_headers = {}
    my_headers["x-client-token"] = token
    resp = requests.post(BaseUrl+'/employee?company=6', json=employee, headers=my_headers)

    assert resp.status_code == 201

#[GET] /employee/{id}
def test_get_employee_by_id():

    resp = requests.get(BaseUrl + '/employee/24')
    new_employee = resp.json()
   
    assert new_employee["firstName"] == "Виктор"    
    assert resp.status_code == 200

#[PATCH] /employee/{id}
def test_patch_employee():
    for_auth = {
        'username' : 'donatello',
        'password' : 'does-machines'
    }

    update_employee = {
        'companyId': 6,
        'firstName': 'Илон',
        'lastName': 'Корнеплод',
        'middleName': '',
        'phone': '88005553535',
        'url': ''
    }

   #авторизация
    resp = requests.post(BaseUrl + '/auth/login', json=for_auth)
    
    #изменение данных 
    token = resp.json()["userToken"]
    my_headers = {}
    my_headers["x-client-token"] = token
    resp = requests.patch(BaseUrl+'/employee/24', json=update_employee, headers=my_headers)
    
    assert resp.status_code == 200
