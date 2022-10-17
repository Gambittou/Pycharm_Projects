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