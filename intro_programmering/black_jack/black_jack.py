import random
deck = {'Ess': 1, 'Två': 2, 'Tre': 3, 'Fyra': 4, 'Fem': 5, 'Sex': 6, 'Sju': 7, 'Åtta': 8, 'Nio': 9, 'Tio': 10, 'Knekt': 10, 'Drottning': 10, 'kung': 10}

player_cards = []

def get_random_item(dictionary):
    random_key, random_value = random.choice(list(dictionary.items()))
    return random_key, random_value

def hit_or_stand(a):
    if a == "hit":
        key, value = get_random_item(deck)
        str(key)
        player_cards.append(key)
        player_point += value
        return player_cards, player_point
        


i = 1

while i == 1:
    player_point = 0
    player_cards = []
    print("black jack!!!!")
    redo = input("Redo att börja?: y/n ")
    if redo == "y":
        key, value = get_random_item(deck)
        player_point += value
        player_cards.append(str(key))
        print(player_cards)
        key, value = get_random_item(deck)
        player_point += value
        print("dina point: ", player_point)
        hit_stand = str(input("hit eller stand?: "))
        hit_or_stand(hit_stand)

       
    else:
        print("Ok")