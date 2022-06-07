import random
from time import sleep
import pygame as pg

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

        if self.value == 1:
            self.img_file_name = f"ace_of_{suit}.png"
        elif self.value == 11:
            self.img_file_name = f"jack_of_{suit}.png"
        elif self.value == 12:
            self.img_file_name = f"queen_of_{suit}.png"
        elif self.value == 13:
            self.img_file_name = f"king_of_{suit}.png"
        else:
            self.img_file_name = f"{val}_of_{suit}.png"

        self.converted_img = pg.transform.scale(pg.image.load(self.img_file_name), (50, 80))
        self.rect = self.converted_img.get_rect()

    # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()
        
    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return f"{val} of {self.suit}"


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print(card.show())

    # Generate 52 cards
    def build(self):
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1,14):
                self.cards.append(Card(suit, val))

    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]    
            # You can also use the build in shuffle method
            # random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.balance = 10
        self.hand_value = 0
        self.hand = []

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else: 
                return False
        return True

    # Display all the cards in the players hand
    def showHand(self):
        print(f"\n{self.name}'s hand: {self.hand}")
        return self

    def discard(self):
        return self.hand.pop()

    def calc_hand_value(self):
        self.hand_value = 0
        for card in self.hand:
            if card.value == 11:
                self.hand_value += 10
            elif card.value == 12:
                self.hand_value += 10
            elif card.value == 13:
                self.hand_value += 10
            elif card.value == 1:
                if self.hand_value <= 10:
                    self.hand_value += 11
                else:
                    self.hand_value += 1
            else:
                self.hand_value += card.value

    def place_bet(self, wager):
        self.balance -= wager

    def calc_profit(self, wager):
        self.balance += wager * 2

    def player_turn(self, deck):
        while self.hand_value < 21:
            prompt = input(f"\nYour hand value is {self.hand_value}, Hit or Stay: ").lower()
            if prompt == "hit":
                self.draw(deck)
                self.calc_hand_value()
                self.showHand()
            elif prompt == "stay":
                break
            else:
                print("\nPlease type hit or stay")


class Dealer(Player):
    def __init__(self, name):
        super().__init__(name)

    def show_dealer_hand(self):
        print(f"\n{self.name}'s hand: [{self.hand[0]}, ***]")
        return self

    def dealer_turn(self, deck):
        while self.hand_value < 17:
            self.showHand()
            self.draw(deck)
            self.calc_hand_value()
            sleep(5)
        self.showHand()


        


# Test making a Card
# card = Card('Spades', 6)
# print(card)
# print(card.image)

# Test making a Deck
# myDeck = Deck()
# myDeck.shuffle()
# deck.show()

# bob = Player("Bob")
# bob.sayHello()
# bob.draw(myDeck, 2)
# bob.showHand()
# myDeck.show()
