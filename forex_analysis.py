import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import regression

sns.set()
path = "EURUSD5test.csv"
mode = "r"

# plt.style.use('seaborn-whitegrid')
data = pd.read_csv("EURUSD5test.csv")
final_data = pd.DataFrame(data)

with open(path, mode) as file1:
    content = file1.readlines()
data1=[]
data2=['date', 'hours', 'minutes', 'open', 'high', 'low', 'close']
date=[]
print(data2)

for i in range(50):
    content[i] = content[i].split(';')
    data1.append(content[i])
    date.append(content[i][0])
# final_data.insert(0,'date',date,True)
final_data = pd.DataFrame(data1)
print(final_data)
# print(final_data['date'])
print(data1[2][2])
