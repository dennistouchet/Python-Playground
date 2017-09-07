while True:
    print('Enter your age: ', end='')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password\n(letters and numbers only)')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers')

print('You password is:' + password, end='')
if int(age) > 40:
    print('. You old coot!')
elif int(age) < 18:
    print('. You baby!')
