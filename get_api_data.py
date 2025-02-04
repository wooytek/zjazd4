import requests
import json
import pandas as pd

response = requests.get("http://api.open-notify.org/astros")
# print(response.status_code)
# print(f'{response.json()}\n')
# data_astros = response.json()
#
# df_astros = pd.DataFrame(data_astros)
# print(f'{df_astros.to_string()}\n')
# print(df_astros[df_astros['craft'] == 'ISS'])
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


