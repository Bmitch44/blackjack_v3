import pygame as pg
import random
from time import sleep

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


class Game:
    def __init__(self, display):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()
        self.fps = 60
        self.screen = display
        
    def set_up_buttons(self, hit_pos, stay_pos, start_pos):
        self.hit_button_nc = Button("hit_button_nc.png", hit_pos)
        self.hit_button_c = Button("hit_button_c.png", hit_pos)
        self.stay_button_nc = Button("stay_button_nc.png", stay_pos)
        self.stay_button_c = Button("stay_button_c.png", stay_pos)
        self.start_button_nc = Button("start_button_nc.png", start_pos)
        self.start_button_c = Button("start_button_c.png", start_pos)

        self.you_win = pg.transform.scale(pg.image.load("you_win.jpeg"), (200, 150))
        self.you_lose = pg.transform.scale(pg.image.load("you_lose.png"), (200, 150))

    def start(self):
        sleep(1)
        self.deck.shuffle()
        self.player.draw(self.deck, 2)
        self.dealer.draw(self.deck, 2)

    def hit(self):
        sleep(1)
        self.player.draw(self.deck)

    def stay(self):
        sleep(1)
        while self.dealer.calc_hand_val() < 17:
            self.dealer.draw(self.deck)
            sleep(1)
    
    def display_cards(self):
        X = 300
        for card in self.player.hand:
            self.screen.blit(card.loaded_img, (X, 410))
            X += 53
        X = 300
        for card in self.dealer.hand:
            self.screen.blit(card.loaded_img, (X, 10))
            X += 53

    def finish_game(self, bool):
        if self.player.calc_hand_val() > 21:
                self.screen.blit(self.you_lose, (300, 175))
                pg.display.update()
                sleep(2)
                return True
        elif self.player.calc_hand_val() == 21:
                self.screen.blit(self.you_win, (300, 175))
                pg.display.update()
                sleep(2)
                return True

        if bool:
            if self.dealer.calc_hand_val() == 21:
                self.screen.blit(self.you_lose, (300, 175))
                pg.display.update()
                sleep(2)
                return True
            elif self.dealer.calc_hand_val() > 21:
                self.screen.blit(self.you_win, (300, 175))
                pg.display.update()
                sleep(2)
                return True
            else:
                if self.player.calc_hand_val() > self.dealer.calc_hand_val():
                    self.screen.blit(self.you_win, (300, 175))
                    pg.display.update()
                    sleep(2)
                    return True
                else:
                    self.screen.blit(self.you_lose, (300, 175))
                    pg.display.update()
                    sleep(2)
                    return True
        else:
            return False



# d = Deck()
# d.shuffle()

# p = Player()
# p.draw(d, 2)

