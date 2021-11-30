#pygame library
import pygame
import time

#buttons class
class Button():

        #initialising the buttons class
        def __init__(self,x,y,image,scale):
            width = image.get_width()
            height = image.get_height()
            self.image = image

            #sets image scale, then takes image length and width and forms a hitbox.
            self.image = pygame.transform.scale(image,(int(width*scale), int(height*scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)
            self.clicked = False


#draw and click method
        def draw(self,surface):
            action = False
            pos = pygame.mouse.get_pos()
            #if the mouse is over the button and the mousebutton is clicked then register a click
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
                    time.sleep(0.1)
            #if no longer clicked then set clicked to false
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            #draw it
            surface.blit(self.image,(self.rect.x,self.rect.y))
            return action
