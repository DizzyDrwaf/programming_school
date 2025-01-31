import random
colors = ['\u2660', '\u2661', '\u2662', '\u2663']
names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

player_win = False
dealer_win = False
who_won = ""
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

def count_dealer():
        # Calculate the total value of the cards in hand
    total_value = 0
    ace_count = 0
    ace_value = 0

    for card in dealer_hand:
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
    dealer_value = total_value + ace_value
    return dealer_value

def first_deal():
    for i in range(2):
        hand.append(deck.pop())
    dealer_hand.append(deck.pop())

def blackjack(score):

    if score == 21:
        game_over = True
    else:
        game_over = False
    
    return game_over 

def hit_or_stand(player_picked):
    
    if player_picked.lower() == "hit":
        hand.append(deck.pop())
        if count_dealer() < 16:
            dealer_hand.append(deck.pop())
    elif player_picked.lower() == "stand":
        if count_dealer() < 16:
            dealer_hand.append(deck.pop())
        else:
            if count_dealer() < count_hand():
                player_win = True
                dealer_win = False
            else:
                player_win = False
                dealer_win = True
                
                if player_win == True:
                    who_won = "player"
                elif dealer_win == True:
                    who_won = "dealer"

                return who_won
    






#ongoing = str(input("Ready?: y/n: "))

#while ongoing.lower() == "y":


play = "y"

while play.lower() == "y":

    play = str(input("Spela en runda blackjack?: y/n: "))
    
    if play.lower() != "y":
        break

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
    dealer_hand = []

    first_deal()
        
    print(" ")

    print("Dealers Hand: ",dealer_hand)
    print("Dealers Hand Value",count_dealer())

    print(" ")

    print("Your Hand: ",hand)
    print("Your Hand Value: " ,count_hand())

    print(" ")

    if blackjack(count_hand()) == True:
        print("Player wins!!!!!")
        continue
    elif blackjack(count_dealer()) == True:
        print("Dealer Wins :'(")
        continue

    hit_or_stand(input("Hit or Stand?: "))

    if who_won == "player":
        print("WOW")
        break
    elif who_won == "dealer": 
        print("SAD")
        break



    play = input("Spela igen?: y/n: ")
