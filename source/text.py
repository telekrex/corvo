import pygame

class Text:

    def __init__(self, surface, text, position_x, position_y, color, size=18, max_lines=26, max_length=300):
        self.surface = surface
        self.position_x = position_x
        self.position_y = position_y
        self.text = text
        self.color = color
        self.size = size
        self.max_lines = max_lines
        self.max_length = max_length
        self.font = pygame.font.Font('DinaRemasterCollection.ttc', self.size)

    def draw(self):
        if '\n' in self.text:
            row = 0
            for line in self.text.split('\n' ):
                if row < self.max_lines:
                    self.block = self.font.render(line[:self.max_length], True, self.color)
                    self.surface.blit(self.block, (self.position_x, self.position_y + (self.size * row)))
                    row += 1
        else:
            self.block = self.font.render(self.text[:self.max_length], True, self.color)
            self.surface.blit(self.block, (self.position_x, self.position_y))