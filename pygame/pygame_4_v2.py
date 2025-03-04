'''
Uses Sprite object insted of list och dictionary to store each plum.


Tasks

1. Make the snake move properly.
2. Add score. Display the score on the screen.
3. Add an other fruit, that will kill the snake.

'''
 
import pygame
import random

def collides(obj_1_x, obj_1_y, obj_1_radius, obj_2_x, obj_2_y, obj_2_radius):
    ''' Check if two objects collide. Circular collision detection.
    '''
    distance_squared = ((obj_1_x - obj_2_x) ** 2 + (obj_1_y - obj_2_y) ** 2)
    return distance_squared < (obj_1_radius + obj_2_radius) ** 2

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (600, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

# Add visual elements to the game
snake = pygame.sprite.Sprite()
snake.image = pygame.image.load("img/snake.png")
snake.rect = snake.image.get_rect()
snake.rect.x = 50
snake.rect.y = 700
snake.last_direction = "right"
snake.radius = (snake.image.get_width() + snake.image.get_height()) / 4


plum_image = pygame.image.load("img/plum.png")
plums = pygame.sprite.Group()
plum_radius = (plum_image.get_width() + plum_image.get_height()) / 4
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
is_running = True

# -------- Main Program Loop -----------
while is_running:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
 
    # --- Game logic should go here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.rect.x -= 5
        if (snake.last_direction == "right"):
            snake.image = pygame.transform.flip(snake.image, True, False)
            snake.last_direction = "left"
        # Wrap the snake around the screen.
        if snake.rect.x < 0:
            snake.rect.x = 600

    # plums
    # Chance of having a new plum.
    if (random.randint(0, 100) < 2):
        plum_x = random.randint(0, 600)
        # Add plum coodinates to the list.
        plum = pygame.sprite.Sprite()
        plum_width = random.randint(20, 40)
        plum_radio = plum_image.get_height() / plum_image.get_width()
        plum.image = pygame.transform.scale(plum_image, (plum_width, plum_width * plum_radio)) 
        plum.rect = plum.image.get_rect()
        plum.rect.x = plum_x
        plum.rect.y = 0
        plum.speed = 0
        plum.radius = (plum.image.get_width() + plum.image.get_height()) / 4
        plums.add(plum) # x, y, speed
    
    # move plums
    for plum in plums:
        # Move the plum down.
        plum.rect.y += plum.speed
        # Increase the speed of the plum.
        plum.speed += 0.2
        # Remove plums that have gone off the screen.
        if plum.rect.y > 800:
            plums.remove(plum)
        # Check for collisions with the snake.
        plum = pygame.sprite.spritecollideany(snake, plums)
        if plum != None:
            plums.remove(plum)
            print("Yum!")
        

        
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)
 
    # --- Drawing code should go here
    screen.blit(snake.image, snake.rect)
    for plum in plums:
        screen.blit(plum.image, plum.rect)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Clean up when the game exits.
pygame.quit()