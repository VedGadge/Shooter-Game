import pygame 
pygame.init() # Initaliszing pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # create game window
pygame.display.set_caption('Shooter') # give the title to the window

# set frame rate
clock = pygame.time.Clock()
FPS = 60


# defone player action variables
moving_left = False
moving_right = False

# define colors
BG = (144,201,120)

def draw_bg():
    screen.fill(BG)

class Soldier(pygame.sprite.Sprite):
    def __init__(self,char_type, x, y, scale,speed):
        pygame.sprite.Sprite.__init__(self) # Inherit some functionality from sprite classs
        self.char_type = char_type
        self.speed = speed
        self.direction = 1          # 1--> look right, -1 --> look left
        self.flip = False
        img = pygame.image.load(f'img/{self.char_type}/Idle/0.png') # Loads the image that you want # idle image
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) # sclaing the image, self --> instance variable
        self.rect = self.image.get_rect() # Takes the size of the image and creates a rectangular boundary around it
        self.rect.center = (x,y)

    def move(self,moving_left,moving_right):
        # reset movement variables
        dx=0
        dy=0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1


        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)  # flips in x or y axis


player = Soldier('player',200,200,3,5)
enemy = Soldier('enemy',400,200,3,5)

       

run = True
while run:

    clock.tick(FPS)

    draw_bg() # every iteration it will generate the bg color so it there is no trail

    player.draw()
    enemy.draw()

    player.move(moving_left,moving_right)
    

    # EVENT HANDLER
    for event in pygame.event.get(): # Gets all the events that are happening
        # quit game
        if event.type == pygame.QUIT: # Clicked on the 'X' button on thw window
            run = False
        # keyboard presses
        if event.type == pygame.KEYDOWN: # basically means pressed any key on the keyboard
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False
        

        # keyboard buttion released
        if event.type == pygame.KEYUP: # When the key is released from the keyboard
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
        



    pygame.display.update() # tells pygame keep updating the game window in that iteration

pygame.quit()


