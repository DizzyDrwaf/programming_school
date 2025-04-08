'''
Maze Game
Loaded from a file.

Tasks:
1. Make the player visible in the maze. Hint: blit
2. Make the player move with the arrow keys.
3. Make the player stop when it hits a wall. In all directions.
4. Add objects to pick up. Use: chrystal_wall_lightmagenta.png
5. Make the player pick up the object when it collides with it.
6. Make the object disappear when the player picks it up.
7. Add score to the game. Show the score on the screen.
8. When all objects are picked up, show a message on the screen.
9. Add monsters that move around in the maze. 
   Random movement of your choice. Use: ogre_old.png
10. Game over if the player collides with a monster.

Extra tasks:
1. Show the doors in the maze.
2. If the player enters a door, the player is teleported to another door.
'''
import pygame


# --- Define helper functions
def get_one_colliding_objects(object_1, objects):
    '''Returns the first object in the list of objects
    that collides with object_1.
    Returns None if no object collides.'''
    for object_2 in objects:
        obj_1_rect = pygame.Rect(object_1['x'], object_1['y'], object_1['image'].get_width(), object_1['image'].get_height())
        obj_2_rect = pygame.Rect(object_2['x'], object_2['y'], object_2['image'].get_width(), object_2['image'].get_height())
        if obj_1_rect.colliderect(obj_2_rect):
            return object_2
    return None

def get_one_colliding_object(object_1, objects):
    '''Returns the first object in the list of objects
    that collides with object_1.
    Returns None if no object collides.'''
    obj_1_rect = pygame.Rect(object_1['x'], object_1['y'], object_1['image'].get_width(), object_1['image'].get_height())
    obj_2_rect = pygame.Rect(objects['x'], objects['y'], objects['image'].get_width(), objects['image'].get_height())
    if obj_1_rect.colliderect(obj_2_rect):
        return objects
    return None

def make_maze(maze_content, wall_size):
    walls = []

    door_size = door_image.get_width()
    doors = []

    chrystal_size = chrystal_image.get_width()
    chrystals = []

    ogre_size = ogre_image.get_width()
    ogres = []

    # Create the player
    player = {}
    player['image'] = player_image
    player['speed'] = 4
    maze_content['player'] = player
    maze_content['walls'] = walls
    maze_content['crystals'] = chrystals
    maze_content['doors'] = doors
    maze_content['ogres'] = ogres
    file = open('pygame/maze.txt', 'r')
    line = file.readline()
    maze_width = len(line) - 1  # Do not count the newline character.
    maze_height = 0
    x = 0
    y = 0
    while len(line) > 1:
        maze_height += 1
        for char in line:
            if char == 'x':
                wall = {}
                wall['x'] = x
                wall['y'] = y
                wall['image'] = wall_image
                maze_content['walls'].append(wall)
            elif char == 'e':
                maze_content['player']['x'] = x
                maze_content['player']['y'] = y
            elif char == 'c':
                crystal = {}
                crystal['x'] = x
                crystal['y'] = y
                crystal['image'] = chrystal_image
                maze_content['crystals'].append(crystal)
            elif char == 'd':
                door = {}
                door['x'] = x
                door['y'] = y
                door['image'] = door_image
                maze_content['doors'].append(door)
            elif char == 'o':
                ogre = {}
                ogre['x'] = x
                ogre['y'] = y
                ogre['image'] = ogre_image
                maze_content['ogres'].append(ogre)

            x += wall_size
        x = 0
        y += wall_size


        line = file.readline()
 
    file.close()
    return( (maze_width * wall_size, maze_height * wall_size) )

# --- Initialize Pygame
pygame.init()

# --- Add elements to the game.
# load graphics
sand_image = pygame.image.load("pygame/img/floor_sand_stone_0.png")
wall_image = pygame.image.load("pygame/img/brick_brown_0.png")
chrystal_image = pygame.image.load("pygame/img/crystal_wall_lightmagenta.png")
door_image = pygame.image.load("pygame/img/open_door.png")
ogre_image = pygame.image.load("pygame/img/ogre_old.png")
player_image = pygame.image.load("pygame/img/deep_elf_knight_old.png") 
# colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
# Add visual elements to the game

wall_size = wall_image.get_width()


# Read the maze from the file.

