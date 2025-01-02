# my_dict = {'name': 'Misia', 'age':4.5, 'weight': 10.5}
# print(my_dict['age'])
# my_dict['weight']+=2
# print(my_dict['weight'])

#===========================================
# shopping_list={}
# while True:
#     check='t'
#     item=input('dodaj produkt do listy: ')
#     if item in shopping_list.keys():
#         check = input('produkt już dodany do listy. czy zaktualizować ilość t/n')
#     item_quantity=input('dodaj ilość tego produktu : ')
#     if check =='t':
#         shopping_list[item] = item_quantity
#     if input('czy dodać kolejny produkt: t/n: ') == 'n':
#         break
# print(shopping_list)
# print(shopping_list.items())
# print(shopping_list.keys())
# print(shopping_list.values())

#===========================================

# suma = zbior1 | zbior2
# przeciecie = zbior1 & zbior2
# roznica = zbior1 - zbior2
# roznica_symetryczna = zbior1 ^ zbior2

# NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
# chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
# chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
# krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
# centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
# zbior_pusty = set()
# chorzy_krzyki = krzyki & chorzy_rok
# chorzy_centrum_miesiac = centrum & chorzy_miesiac
# print(chorzy_krzyki)
# print(chorzy_centrum_miesiac)
# print(f'w krzykach i centrum mieszka {krzyki | centrum}')
# print(f'w obu miejscach {krzyki & centrum}')
# print(f'mieszkańcy centrum krzyków i nie w obu miejscach jednocześnie {(krzyki | centrum) - (krzyki & centrum)}')
# print(f'\nmieszkańcy centrum krzyków i nie w obu miejscach jednocześnie {(krzyki) - (krzyki & centrum)}')

#===========================================
# NFZ = NFZ | (centrum | krzyki)
# print(f'\n {NFZ}')
#
# women=set()
# men=set()
# for pesel in NFZ:
#     if pesel%2==0:
#         women.add(pesel)
#     else:
#         men.add(pesel)
# print(f'to jest {men}')

#===========================================

# users = {'Kamil': '123', 'Mario':'M11'}
# special_char = {'/ ! @ \\_'}
#
# login = input('Podaj login:  ')
# passwd = input('Podaj hasło:   ')
# if login in users.keys():
#     if passwd == users[login]:
#         print('Zalogowany')
#     else:
#         exit()
# else:
#     print(f'rejestracja {login}')
#     if len(special_char & set(passwd)):
#         users[login] = passwd
#     else: passwd = input('podaj jeszcze raz hasło')

#===========================================

# class Auto:
#
#     def __init__(self, color, year):
#         self.color = color
#         self.condition = 5
#         self.age=2024-year
#
#     def change_mileage(self,km):
#         if km >= 0:
#             self.mileage += km
#         else:
#             passwd = input('podaj haslo serwisowe: ')
#             if passwd =='1234':
#                 print('zaraportowano')
#                 self.mileage += km
#
# auto11 = Auto('red',5)
# print(auto11.age)

#===========================================

# def mnozenie(a,b):
#     result = a * b
#     return result
# print(mnozenie(4,3))
#
# def insurance(age,bmi,smoking):
#     total = 100
#     total += age * 1.3
#     if bmi >30:
#         total +=bmi * .9
#     if smoking == 't':
#         total += 2
#     return total
# print(insurance(40,35,'t'))

#===========================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime as dt

df = pd.read_csv(r'otodom.csv')
# print(df)
# print(df.head(3))
# print(df.describe().T.to_string())
# print(df.iloc[0:,1:7])
# print(df.iloc[0:,1:7].corr())

# sns.heatmap(df.iloc[:,1:].corr(),annot=True)

# def fileName():
#     now = dt.datetime.now()
#     return now.strftime('mojplik%H%M%S')
#
# # plt.hist(df.price, bins=30)
# # plt.show()
#
# sns.histplot(df.price,bins=50)
# # sns.histplot(df.price)
# plt.savefig(r'charts\wykres'+fileName()+'.png')
# plt.show()

q1 = df.describe().T.loc['price', '25%']
q3 = df.describe().T.loc['price', '75%']
# print(q1)
# print(q3)

df1 = df[df.price <= q3]
sns.histplot(df1.price)
plt.show()

X = df1.iloc[:,2:]
y = df1.price
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = LinearRegression()
model.fit(X_train,y_train)
print(f'\n\n{model.score(X_test, y_test)}\n\n')
print(pd.DataFrame(model.coef_, X.columns))


