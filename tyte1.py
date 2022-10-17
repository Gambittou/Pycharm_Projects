name = 'Gambit'
age = 23

def gambit():
    print('This is the function, now die')

def greeting():
    print(f'My name is {name} and i am {age} years old')
    bye()

def bye():
    print(f'good bye {name}, have a bad day')
    gambit()

print('This is outside function')

print(50 * '-')

greeting()