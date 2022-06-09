import pygame
import os 
pygame.init() # Initaliszing pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # create game window
pygame.display.set_caption('Shooter') # give the title to the window

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# define game variables
GRAVITY = 0.75

# defone player action variables
moving_left = False
moving_right = False

# define colors
BG = (144,201,120)
RED = (255,0,0)

def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen,RED,(0,300), (SCREEN_WIDTH,300)) # current floor

class Soldier(pygame.sprite.Sprite):
    def __init__(self,char_type, x, y, scale,speed):
        pygame.sprite.Sprite.__init__(self) # Inherit some functionality from sprite classs
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.direction = 1          # 1--> look right, -1 --> look left
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()  # To track when the last animation was updated
        
        #load all images for the players
        animation_types = ['Idle','Run','Jump']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count the no of files in the folder
            num_of_frames = len(os.listdir(f'img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png') # Loads the image that you want # idle image
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) # sclaing the image, self --> instance variable
                temp_list.append(img)
            self.animation_list.append(temp_list)

         

        self.image = self.animation_list[self.action][self.frame_index]
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

        #jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # apply gravity
        self.vel_y += GRAVITY
        # setting up the terminal velocitiy
        if self.vel_y >10:
            self.vel_y
        dy += self.vel_y    

        # check collision with the floor
        if self.rect.bottom + dy >300:
           dy = 300 - self.rect.bottom 
           self.in_air = False


        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def update_animatioin(self):
      # update animation
      ANIMATION_COOLDOWN = 100 # timer --> controls the speed of animation
      # update image depending on current frame
      self.image = self.animation_list[self.action][self.frame_index]

      # check if enough time has passed since the last update
      if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN :
          self.update_time = pygame.time.get_ticks()
          self.frame_index += 1
      # if the animation has run out then reset back to the start
      if self.frame_index >= len(self.animation_list[self.action]):
          self.frame_index = 0

    def update_action(self,new_action):
        #check if the new action is diifferent to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)  # flips in x or y axis


player = Soldier('player',200,200,3,5)
enemy = Soldier('enemy',400,200,3,5)

       

run = True
while run:

    clock.tick(FPS)

    draw_bg() # every iteration it will generate the bg color so it there is no trail

    player.update_animatioin()
    player.draw()
    enemy.draw()


    #update player actions
    if player.alive:
        if player.in_air:
            player.update_action(2) #2 -> jump
        elif moving_left or moving_right:
            player.update_action(1) #1 -> run
        else:
            player.update_action(0) # 0 -> idle

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
            if event.key == pygame.K_w and player.alive:
                player.jump = True
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


