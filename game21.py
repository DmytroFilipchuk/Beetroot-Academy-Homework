import random

def get_deck():
    suits = ("♠","♥","♦","♣")
    cards = ("6","7","8","9","10","Jack","Queen","King","Ace")
    weight = (6,7,8,9,10,3,4,5,11)
    deck = []
    for suit in suits:
        for idx,title in enumerate(cards):
            card_weight = weight[idx]
            deck.append(
                (card_weight,suit,title)
            )
    return deck

def want_play():
    while True:
        user_input = input("Do you want to play? Type 'Yes' or 'No' ")
        if user_input.lower() == "yes":
            return True
        elif user_input.lower() == "no":
            exit()
        else:
            pass

def calculate_player_cards(cards):
    total = 0
    for card in cards:
        total += card[0]
    return total

def display_user_cards(cards):
    print("\nYour cards:\n")
    for card in cards:
        print(f"Suit: {card[1]}\nCard: {card[2]}\n")
    print(f"Sum: {calculate_player_cards(cards)}\n")

#def get_two():
   # for _ in range(2):
     #  deck.pop()

def one_more_card():
    while True:
        user_input = input("One more card? Press enter to continue, or type 'no'\n ")
        if user_input.lower() == "":
            return True
        elif user_input.lower() == "no":
            return False
        else:
            pass

def player_game():
    while calculate_player_cards(player) <= 21:
        if one_more_card():
            player.append(deck.pop())
            display_user_cards(player)
        else:
            break
counter_player = 0
counter_computer = 0
def game_end():
    global counter_player, counter_computer
    if calculate_player_cards(player) > 21:
        print("Loser!")
        counter_computer += 1
    else:
        while calculate_player_cards(computer) < random.randint(14, 17):
            computer.append(deck.pop())

        if calculate_player_cards(computer) > 21 or calculate_player_cards(computer) < calculate_player_cards(player):
            print("Congrats, you win!")
            counter_player += 1
        else:
            print("Loser!")
            counter_computer +=1


    print(f"Computer: {calculate_player_cards(computer)}")

while want_play():
    deck = get_deck()
    random.shuffle(deck)
    player = [deck.pop(), deck.pop()]
    computer = [deck.pop(), deck.pop()]
    display_user_cards(player)
    player_game()
    game_end()
    print(f"\nPlayer: {counter_player}\nComputer: {counter_computer}")
else:
    exit()
