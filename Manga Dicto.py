mangas = {'Dragon Ball Z':'Akira Toriyama', 'One Piece':'Eiichiro Oda', 'Naruto':'Masashi Kishimoto', 'Kingdom':'Yasuhisa Hara'}
# Keys are Manga's and the Value are their authors.

name = input("Enter Author's name: ")
print(name)

A = 'Akira Toriyama'

E = 'Echiiro Oda'

M = 'Masashi Kishimoto'

Y = 'Yasuhisa Hara'

if name.startswith('Akira') is not None:
    print('Dragon Ball Z, Akira Toriyama')
else:
    print('Please Start Over Again')

if name.startswith('E') is not None:
    print('One Piece, Eiichiro Oda')
else:
    print('Please Start Over Again')

if name.startswith('Masa') is not None:
    print('Naruto, Masashi Kishimoto')
else:
    print('Please Start Over Again')