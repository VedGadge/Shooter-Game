import pygame

pygame.init()
# set frame rate
clock = pygame.time.Clock()
FPS = 60

# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')

#define game varibales
ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

# define colors
G = (144, 201, 120)
W = (255, 255, 255)
R = (200, 25, 25) 



#load Images
pine1_img = pygame.image.load('img/background/pine1.png').convert_alpha()
pine2_img = pygame.image.load('img/background/pine2.png').convert_alpha()
mountain_img = pygame.image.load('img/background/mountain.png').convert_alpha()
sky_img = pygame.image.load('img/background/sky_cloud.png').convert_alpha()

# create function for drawing background
def draw_bg():
    screen.fill(G)
    width = sky_img.get_width()
    for x in range(4):
        # here we multiplied scroll with some float value to give a depth perception
        # sky is the furthest away so it has the least multiplying factor
        screen.blit(sky_img,((x * width) -scroll * 0.5, 0))
        screen.blit(mountain_img,((x * width) -scroll * 0.6, SCREEN_HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine1_img,((x * width) -scroll * 0.7, SCREEN_HEIGHT - pine1_img.get_height() - 150))
        screen.blit(pine2_img,((x * width) -scroll * 0.8, SCREEN_HEIGHT - pine2_img.get_height()))

# draw grid
def draw_grid():
    # vertical lines
    for c in range(MAX_COLS + 1):
        pygame.draw.line(screen, W, (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE - scroll, SCREEN_HEIGHT))

       # horizontal lines
    for c in range(ROWS + 1):
        pygame.draw.line(screen, W, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))



run = True
while run:

    clock.tick(FPS)

    draw_bg()
    draw_grid()



    # scroll the  map
    if scroll_left == True and scroll > 0:
        scroll -= 5 * scroll_speed
    if scroll_right == True:
        scroll += 5 * scroll_speed


    for event in pygame.event.get(): # Gets all the events that are happening
        # quit game
        if event.type == pygame.QUIT: # Clicked on the 'X' button on thw window
            run = False
          # keyboard presses
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 5

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 1

            
            
        

    pygame.display.update()


pygame.quit()