import requests
import master_configuration_provider
import json
from datetime import date


def get_custom_token():
    print("Call for token")
    url = "https://localhost:7250/CustomToken/GetPython"
    response = requests.get(url, json={}, verify=False)
    print(response.text)
    print("call for token finished")
    return response.text

def get_access_token(custom_token):
    transfers_firebase_webapi_key=master_configuration_provider.get_master_configuration_value("TransfersFirebaseWebApiKey")
    print(transfers_firebase_webapi_key)
    url=f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={transfers_firebase_webapi_key}"
    body={'token':custom_token, 'returnSecureToken':True}
    response=requests.post(url,json=body,verify=False)
    js=json.loads(response.content)
    idToken=js["idToken"]
    return idToken

def get_id_token():
    custom_token = get_custom_token()
    idToken = get_access_token(custom_token)
    return idToken

def add_new_transfer_instance(date, category, name, value):
    id_token=get_id_token();
    url="https://localhost:7250/Transfer/Add"
    obj={'Date':date.strftime("%Y-%m-%dT00:00:00"), 'Category':category,'Name':name,'Value':value}
    headers={'Authorization':f'Bearer {id_token}', 'Content-Type': 'application/json'}
    response = requests.post(url, json=obj, headers=headers, verify=False)
    print(response.status_code)
    print(f'Request done')  # Press Ctrl+F8 to toggle the breakpoint.
    #2023-01-01T00:00:00

def get_last_transfer_istances():
    id_token=get_id_token()
    url = "https://localhost:7250/Transfer/List"
    obj = {'Name': 'Proxy'}
    headers = {'Authorization': f'Bearer {id_token}', 'Content-Type': 'application/json'}
    response = requests.post(url, json=obj, headers=headers, verify=False)