#file = open('pygame/maze.txt', 'r')
#line = file.readline()
#maze_width = len(line) - 1  # Do not count the newline character.
#maze_height = 0
#x = 0
#y = 0
#while len(line) > 1:
#    maze_height += 1
#    for char in line:
#        if char == 'x':
#            wall = {}
#            wall['x'] = x
#            wall['y'] = y
#            wall['image'] = wall_image
#            walls.append(wall)
#        elif char == 'e':
#            maze_content['player']['x'] = x
#            maze_content['player']['y'] = y
#        elif char == 'c':
#            crystal = {}
#            crystal['x'] = x
#            crystal['y'] = y
#            crystal['image'] = chrystal_image
#            chrystals.append(crystal)
#        elif char == 'd':
#            door = {}
#            door['x'] = x
#            door['y'] = y
#            door['image'] = door_image
#            doors.append(door)
#        elif char == 'o':
#            ogre = {}
#            ogre['x'] = x
#            ogre['y'] = y
#            ogre['image'] = ogre_image
#            ogres.append(ogre)
#
#        x += wall_size
#    x = 0
#    y += wall_size
#    line = file.readline()
#
#file.close()

# --- player starting direction ---

player_last_direction = "left"
# --- variable ---

maze_content = {}
# --- score --- 
size = make_maze(maze_content, wall_size)
score = 0
font = pygame.font.Font(None, 36)

last_door = "top"
is_outside_door = True

# --- Set the width and height of the screen [width, height]
#size = (maze_width_list[0] * wall_size, maze_height_list[0] * wall_size)
screen = pygame.display.set_mode(size) # maze_size * wall_size

pygame.display.set_caption("Maze Game")

