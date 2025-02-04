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

def hit():
        hand.append(deck.pop())
        if count_hand() > 21:
            who_won = "dealer"
            return who_won
        
def stand():


    while count_dealer() < 17:
            dealer_hand.append(deck.pop())

    if count_dealer() > 21:
        who_won = "player"
        return who_won

    if count_dealer() < count_hand():
        who_won = "player"
        return who_won
    else:
        who_won = "dealer"
        return who_won
                
def print_hand(han):
    return_hand = ""
    for w in han:
        for v in w:
            return_hand += v
            return_hand += " "
        return_hand += ", "
    return return_hand
    






#ongoing = str(input("Ready?: y/n: "))

#while ongoing.lower() == "y":


play = str(input("Spela en eller fler rundor blackjack?: y/n: "))

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
    dealer_hand = []

    first_deal()
    
    print(" ")

    print("Dealers Hand: ",print_hand(dealer_hand))
    print("Dealers Hand Value",count_dealer())

    print(" ")

    print("Your Hand: ",print_hand(hand))
    print("Your Hand Value: " ,count_hand())

    print(" ")


    first_stand = True

    while who_won != "player" or who_won != "dealer":


        if blackjack(count_hand()) == True:
            print("Player wins!!!!!")
            break
        elif blackjack(count_dealer()) == True:
            print("Dealer Wins :'(")
            break


        if first_stand == True:
            hors = str(input("Hit or Stand?: "))
            if hors.lower() == "hit" or hors.lower() == "h":
                who_won = hit()
            elif hors.lower() == "stand" or hors.lower() == "s":    
                who_won = stand()
                first_stand = False
        
        
        print(" ")

        print("Dealers Hand: ", print_hand(dealer_hand))
        print("Dealers Hand Value",count_dealer())

        print(" ")

        print("Your Hand: ",print_hand(hand))
        print("Your Hand Value: " ,count_hand())

        print(" ")



        if who_won == "player":
            print("player won!")
            break
        elif who_won == "dealer": 
            print("Dealer won!")
            break



    play = input("Spela igen?: y/n: ")
