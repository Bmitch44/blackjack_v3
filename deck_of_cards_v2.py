import pygame as pg
import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        self.initialize_img_file(suit, val)
        self.loaded_img = pg.transform.scale(pg.image.load(self.img_file_name), (50, 80))
        self.rect = self.loaded_img.get_rect()
    
    # creates the file name for each card, used to load image into pygame
    def initialize_img_file(self, suit, val):
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

    # changes the size of loaded image to  width x hieght
    def change_img_size(self, width, height):
        self.loaded_img = pg.transform.scale(self.loaded_img, (width, height))
    
    # prints the name of card, derived from the image file name
    def __repr__(self):
        card_name = ""
        for char in self.img_file_name:
            if char == "_":
                card_name += " "
            elif char == ".":
                break
            else:
                card_name += char
        return card_name

        
        

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    # Generate 52 cards
    def build(self):
        for suit in ["hearts", "clubs", "diamonds", "spades"]:
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

    # Return the top card
    def deal(self):
        return self.cards.pop()


class Button:
    def __init__(self, png, pos=(0, 0)):
        self.loaded_img = pg.image.load(png)
        self.rect = self.loaded_img.get_rect()
        self.rect.topleft = pos

    # changes the size of loaded image to  width x hieght
    def change_img_size(self, width, height):
        self.loaded_img = pg.transform.scale(self.loaded_img, (width, height))

        
class Player:
    def __init__(self):
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

    def calc_hand_val(self):
        sum = 0
        for card in self.hand:
            if card.value == 1 and sum < 11:
                sum += 11
            elif 11 <= card.value <= 13:
                sum += 10
            else:
                sum += card.value
        return sum

# d = Deck()
# d.shuffle()

# p = Player()
# p.draw(d, 2)

