import pygame
import pygame_textinput

from Button import Button
from Label import Label
 
class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.clock = None
        self.size = self.weight, self.height = 640, 400
        self.title = "Character Selection"
        self.bg_loc = "assets/images/charSelBg.jpg"
        self.image = None
        
 
    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.font = pygame.font.Font(None, 30)
        self.titleFont = pygame.font.Font(None, 40)
        
        self.clock = pygame.time.Clock()

        # Pygame now allows natively to enable key repeat:
        pygame.key.set_repeat(200, 25)
        
        pygame.display.set_caption(self.title)
        
        self.image = pygame.image.load(self.bg_loc).convert()
        self.screen.blit(self.image, (0, 0))
        
        self.titleBox = Label("Character Selection", 300, 70, (170, 10), self.screen, self.titleFont)
        
        self.player1Sel = Button("Hello", 150, 150, (110, 105),5, self.screen, self.font)
        self.player2Sel = Button("Hello", 150, 150, (380, 105),5, self.screen, self.font)
            
        self.manager = pygame_textinput.TextInputManager(validator = lambda input: len(input) <= 5)
        self.manager1 = pygame_textinput.TextInputManager(validator = lambda input: len(input) <= 5)
        
        self.player1NameBox = pygame_textinput.TextInputVisualizer(manager=self.manager, cursor_width=4, cursor_blink_interval=400, antialias=False)
        self.player2NameBox = pygame_textinput.TextInputVisualizer(manager=self.manager1, cursor_width=4, cursor_blink_interval=400, antialias=False)

        self.Next = Button("Proceed", 130, 40, (490, 340),5, self.screen, self.font)
    
        return self.screen
 
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            

    def on_all_events(self, events):
        self.player1NameBox.update(events)
        self.player2NameBox.update(events)
        
            
    def on_loop(self):
        pass
 
    
    def on_render(self):
        self.screen.blit(self.image, (0, 0))
        
        self.titleBox.draw()
        
        self.player1Sel.draw()
        self.player2Sel.draw()
        self.Next.draw()
        
        self.screen.blit(self.player1NameBox.surface, (110, 270))
        self.screen.blit(self.player2NameBox.surface, (380, 270))
                
        pygame.display.update()
        self.clock.tick(30)
 
    
    def on_cleanup(self):
        pygame.quit()
        
        
    def change_image(self, index):
        pass
        
 
    def on_execute(self):
        if self.on_init() is None:
            self._running = False
 
        while( self._running ):
            events = pygame.event.get()
            
            self.on_all_events(events)
            
            for event in events:
                self.on_event(event)
            
            self.on_loop()
            self.on_render()
        
        self.on_cleanup()
 
 
if __name__ == "__main__" :
    root = App()
    root.on_execute()
