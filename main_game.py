import pygame as pg
import deck_of_cards_v2 as d
from time import sleep

window = (800, 500)

GREEN = (50, 180, 50)

successes, failures = pg.init()
print(f"{successes} successes and {failures} failures")

screen = pg.display.set_mode((window)) # Notice the tuple! It's not 2 arguments.
clock = pg.time.Clock()
pg.display.set_caption("Blackjack")
FPS = 60  # This variable will define how many frames we update per second.

dealer = d.Player()
player = d.Player()

hit_pos = (735, 220)
stay_pos = (735, 280)
start_pos = (735, 470)
 
hit_button_nc = d.Button("hit_button_nc.png", hit_pos)
hit_button_c = d.Button("hit_button_c.png", hit_pos)
stay_button_nc = d.Button("stay_button_nc.png", stay_pos)
stay_button_c = d.Button("stay_button_c.png", stay_pos)
start_button_nc = d.Button("start_button_nc.png", start_pos)
start_button_c = d.Button("start_button_c.png", start_pos)

you_win = pg.transform.scale(pg.image.load("you_win.jpeg"), (200, 150))
you_lose = pg.transform.scale(pg.image.load("you_lose.png"), (200, 150))

done = False

while True:
    clock.tick(FPS)

    for event in pg.event.get():
        screen.fill(GREEN)
        if event.type == pg.QUIT:  # The user pressed the close button in the top corner of the window.
            quit()
            # Close the program. Other methods like 'raise SystemExit' or 'sys.exit()'.
            # Calling 'pygame.quit()' won't close the program! It will just uninitialize the modules.
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            if start_button_nc.rect.collidepoint(pos[0], pos[1]):
                screen.blit(start_button_c.loaded_img, start_pos)
                sleep(1)
                deck = d.Deck()
                deck.shuffle()
                player.draw(deck, 2)
                dealer.draw(deck, 2)
            if hit_button_nc.rect.collidepoint(pos[0], pos[1]):
                screen.blit(hit_button_c.loaded_img, hit_pos)
                sleep(1)
                player.draw(deck)
            if stay_button_nc.rect.collidepoint(pos[0], pos[1]):
                screen.blit(stay_button_c.loaded_img, stay_pos)
                sleep(1)
                while dealer.calc_hand_val() < 17:
                    dealer.draw(deck)
                    sleep(1)
                done = True
                    
        X = 300
        for card in player.hand:
            screen.blit(card.loaded_img, (X, 410))
            X += 53
        X = 300
        for card in dealer.hand:
            screen.blit(card.loaded_img, (X, 10))
            X += 53
        
        if player.calc_hand_val() > 21:
                screen.blit(you_lose, (300, 175))
                pg.display.update()
                sleep(5)
                quit()
        elif player.calc_hand_val() == 21:
                screen.blit(you_win, (300, 175))
                pg.display.update()
                sleep(5)
                quit()

        if done:
            if dealer.calc_hand_val() == 21:
                screen.blit(you_lose, (300, 175))
                pg.display.update()
                sleep(5)
                quit()
            elif dealer.calc_hand_val() > 21:
                screen.blit(you_win, (300, 175))
                pg.display.update()
                sleep(5)
                quit()
            else:
                if player.calc_hand_val() > dealer.calc_hand_val():
                    screen.blit(you_win, (300, 175))
                    pg.display.update()
                    sleep(5)
                    quit()
                else:
                    screen.blit(you_lose, (300, 175))
                    pg.display.update()
                    sleep(5)
                    quit()


        
        screen.blit(start_button_nc.loaded_img, start_pos) 
        screen.blit(hit_button_nc.loaded_img, hit_pos) 
        screen.blit(stay_button_nc.loaded_img, stay_pos) 
        pg.display.update()