# --- Game time
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
game_is_pause = False
is_running = True
while is_running:
    # --- Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    if game_is_pause == False:
        # --- Game logic should go here
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            game_is_pause = True
        

        # --- Move the player
        if score == 7:
            game_is_pause = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            maze_content['player']['x'] -= maze_content['player']['speed']
            if get_one_colliding_objects(maze_content['player'], maze_content['walls']):
                maze_content['player']['x'] += maze_content['player']['speed']

            elif get_one_colliding_objects(maze_content['player'], maze_content['crystals']):
                score += 1
                maze_content['crystals'].remove(get_one_colliding_objects(maze_content['player'], maze_content['crystals']))

            elif get_one_colliding_objects(maze_content['player'], maze_content['doors']):
                if is_outside_door == True:
                    is_outside_door = False
                    # kolla spelarens x och y, hitta samma dörr
                    if get_one_colliding_object(maze_content['player'], maze_content['doors'][0]):
                        maze_content['player']['x'] = wall_size * 10
                        maze_content['player']['y'] = wall_size * 9
                        is_outside_door = False
                    elif get_one_colliding_object(maze_content['player'], maze_content['doors'][1]):
                        maze_content['player']['x'] = wall_size * 5
                        maze_content['player']['y'] = wall_size * 5
                        is_outside_door = False
            else:
                # utanför dörr
                is_outside_door = True

            if (player_last_direction == "right"):
                player_image = pygame.transform.flip(player_image, True, False)
                player_last_direction = "left"

        elif keys[pygame.K_RIGHT]:
            maze_content['player']['x'] += maze_content['player']['speed']
            if get_one_colliding_objects(maze_content['player'], maze_content['walls']):
                maze_content['player']['x'] -= maze_content['player']['speed']

            elif get_one_colliding_objects(maze_content['player'], maze_content['crystals']):
                score += 1
                maze_content['crystals'].remove(get_one_colliding_objects(maze_content['player'], maze_content['crystals']))

            elif get_one_colliding_objects(maze_content['player'], maze_content['doors']):
                if is_outside_door == True:
                    is_outside_door = False
                    # kolla spelarens x och y, hitta samma dörr
                    if get_one_colliding_object(maze_content['player'], maze_content['doors'][0]):
                        maze_content['player']['x'] = wall_size * 10
                        maze_content['player']['y'] = wall_size * 9
                        is_outside_door = False
                    elif get_one_colliding_object(maze_content['player'], maze_content['doors'][1]):
                        maze_content['player']['x'] = wall_size * 5
                        maze_content['player']['y'] = wall_size * 5
                        is_outside_door = False
            else:
                # utanför dörr
                is_outside_door = True

            if (player_last_direction == "left"):
                player_image = pygame.transform.flip(player_image, True, False)
                player_last_direction = "right"

        elif keys[pygame.K_UP]:
            maze_content['player']['y'] -= maze_content['player']['speed']
            if get_one_colliding_objects(maze_content['player'], maze_content['walls']):
                maze_content['player']['y'] += maze_content['player']['speed']

            elif get_one_colliding_objects(maze_content['player'], maze_content['crystals']):
                score += 1
                maze_content['crystals'].remove(get_one_colliding_objects(maze_content['player'], maze_content['crystals']))

            elif get_one_colliding_objects(maze_content['player'], maze_content['doors']):
                if is_outside_door == True:
                    is_outside_door = False
                    # kolla spelarens x och y, hitta samma dörr
                    if get_one_colliding_object(maze_content['player'], maze_content['doors'][0]):
                        maze_content['player']['x'] = wall_size * 10
                        maze_content['player']['y'] = wall_size * 9
                        is_outside_door = False
                    elif get_one_colliding_object(maze_content['player'], maze_content['doors'][1]):
                        maze_content['player']['x'] = wall_size * 5
                        maze_content['player']['y'] = wall_size * 5
                        is_outside_door = False
            else:
                # utanför dörr
                is_outside_door = True

        elif keys[pygame.K_DOWN]:
            maze_content['player']['y'] += maze_content['player']['speed']
            if get_one_colliding_objects(maze_content['player'], maze_content['walls']):
                maze_content['player']['y'] -= maze_content['player']['speed']

            elif get_one_colliding_objects(maze_content['player'], maze_content['crystals']):
                score += 1
                maze_content['crystals'].remove(get_one_colliding_objects(maze_content['player'], maze_content['crystals']))

            elif get_one_colliding_objects(maze_content['player'], maze_content['doors']):
                if is_outside_door == True:
                    is_outside_door = False
                    # kolla spelarens x och y, hitta samma dörr
                    if get_one_colliding_object(maze_content['player'], maze_content['doors'][0]):
                        maze_content['player']['x'] = wall_size * 10
                        maze_content['player']['y'] = wall_size * 9
                        is_outside_door = False
                    elif get_one_colliding_object(maze_content['player'], maze_content['doors'][1]):
                        maze_content['player']['x'] = wall_size * 5
                        maze_content['player']['y'] = wall_size * 5
                        is_outside_door = False
            else:
                # utanför dörr
                is_outside_door = True

        else:
            # snap player to grid
            maze_content['player']['x'] = round(maze_content['player']['x'] / wall_size) * wall_size
            maze_content['player']['y'] = round(maze_content['player']['y'] / wall_size) * wall_size






        # --- Screen-clearing code goes here
        # fill widh sand
        for y in range(0, size[1], wall_size):
            for x in range(0, size[0], wall_size):
                screen.blit(sand_image, (x, y))
        # --- Drawing code should go here
        for wall in maze_content['walls']:
            screen.blit(wall_image, (wall['x'], wall['y']))

        for crystal in maze_content['crystals']:
            screen.blit(chrystal_image, (crystal['x'], crystal['y']))

        for door in maze_content['doors']:
            screen.blit(door_image, (door['x'], door['y']))
        
        for ogre in maze_content['ogres']:
            screen.blit(ogre_image, (ogre['x'], ogre['y']))

        screen.blit(player_image, (maze_content['player']['x'], maze_content['player']['y']))
        #screen.blit(maze_content)
        screen.blit(font.render("Score: " + str(score), True, WHITE), [5, 5])

        if score == 7 and game_is_pause == True:
            screen.blit(font.render("You Win!!!!", True, WHITE), [(wall_size * 4) + (wall_size * 0.5), (wall_size * 6) - (wall_size * 0.5)])
            screen.blit(font.render("Press Return to play again", True, WHITE), [(wall_size * 1) + (wall_size * 0.75), (wall_size * 7) - (wall_size * 0.5)])

        pygame.display.update()  # or pygame.display.flip()
        # --- Increase game time
        clock.tick(60)  # 60 frames per second
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        if game_is_pause == True and score == 7:
            score = 0
            make_maze(maze_content, wall_size)
        game_is_pause = False
        
# Clean up when the game exits.
pygame.quit()
