import requests
import json
import pandas as pd

api_url = 'http://apilayer.net/api/live'
api_key = '97c2b94caefe3f41f1e216cb59e66baf'

headers = {
    'access_key' : '97c2b94caefe3f41f1e216cb59e66baf'

}
response = requests.get(api_url, headers=headers)
print("hello")

if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print(response.status_code)