users = ['Kamil', 'Anna01', 'piesek', 'DIDI']

user_name = input('jak masz na imię')
user = input('podaj nazwę użytkownika')

if user in users:
    if user_name[-1].lower()=='a':
        print('witam panią')
    else:
        print('witam pana')
else:
    users.append(user)
    print(f'witamy {user}')

