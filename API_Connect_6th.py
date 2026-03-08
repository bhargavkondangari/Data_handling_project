import requests
from requests.auth import HTTPBasicAuth

url = "https://100.98.179.61/redfish/v1/"

response = requests.get(url=url,auth=HTTPBasicAuth(username="root",password="calvin"),verify= False)

if response.status_code == 200:
    print("connection establish")

print(dir(requests))

