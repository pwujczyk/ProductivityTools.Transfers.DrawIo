import requests

def get_custom_token():
    print("Call for token")
    url = "https://localhost:7250/CustomToken/GetPython"
    response = requests.get(url, json={}, verify=False)
    print(response.text)
    print("call for token finished")
    return response.text

def get_access_token(custom_token):
    url="https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key=AIzaSyAr0HCAH_e80NeivpRm7PJls50O0sX2Y18"
    json={'token':custom_token, 'returnSecureToken':True}
    response=requests.post(url,json=json,verify=False)
    print(response)

def print_hi(name):
    url="https://localhost:7250/Transfer/Add"

    obj={'Date':'2023-01-01T00:00:00', 'Category':'car','Name':'fef','Value':33}
    response = requests.post(url, json=obj, verify=False)
    print(response.text)
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    custom_token=get_custom_token()
    get_access_token(custom_token)
