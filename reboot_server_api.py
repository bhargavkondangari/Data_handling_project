import json
from wsgiref.headers import Headers

import requests
from requests.auth import HTTPBasicAuth
#print(dir(requests))

#url : http : //100.98.179.61/redfish
#403 error occurs : server succesfully received the request and understood the request but refuses to authorize it due to access restrications
#no valid cred : 401 error Unauthorized error
payload = {}

res = requests.post('https://100.98.179.61/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.GetRemoteServicesAPIStatus',json = payload, auth = HTTPBasicAuth('root','calvin'), verify = False)
##print(res.status_code)
##print(res.text)

if requests.status_codes == 200:
    print(res.text)
    print(type(res.text))
    print(res.json())

payload_reboot = {"ResetType": "ForceOff"}

res_2 = requests.post(url='https://100.98.179.61/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset',json=payload_reboot, auth = HTTPBasicAuth('root','calvin'), verify = False)
if res_2.status_code == 204:
    text_words =res_2.text
    print(type(text_words))




