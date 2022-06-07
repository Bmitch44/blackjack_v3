import pygame as pg
import deckofcards as d


window = (800, 500)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 180, 50)

successes, failures = pg.init()
print(f"{successes} successes and {failures} failures")

screen = pg.display.set_mode((window)) # Notice the tuple! It's not 2 arguments.
clock = pg.time.Clock()
pg.display.set_caption("Blackjack")
FPS = 60  # This variable will define how many frames we update per second.

# load buttons
hit_not_clicked = pg.image.load("hit_button_nc.png")
button_rect = hit_not_clicked.get_rect()

dealer = d.Dealer("Dealer")
player = d.Player("player_name")

while True:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:  # The user pressed the close button in the top corner of the window.
            quit()
            # Close the program. Other methods like 'raise SystemExit' or 'sys.exit()'.
            # Calling 'pygame.quit()' won't close the program! It will just uninitialize the modules.
        if event.type == pg.MOUSEBUTTONDOWN:
            pass
        screen.fill(GREEN)

        screen.blit(hit_not_clicked, (738, 250))
       
        # creates and shuffles deck
        deck = d.Deck()
        deck.shuffle()

        # Deals 2 cards to player and 2 to dealer
        if len(dealer.hand) < 2:
            dealer.draw(deck, 2)
        if len(player.hand) < 2:
            player.draw(deck, 2)

        # Draws players hand on screen
        X, Y, Z = 320, 415, 5
        for card in player.hand:
            screen.blit(card.converted_img, (X,Y))
            X += 55
        X = 320
        screen.blit(dealer.hand[0].converted_img, (X, Z))

        ### To Be Implemented ###
        # Make Buttons instead of inputs
        # Finish game
        # Make card Animations
        ### To Be Implemented ###

        pg.display.update()  # Or pygame.display.flip()