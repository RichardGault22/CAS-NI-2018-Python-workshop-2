'''
This file will look at for loops
'''
password = 'safe'
password_missing = True
for attempt in range(5):
    login  = input('Please enter password: ')
    if login == password:
        password_missing = True
        break

if password_missing == True:
    print('Sorry, you are locked out!')
else:
    print('You are now logged in')
