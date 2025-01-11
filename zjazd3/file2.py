# zmienna = 'Piesek'
# print(type(zmienna))
#
# class Dog:
#     def __init__(self,weight):
#         self.weight = 15
#
# class Cat:
#     def __init__(self, weight):
#         self.weight = 9
#
# cat1 = Cat(25)
# dog1 = Dog(35)
# print(dog1 and cat1)
from sklearn.metrics import balanced_accuracy_score


class BankAccount:
    def __init__(self,owner,balance=0):
        self.balance = balance
        self.owner = owner

    def __str__(self):
        return f'konto należy do{self.owner} i jest na nim {self.balance} zł'

    def deposit(self,amount):
        self.balance +=amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('możesz wypłacić tylko')

    def display(self):
        print(f'twój balans to: {self.balance}')

account1 = BankAccount('Wojtek', 500)
account1.deposit(500)
print(account1.balance)