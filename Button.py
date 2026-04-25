
import pygame
pygame.init()

class Button:
    def __init__(self, screen, img, x, y, centered = False):
        self.img = img 
        self.screen = screen
        self.clicked = False
        if centered:
            self.rect = self.img.get_rect(center=(x, y))
        
        else:
            self.rect = self.img.get_rect(topleft = (x, y))

    def draw(self):
        action = False
        self.screen.blit(self.img, self.rect) 
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False # self.clicked prevents repeat firing by the mouse being held done

        return action