gambit = {"name" : "Gambit", "no_cards" : 1, "card_missing" : True, "location" : "Tartarus", "Bounty" : -1.025}

print(type(gambit))
print(gambit)

kaido = {"name" : "Kaido", "card_missing" : False}
print(kaido)

kaido["location"] = "unknown"
kaido["no_cards"] = 16
kaido["Bounty"] = 98.27

print(kaido)


if "location" in gambit:
 print(gambit["location"])
else:
    print("gambit does not have a location")


print("iterating through all the cards: ")

for card in kaido.cards():
    value = kaido[card]
    print(card, "=", value)