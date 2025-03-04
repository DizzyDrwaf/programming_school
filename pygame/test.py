import pygame
import random

# Function to check if two circular objects collide
def collides(obj_1_x, obj_1_y, obj_1_radius, obj_2_x, obj_2_y, obj_2_radius):
    distance_squared = ((obj_1_x - obj_2_x) ** 2 + (obj_1_y - obj_2_y) ** 2)
    return distance_squared < (obj_1_radius + obj_2_radius) ** 2

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Plums & Poisonous Cherries")

# Load images
snake_image = pygame.image.load("pygame/img/snake.png")
snake_x, snake_y = 50, 700
snake_radius = (snake_image.get_width() + snake_image.get_height()) / 4
snake_speed = 5
snake_direction = "right"

# Load fruit images
plum_image = pygame.image.load("pygame/img/plum.png")  # Good fruit (increases score)
cherry_image = pygame.image.load("pygame/img/cherries.png")  # Poisonous fruit (game over)
plums = []
cherries = []
plum_radius = (plum_image.get_width() + plum_image.get_height()) / 4
cherry_radius = (cherry_image.get_width() + cherry_image.get_height()) / 4

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GREEN)  # Clear screen
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Snake movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= snake_speed
        if snake_direction == "right":
            snake_image = pygame.transform.flip(snake_image, True, False)
            snake_direction = "left"
        if snake_x < 0:  
            snake_x = WIDTH
    if keys[pygame.K_RIGHT]:
        snake_x += snake_speed
        if snake_direction == "left":
            snake_image = pygame.transform.flip(snake_image, True, False)
            snake_direction = "right"
        if snake_x > WIDTH:
            snake_x = 0
    if keys[pygame.K_UP]:  
        snake_y -= snake_speed
        if snake_y < 0:
            snake_y = HEIGHT
    if keys[pygame.K_DOWN]: 
        snake_y += snake_speed
        if snake_y > HEIGHT:
            snake_y = 0

    # Spawn plums (good)
    if random.randint(0, 100) < 2:
        plums.append([random.randint(0, WIDTH), 0, 0])

    # Spawn cherries (poisonous)
    if random.randint(0, 200) < 2:
        cherries.append([random.randint(0, WIDTH), 0, 0])

    # Move plums
    for plum in plums[:]:
        plum[1] += plum[2]
        plum[2] += 0.2
        if plum[1] > HEIGHT:
            plums.remove(plum)
        if collides(snake_x, snake_y, snake_radius, plum[0], plum[1], plum_radius):
            plums.remove(plum)
            score += 1  # Increase score
            print("Yum! +1 Point")

    # Move cherries (poisonous)
    for cherry in cherries[:]:
        cherry[1] += cherry[2]
        cherry[2] += 0.2
        if cherry[1] > HEIGHT:
            cherries.remove(cherry)
        if collides(snake_x, snake_y, snake_radius, cherry[0], cherry[1], cherry_radius):
            print("Game Over! Poisonous Cherry!")
            running = False  

    # Draw elements
    screen.blit(snake_image, (snake_x, snake_y))
    for plum in plums:
        screen.blit(plum_image, (plum[0], plum[1]))
    for cherry in cherries:
        screen.blit(cherry_image, (cherry[0], cherry[1]))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()  
    clock.tick(60)  

pygame.quit()
