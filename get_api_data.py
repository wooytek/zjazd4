import requests
import json
import pandas as pd

response = requests.get("http://api.open-notify.org/astros").text
print(response)
data_text = str(response).splitlines()[-1].split(",")
text = data_text[5].split(':')
print(data_text[5])
print(text[1])


