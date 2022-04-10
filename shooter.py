import pygame 
pygame.init() # Initaliszing pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self) # Inherit some functionality from sprite classs
        
        img = pygame.image.load('img/player/Idle/0.png') # Loads the image that you want # idle image
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) # sclaing the image

        self.rect = self.image.get_rect() # Takes the size of the image and creates a rectangular boundary around it
        self.rect.center = (x,y)

    def draw(self):
        screen.blit(self.image,self.rect)


player = Soldier(200,200,3)
player2 = Soldier(400,200,3)
       

run = True
while run:

    # screen.blit(player.image,player.rect) # drawing the image on the screen
    # screen.blit(player2.image,player2.rect)

    player.draw()
    player2.draw()


    for event in pygame.event.get(): # Gets all the events that are happening
        # quit game
        if event.type == pygame.QUIT: # Clicked on the 'X' button on thw window
            run = False
    
    pygame.display.update() # tells pygame keep updating the game window in that iteration

pygame.quit()


