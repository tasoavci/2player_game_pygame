import pygame
import os

WIDTH, HEIGHT = 900, 600
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 45
YELLOW_SPACESHIP_LOCATION_X, YELLOW_SPACESHIP_LOCATION_Y = 30, (HEIGHT/2) - (SPACESHIP_HEIGHT/2)
RED_SPACESHIP_LOCATION_X, RED_SPACESHIP_LOCATION_Y = WIDTH - (30 + SPACESHIP_WIDTH), (HEIGHT/2) - (SPACESHIP_HEIGHT/2)
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)

RED_SHIP_SPEED = 2.5
SHIP_SPEED = 2.5
BOOST_DURATION = 500  
BULLET_SPEED = 10
MAX_BULLETS = 5
cubuk_width = 8
cubuk_height = HEIGHT
cubuk_x = (WIDTH - cubuk_width) // 2
cubuk_y = 0


YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


BG_IMAGE = pygame.image.load(os.path.join("assets", "space.png"))
background_image = pygame.transform.scale(BG_IMAGE, (3840, 2160))
pygame.display.set_caption('GAME OF TASO')





def draw_window(red, yellow,yellow_bullets,red_bullets):
    WIN.blit(BG_IMAGE, (0, 0))
    pygame.draw.rect(WIN, WHITE, (cubuk_x, cubuk_y, cubuk_width, cubuk_height))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIN,(255,0,0),bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,(255,255,0),bullet)
    pygame.display.update()


def yellow_handle_movement(key_pressed, yellow):
    if key_pressed[pygame.K_a]:  # LEFT FOR YELLOW {KEY A}
        if key_pressed[pygame.K_LSHIFT]:
            yellow.x -= SHIP_SPEED + 0.5
        if yellow.x < 0:
            yellow.x = 0
        yellow.x -= SHIP_SPEED

    if key_pressed[pygame.K_d]:  # RIGHT FOR YELLOW {KEY D}
        if key_pressed[pygame.K_LSHIFT]:
            yellow.x += SHIP_SPEED + 0.5
        if yellow.x > WIDTH / 2 - yellow.width:
            yellow.x = WIDTH / 2 - yellow.width
        yellow.x += SHIP_SPEED

    if key_pressed[pygame.K_s]:  # DOWN FOR YELLOW {KEY S}
        if key_pressed[pygame.K_LSHIFT]:
            yellow.y += SHIP_SPEED + 0.5
        if yellow.y > HEIGHT - yellow.height - 8:
            yellow.y = HEIGHT - yellow.height - 8
        yellow.y += SHIP_SPEED

    if key_pressed[pygame.K_w]:  # UP FOR YELLOW {KEY W}
        if key_pressed[pygame.K_LSHIFT]:
            yellow.y -= SHIP_SPEED + 0.5
        if yellow.y < 8:
            yellow.y = 8
        yellow.y -= SHIP_SPEED


        

            


def red_handle_movement(key_pressed, red):
    if key_pressed[pygame.K_LEFT]:
        if key_pressed[pygame.K_RSHIFT]:
            red.x -= SHIP_SPEED + 0.5
        if red.x < WIDTH / 2:
            red.x = WIDTH / 2
        red.x -= SHIP_SPEED
    if key_pressed[pygame.K_RIGHT]:
        if key_pressed[pygame.K_RSHIFT]:
            red.x += SHIP_SPEED + 0.5
        if red.x > WIDTH - red.width:
            red.x = WIDTH - red.width
        red.x += SHIP_SPEED
    if key_pressed[pygame.K_UP]:
        if key_pressed[pygame.K_RSHIFT]:
            red.y -= SHIP_SPEED + 0.5
        if red.y < 8:
            red.y = 8
        red.y -= SHIP_SPEED
    if key_pressed[pygame.K_DOWN]:
        if key_pressed[pygame.K_RSHIFT]:
            red.y += SHIP_SPEED + 0.5
        if red.y > HEIGHT - red.height - 10:
            red.y = HEIGHT - red.height - 10
        red.y += SHIP_SPEED

def handle_bullets(red_bullets,yellow_bullets,red,yellow):
    for bullet in yellow_bullets:
        bullet.x += BULLET_SPEED
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_SPEED
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
    


def main():
    yellow = pygame.Rect(YELLOW_SPACESHIP_LOCATION_X, YELLOW_SPACESHIP_LOCATION_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(RED_SPACESHIP_LOCATION_X, RED_SPACESHIP_LOCATION_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True

    red_bullets = []
    yellow_bullets = []
       
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 , 10,5)
                    yellow_bullets.append(bullet)
                
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 , 10,5)
                    red_bullets.append(bullet)
                    
        print(f'yellow:{yellow_bullets}   red: {red_bullets}') 
        
        
        
        
        key_pressed = pygame.key.get_pressed()
        yellow_handle_movement(key_pressed, yellow)
        red_handle_movement(key_pressed, red)

        handle_bullets(red_bullets,yellow_bullets,red,yellow)


        draw_window(red, yellow,yellow_bullets,red_bullets)
    pygame.quit()


if __name__ == "__main__":
    main()
