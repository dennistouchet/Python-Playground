print('hello, world!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('You name is ', end='')
if len(myName) == 1:
   print(str(len(myName)) + ' character long!')
else:
   print(str(len(myName)) + ' characters long!')

