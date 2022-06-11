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

while True:
    game = d.Game(screen)
    game.set_up_buttons(hit_pos, stay_pos, start_pos)

    done = False

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
                if game.start_button_nc.rect.collidepoint(pos[0], pos[1]):
                    game.start()
                if game.hit_button_nc.rect.collidepoint(pos[0], pos[1]):
                    game.hit()
                if game.stay_button_nc.rect.collidepoint(pos[0], pos[1]):
                    game.stay()
                    done = True
                        
        game.display_cards(done)
        
        if game.finish_game(done):
            game.screen.fill(GREEN)
            break
            
        game.screen.blit(game.start_button_nc.loaded_img, start_pos) 
        game.screen.blit(game.hit_button_nc.loaded_img, hit_pos) 
        game.screen.blit(game.stay_button_nc.loaded_img, stay_pos) 
        pg.display.update()
