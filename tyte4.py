class Arsenal:
    def __init__(self):
        self.name = 'katana'
        self.element = 'dark'
        self.spiritlevel = 'lvl55'

my_arsenal = Arsenal()
my_arsenal.spiritlevel = 'lvl55'
my_arsenal.element = 'dark'

print(f'this spirit is strong')
print(my_arsenal.element)
print(my_arsenal.name)