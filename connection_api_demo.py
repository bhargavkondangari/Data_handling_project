import requests
from requests.auth import HTTPBasicAuth
#print(dir(requests))

#url : http : //100.98.179.61/redfish
#403 error occurs : server successfully received the request and understood the request but refuses to authorize it due to access restrications
#no valid cred : 401 error Unauthorized error
res = requests.get('https://100.98.179.61/redfish/v1',auth=HTTPBasicAuth('root','calvin'), verify = False)
print(res.status_code)
if res.status_code ==200:
   # print(res.json)
    text = res.text
    print(type(res.text))
#{"UpdateService":{"@odata.id":"/redfish/v1/UpdateService"},"Managers":{"@odata.id":"/redfish/v1/Managers"},"CertificateService":{"@odata.id":"/redfish/v1/CertificateService"},"SessionService":{"@odata.id":"/redfish/v1/SessionService"},"JobService":{"@odata.id":"/redfish/v1/JobService"},"Vendor":"Dell","Fabrics":{"@odata.id":"/redfish/v1/Fabrics"},"JsonSchemas":{"@odata.id":"/redfish/v1/JsonSchemas"},"Links":{"Sessions":{"@odata.id":"/redfish/v1/SessionService/Sessions"}},"@odata.id":"/redfish/v1","Registries":{"@odata.id":"/redfish/v1/Registries"},"ServiceIdentification":"PNT3003","Tasks":{"@odata.id":"/redfish/v1/TaskService"},"TelemetryService":{"@odata.id":"/redfish/v1/TelemetryService"},"Description":"Root Service","LicenseService":{"@odata.id":"/redfish/v1/LicenseService"},"Systems":{"@odata.id":"/redfish/v1/Systems"},"Name":"Root Service","UUID":"3330304f-c0d0-3380-5410-004e4c4c4544","EventService":{"@odata.id":"/redfish/v1/EventService"},"AccountService":{"@odata.id":"/redfish/v1/AccountService"},"Oem":{"Dell":{"IsBranded":0,"ManagerMACAddress":"6c:3c:8c:96:6e:96","ServiceTag":"PNT3003","@odata.context":"/redfish/v1/$metadata#DellServiceRoot.DellServiceRoot","@odata.type":"#DellServiceRoot.v1_0_0.DellServiceRoot"}},"Product":"Integrated Dell Remote Access Controller","@odata.etag":"W/\"gen-6\"","ProtocolFeaturesSupported":{"DeepOperations":{"DeepPATCH":false,"DeepPOST":false},"ExcerptQuery":false,"ExpandQuery":{"Levels":true,"Links":true,"MaxLevels":1,"NoLinks":true,"ExpandAll":true},"FilterQuery":true,"OnlyMemberQuery":true,"SelectQuery":true},"Id":"RootService","@odata.type":"#ServiceRoot.v1_19_0.ServiceRoot","RedfishVersion":"1.22.1","ComponentIntegrity":{"@odata.id":"/redfish/v1/ComponentIntegrity"},"@odata.context":"/redfish/v1/$metadata#ServiceRoot.ServiceRoot","Chassis":{"@odata.id":"/redfish/v1/Chassis"}}
    res = text.split(" ")
    