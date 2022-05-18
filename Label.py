import pygame


class Label:
    def __init__(self, text, width, height, pos, screen, font):
        self.text = text
        self.screen = screen
        self.gui_font = font
        
        self.top_rect = pygame.Rect(pos, (width, height))
        self.text_surf = self.gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        
    
    def draw(self):
        self.screen.blit(self.text_surf, self.text_rect)