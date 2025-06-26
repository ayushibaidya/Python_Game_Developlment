import pygame
import time 
import random 

# creating the window
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain Dodge")

BG = pygame.transform.scale(pygame.image.load("space-bg.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

def draw(player): 
    WIN.blit(BG, (0,0))
    #where, color, who
    pygame.draw.rect(WIN, "red", player)

    pygame.display.update()

#main game loop

def main():
    run = True
    #X, Y, WIDTH, HEIGHT
    player = pygame.Rect(200,HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                break
        keys = pygame.key.get_pressed()   
        if keys[pygame.K_LEFT]:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT]:
            player.x += PLAYER_VEL


        draw(player)

    pygame.quit()

#directly run the python filer
if __name__ == "__main__":
    main()
