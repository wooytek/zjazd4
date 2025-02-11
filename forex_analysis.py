import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
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
# print(data2)

for i in range(100):
    content[i] = content[i].split(';')
    data1.append(content[i])
    date.append(content[i])
# final_data.insert(0,'date',date,True)
final_data = pd.DataFrame(data1)
final_data.rename(columns={0:'date', 1:'hours', 2:'minutes', 3:'open', 4:'high', 5:'low', 6:'close'}, inplace=True)
fd1 = final_data[['open', 'high', 'low', 'close']].replace(r',','.', regex=True)
fd1=fd1.replace(r'\n','0', regex=True)
# print(final_data.columns)
fd1=fd1.drop(0)
print(fd1)
print(float(fd1['close'][1]))
# print(float(fd1[2])*2)
# model=LinearRegression()
# model.fit()