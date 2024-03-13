# Day 11 project from 100 Days of Code: The Complete Python Pro Bootcamp course

import random as ra

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(logo)
wanna_play = input("Do you want to play a game of Blackjack? Type 'y or 'n': ").lower()

while wanna_play != "n":
    hit = ""
    your_cards = []
    dealer_cards = []
    first_card = cards[ra.randint(0, len(cards) - 1)]
    second_card = cards[ra.randint(0, len(cards) - 1)]
    dealer_card_one = cards[ra.randint(0, len(cards) - 1)]
    dealer_card_two = cards[ra.randint(0, len(cards) - 1)]
    dealer_score = dealer_card_one + dealer_card_two
    player_score = first_card + second_card
    if player_score > 21:
        player_score -= 10
        second_card -= 10
    if dealer_score > 21:
        player_score -= 10
        dealer_card_two -= 10
    dealer_cards.append(dealer_card_one), dealer_cards.append(dealer_card_two)
    your_cards.append(first_card), your_cards.append(second_card)
    print(f"Your cards: {your_cards}, current score: {player_score}]")
    print(f"Computer's first card: {dealer_card_one}")
    if player_score == 21 and dealer_score == 21:
        print("Draw!")
    elif player_score == 21:
        print("Black Jack, you win!")
    elif dealer_score == 21:
        print("You Lose!")
    else:
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while hit != "n" and player_score < 21:
            another_card = cards[ra.randint(0, len(cards) - 1)]
            player_score += another_card
            if 11 in your_cards and player_score > 21:
                player_score -= 10
                your_cards[your_cards.index(11)] = 1
            your_cards.append(another_card)
            print(f"Your cards: {your_cards}, current score: {player_score}]")
            if player_score == 21:
                print("Black Jack, you win!")
            elif player_score > 21:
                print("You lose!")
            else:
                hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if hit == 'n':
        while dealer_score < 17 and player_score < 22:
            another_dealer = cards[ra.randint(0, len(cards) - 1)]
            dealer_cards.append(another_dealer)
            dealer_score += another_dealer
            if 11 in your_cards and player_score > 21:
                dealer_score -= 10
                dealer_cards[dealer_cards.index(11)] = 1

        if dealer_score > 21:
            print("You win!")
        elif 21 > player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("You lose!")
        else:
            print("Draw!")

    print(f"Dealer cards: {dealer_cards}. Dealer score: {dealer_score}")
    wanna_play = input("Do you want to play a game of Blackjack? Type 'y or 'n': ").lower()
