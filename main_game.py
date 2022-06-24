import pygame as pg
import deck_of_cards_v2 as d
from time import sleep


window = (800, 500)
GREEN = (50, 180, 50)
hit_pos = (735, 220)
stay_pos = (735, 280)
start_pos = (735, 470)

# initializes pygame, prints successes and failures
successes, failures = pg.init()
print(f"{successes} successes and {failures} failures")

screen = pg.display.set_mode((window))
clock = pg.time.Clock()
pg.display.set_caption("Blackjack")

# for betting
c = 0

while True:
    if c == 0:
        game = d.Game(screen)
    else:
        game = d.Game(screen, game.balance)

    game.set_up_buttons(hit_pos, stay_pos, start_pos)

    done = False
    start = False

    while True:
        clock.tick(game.fps)
       

        for event in pg.event.get():
            game.screen.fill(GREEN)
            if event.type == pg.QUIT:  # The user pressed the close button in the top corner of the window.
                quit()
                # Close the program. Other methods like 'raise SystemExit' or 'sys.exit()'.
                # Calling 'pygame.quit()' won't close the program! It will just uninitialize the modules.
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if start == False:
                    if game.bet == 0:
                        if game.chip_1.rect.collidepoint(pos[0], pos[1]):
                            game.bet += 1
                            game.balance -= 1
                        if game.chip_5.rect.collidepoint(pos[0], pos[1]):
                            game.bet += 5
                            game.balance -= 5
                        if game.chip_10.rect.collidepoint(pos[0], pos[1]):
                            game.bet += 10
                            game.balance -= 10
                        if game.start_button_nc.rect.collidepoint(pos[0], pos[1]):
                            game.show_text("Please place bet", (400, 250), 30)
                            pg.display.update()
                            sleep(1)
                    else:
                        if game.chip_1.rect.collidepoint(pos[0], pos[1]):
                            game.bet += 1
                            game.balance -= 1
                        if game.chip_5.rect.collidepoint(pos[0], pos[1]):
                            game.bet += 5
                            game.balance -= 5
                        if game.chip_10.rect.collidepoint(pos[0], pos[1]):
                            game.bet += 10
                            game.balance -= 10
                        if game.start_button_nc.rect.collidepoint(pos[0], pos[1]):
                            start = True
                            game.start()
                else:
                    if game.hit_button_nc.rect.collidepoint(pos[0], pos[1]):
                        game.hit()
                    if game.stay_button_nc.rect.collidepoint(pos[0], pos[1]):
                        done = True
                        game.stay()
                    
        if game.balance < 0: 
            game.show_text("Refill! + $100", (400, 250), 30)
            pg.display.update()
            sleep(1)
            game.balance += 100
        
        game.show_text(f"Balance: ${game.balance}", (80, 50), 20)
                        
        game.display_cards(done)
        
        if game.finish_game(done):
            print(game.balance)
            game.screen.fill(GREEN)
            c += 1
            break
        
        if start == False:
            game.screen.blit(game.start_button_nc.loaded_img, game.start_button_nc.rect) 
        else:
            game.screen.fill(GREEN, game.start_button_nc.rect)
            game.screen.blit(game.hit_button_nc.loaded_img, game.hit_button_nc.rect) 
            game.screen.blit(game.stay_button_nc.loaded_img, game.stay_button_nc.rect) 
        if start == False:
            game.screen.blit(game.chip_1.loaded_img, game.chip_1.rect)
            game.screen.blit(game.chip_5.loaded_img, game.chip_5.rect)
            game.screen.blit(game.chip_10.loaded_img, game.chip_10.rect)
        else:
            game.screen.fill(GREEN, game.chip_1.rect)
            game.screen.fill(GREEN, game.chip_5.rect)
            game.screen.fill(GREEN, game.chip_10.rect)
        pg.display.update()
