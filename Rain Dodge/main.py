import pygame
import time 
import random 
pygame.font.init()

# creating the window
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain Dodge")

BG = pygame.transform.scale(pygame.image.load("space-bg.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

def draw(player, elapsed_time, stars): 
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    #where, color, who
    pygame.draw.rect(WIN, "red", player)
    
    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()

def start_screen():
    title_font = pygame.font.SysFont("comicsans", 50)
    title_text = title_font.render("Rain Dodge - Press any Key to Start", 1, "white")
    run = True
    while run: 
        WIN.blit(BG, (0,0))
        WIN.blit(title_text, (WIDTH/2 - title_text.get_width()/2, HEIGHT/2 - title_text.get_height()/2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                run = False

#main game loop

def main():

    start_screen()

    run = True
    #X, Y, WIDTH, HEIGHT
    player = pygame.Rect(200,HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH-STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            
            star_add_increment = max(200, star_add_increment -50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                break
        keys = pygame.key.get_pressed()   
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT: 
                stars.remove(star)
            elif star.y >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True 
                break
        
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)

        draw(player, elapsed_time, stars)

    pygame.quit()

#directly run the python filer
if __name__ == "__main__":
    main()
