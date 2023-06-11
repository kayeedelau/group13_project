import pygame

class Button():
    def __init__(self, x, y, image, scale):
    	
    	# get button data
        width = image.get_width()
        height= image.get_height()
        
        # fit into the screen size
        self.image = pygame.transform.scale(image, (int(width*scale),int(height*scale)))
        
        # get rect
        self.rect = self.image.get_rect()
        self.rect.center=(x,y)
        
        # clicked
        self.clicked= False

    def draw(self, surface):
        
        action = False

		# mouse track
        pos = pygame.mouse.get_pos()

		# collision
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked = False
        
        # draw
        surface.blit(self.image,(self.rect.x, self.rect.y))

        return action
