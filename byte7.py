gambit = {'name' : 'Gambit, 'cards_missing}
print(gambit)

gambit['location'] = 'unknown'
gambit['no_cards'] = 12
gambit['Bounty'] = -1116

print(gambit)

if 'Location' in gambit:
    print(gambit['Location'])
else:
    print('gambit's location Is unknown')
