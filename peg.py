import pygame

# 50 Shades of Grey: take away 49 shades
WHITE = (255, 255, 255)


# Peg definition
class Peg(pygame.Surface):
    def __init__(
            self,
            id,
            screen,  # the peg will draw itself on this surface
            location,  # The peg will be centered on this location
            action,
            size=(20, 20),  # size of the peg
    ):
        super().__init__(size)
        self.id = id
        self.screen = screen

        # Converts image to surface, then takes out every white pixel
        self.image = pygame.image.load("peg.bmp").convert()
        self.image.set_colorkey(WHITE)

        self.rect = self.get_rect(center=location)
        self.mouse_click_callback = action

    def draw(self, location):
        """Draw the peg on the screen"""
        self.screen.blit(self.image, self.rect)

    def mouse_click_callback(self, event):
        """When a mouse click occurs on this hole, this function is called. It then calls
           the user-specified function for action"""
        pe = Peg.Event(self, event)
        self.mouse_click_call_back_(pe, self.id)



