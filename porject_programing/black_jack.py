import random 

spela = str(input("Vill du köra en runda av black jack?: y/n "))

if spela.lower == "y" or "yes" or "ja":
    i = 1
else:
    i = 0




deck = []
my_strings = {1: "Ace", 2: "2", 3: "kung"}
for i in range(1, 4):
    deck.append({"rank": 1, "suit": "hearts", "string": my_strings[i]+" hearts"})

print(deck)

ett_kort = deck.pop()
print(ett_kort["string"])
    