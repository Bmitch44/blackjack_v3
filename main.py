import deckofcards as d
import pygame as pg

def start_game():
    player_name = input("\nWhat is your name? ")

    # initalizes player and dealer
    dealer = d.Dealer("Dealer")
    player = d.Player("player_name")

    while True:
        start = input("\nType 's' to start or 'q' to quit: ").lower()
        if start == "q":
            quit()
        
        print(f"\nYour balance is ${player.balance}")

        bet = int(input("Please place your bet: "))
        player.place_bet(bet)


        # creates and shuffles deck
        deck = d.Deck()
        deck.shuffle()

        # Deals 2 cards to player and 2 to dealer
        if len(dealer.hand) < 2:
                dealer.draw(deck, 2)
        if len(player.hand) < 2:
            player.draw(deck, 2)

        # Draws players hand on screen (Pygame)
        # X, Y, Z = 320, 415, 5
        # for card in player.hand:
        #     surface.blit(card.converted_png, (X,Y))
        #     X += 55
        
        # surface.blit(dealer.hand[0].converted_png, (X, Z))
        


        player.showHand()
        dealer.show_dealer_hand()
        
        # calculates hand values
        player.calc_hand_value()
        dealer.calc_hand_value()

        # checks for blackjack
        if player.hand_value == 21:
            print(f"Blackjack! You win ${bet * 2}!")
            player.calc_profit(bet)
            player.hand.clear()
            dealer.hand.clear()
            continue

        # players turn
        player.player_turn(deck)
        
        # checks for player bust
        if player.hand_value > 21:
            print(f"\nBust with {player.hand_value}! Dealer wins")
            player.hand.clear()
            dealer.hand.clear()
            continue
        else:
            # dealers turn
            dealer.dealer_turn(deck)
        
        # determines winner
        if dealer.hand_value > 21:
            print(f"\nDealer Bust with {dealer.hand_value}! You Win ${bet * 2}!")
            player.calc_profit(bet)
            player.hand.clear()
            dealer.hand.clear()
            continue
        else:
            if player.hand_value > dealer.hand_value:
                print(f"\nYou scored {player.hand_value}, beating the dealer's {dealer.hand_value}. You win ${bet * 2}!")
                player.calc_profit(bet)
            elif player.hand_value < dealer.hand_value:
                print(f"\nThe Dealer scored {dealer.hand_value}, beating your {player.hand_value}. You lose!")
            else:
                print("\nDraw!")
                player.balance += bet

        player.hand.clear()
        dealer.hand.clear()


start_game()