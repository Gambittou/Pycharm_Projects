names = 0

print(f'type the names of 5 people one at a time')

while names < 5:
    print('type the name of person number ' , names + 1)
    named_p = input()
    print(named_p, 'is awesome!')
    names += 1

text = 'Welcome Gambit'
print(text.count('o'))

if text.startswith('Welc'):
    print('Gambit has appeared!!!')

else:
    print("looks like a god")

    if text.isalpha():
        print('string is all alpha')
        
        text = ' \t\r\n'
        if text.isspace():
            print('string is whitespace')