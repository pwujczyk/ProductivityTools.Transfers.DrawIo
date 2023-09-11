import requests

def print_hi(name):
    response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
