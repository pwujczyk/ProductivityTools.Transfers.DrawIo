import requests

def print_hi(name):
    url="https://localhost:7250/Transfer/Add"

    obj={'Date':'2023-01-01T00:00:00', 'Category':'car','Name':'fef','Value':33}
    response = requests.post(url, json=obj, verify=False)
    print(response.text)
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    print("Call for token")
    url = "https://localhost:7250/CustomToken/GetPython"
    response=requests.get(url,json={}, verify=False)
    print(response.text)
    print("call for token finished")