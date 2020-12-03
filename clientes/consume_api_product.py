import requests

url = "http://challenge-api.luizalabs.com/api/product/?page=1"
response = requests.get(url)

if (response.status_code == 200):
    print('Json', response.json())
else:
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    print('Text', response.text)
