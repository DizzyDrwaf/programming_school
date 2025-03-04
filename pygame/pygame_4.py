'''
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

# Score
score = 0
font = pygame.font.Font(None, 36)
 
pygame.display.set_caption("My Game")

# Add visual elements to the game
snake_image = pygame.image.load("pygame/img/snake.png")
snake_x = 50
snake_y = 700
snake_last_direction = "right"
snake_radius = (snake_image.get_width() + snake_image.get_height()) / 4

plum_image = pygame.image.load("pygame/img/plum.png")
cherry_image = pygame.image.load("pygame/img/cherries.png")
plums = []
cherries = []
plum_radius = (plum_image.get_width() + plum_image.get_height()) / 4
cherry_radius = (cherry_image.get_width() + cherry_image.get_height()) / 4


 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#score
score = 0
 
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

    # plums
    # Chance of having a new plum.
    if (random.randint(0, 100) < 2):
        plum_x = random.randint(0, 600)
        # Add plum coodinates to the list.
        plums.append([plum_x, 0, 0]) # x, y, speed
    
    # move plums
    for plum in plums:
        # Move the plum down.
        plum[1] += plum[2]
        # Increase the speed of the plum.
        plum[2] += 0.2
        # Remove plums that have gone off the screen.
        if plum[1] > 800:
            plums.remove(plum)
        # Check for collisions with the snake.
        if collides(snake_x, snake_y, snake_radius, 
                    plum[0], plum[1], plum_radius):
            plums.remove(plum)
            score += 1
            print("Yum!")

    for cherry in cherries[:]:
        cherry[1] += cherry[2]
        cherry[2] += 0.2
        if cherry[1] > 800:
            cherries.remove(cherry)
        if collides(snake_x, snake_y, snake_radius, cherry[0], cherry[1], cherry_radius):
            print("Game Over! Poisonous Cherry!")
            done = True
    
        # Chance of having a new plum.
    if (random.randint(0, 200) < 2):
        cherry_x = random.randint(0, 600)
        # Add plum coodinates to the list.
        cherries.append([cherry_x, 0, 0]) # x, y, speed

        
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)
 
    # --- Drawing code should go here
    screen.blit(snake_image, [snake_x, snake_y])
    for plum in plums:
        screen.blit(plum_image, [plum[0], plum[1]])
    for cherry in cherries:
        screen.blit(cherry_image, (cherry[0], cherry[1]))
    screen.blit(font.render("Score: " + str(score), True, WHITE), [5, 5])

 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.