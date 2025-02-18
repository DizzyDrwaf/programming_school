'''
Tasks

1. Make it possible for the snake to move right.
2. Flip the snake image in the diraction it is moving.
3. When the snake moves off the screen to the right, make it reappear on the left side of the screen.

'''
 
import pygame
 
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
snake_image = pygame.image.load("pygame/img/snake.png")
snake_x = 50
snake_y = 700
snake_last_direction = "right"
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= 5
        if (snake_last_direction == "right"):
            snake_image = pygame.transform.flip(snake_image, True, False)
            snake_last_direction = "left"
        # Wrap the snake around the screen.
        if snake_x < 0:
            snake_x = 600
    
    if keys[pygame.K_RIGHT]:
        snake_x += 5
        if (snake_last_direction == "left"):
            snake_image = pygame.transform.flip(snake_image, True, False)
            snake_last_direction = "right"
        # Wrap the snake around the screen.
        if snake_x > 600:
            snake_x = 0
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)
 
    # --- Drawing code should go here
    screen.blit(snake_image, [snake_x, snake_y])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.