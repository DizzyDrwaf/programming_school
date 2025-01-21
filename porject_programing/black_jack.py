import random
colors = ['\u2660', '\u2661', '\u2662', '\u2663']
names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

play = str(input("Spela black jack?: y/n: "))

def count_hand():
        # Calculate the total value of the cards in hand
    total_value = 0
    ace_count = 0
    ace_value = 0

    for card in hand:
        card_name = card[0]  # Get the name of the card (e.g., '2', 'J', 'A')
        if card_name == 'A':
            ace_count += 1  # Count the Aces separately
        else:
            total_value += name_to_value[card_name]

    # Add Ace values optimally
    for te in range(ace_count):
        if total_value + 11 <= 21:
            ace_value += 11  # Use Ace as 11 if it doesn't exceed 21
        else:
            ace_value += 1  # Otherwise, use Ace as 1
    hand_value = total_value + ace_value
    return hand_value






while play.lower() == "y":

    name_to_value = {}

    value = 2

    for name in names:
        
        if name != 'J' and name != 'Q' and name != 'K' and name != 'A':
            name_to_value[name] = value
            value += 1
        elif name == 'A':
            shadow = 1
        else:
            name_to_value[name] = 10


    deck = []
    for color in colors:
        for value in names:
            deck.append([value, color])

    

    random.shuffle(deck)

    hand = []
    for i in range(5):
        hand.append(deck.pop())
    
    print(hand)
    print(count_hand())

    play = input("Spela igen?: y/n: ")
