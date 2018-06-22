'''
This file will look at (potentially) infinite while loops
'''
password = 'safe'
password_missing = True
while password_missing:
    login  = input('Please enter password:')
    if login == password:
        password_missing = False
print('You are now logged in')
