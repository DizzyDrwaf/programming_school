import random
colors = ['\u2660', '\u2661', '\u2662', '\u2663']
names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

play = str(input("Spela black jack?: y/n: "))

while play.lower == "y" or "yes" or "ja" or "j":

    name_to_value = {}

    value = 2

    for name in names:
        name_to_value[name] = value
        value += 1

    deck = []
    for color in colors:
        for value in names:
            deck.append([value, color])

    random.shuffle(deck)

    hand = []
    for i in range(5):
        hand.append(deck.pop())
    

    play = input("Spela igen?: y/n: ")
