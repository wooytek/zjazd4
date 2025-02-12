import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import regression
import statistics
from sklearn.model_selection import train_test_split

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
fd_numeric=fd1[['open','high', 'low', 'close']].astype(float)
# print('poniżej dane')
# print(fd_numeric['close'][2]*2)
# fd1 = pd.get_dummies(fd1)
# print(statistics.mean([float(fd1['close'][2]),float(fd1['close'][3])]))
print(fd1['close'][1])
print(fd_numeric)
# print(float(fd1[2])*2)
model1=LinearRegression()
model1.fit(fd_numeric[['open','high','low']], fd_numeric['close'])
print(f'Wspolczynnik kierunkowy: {model1.coef_}')
print(f'Wspolczynnik kierunkowy1: {model1.coef_[1]}')
print(f'Wyraz wolny: {model1.intercept_}')
open=1.20945
high=1.20974
low=1.20943
close=model1.coef_[0]*open+model1.coef_[1]*high+model1.coef_[2]*low+model1.intercept_
print(close)


X=fd_numeric.iloc[:,2:5]
y=fd_numeric['close']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

model2=LinearRegression()
model2.fit(X_train,y_train)
print(f'\n\n{model2.score(X_test, y_test)}\n\n')
print(pd.DataFrame(model2.coef_, X.columns))

fd_numeric['change'] = 0
for i in range(len(fd_numeric['change'])-1):
    i+=1
    if fd_numeric.loc[i,'close']<fd_numeric.loc[i+1,'close']:
        fd_numeric.loc[i,'change']=1
print(fd_numeric)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
# fd_numeric = fd_numeric.astype(float)
X1 = fd_numeric.iloc[:,:-1]
y1 = fd_numeric.change
X_train1,X_test1,y_train1,  y_test1 = train_test_split(X1,y1,test_size=0.2)
model2=LogisticRegression()
# print(type(fd_numeric.change[2]))
# print(len(y_train1))
model2.fit(X_train1,y_train1)
print(model2.score(X_test1,y_test1))
print(pd.DataFrame(confusion_matrix(y_test1, model2.predict((X_test1)))))
