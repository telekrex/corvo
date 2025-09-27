import pygame

class Line:

    def __init__(self, surface, position_x, position_y, size_x, color):
        self.surface = surface
        self.position_x = position_x
        self.position_y = position_y
        self.size_x = size_x
        self.color = color
        self.rect = pygame.Rect(
            self.position_x,
            self.position_y,
            self.size_x,
            1)
        
        self.rect_glow_bottom_1 = pygame.Rect(
            self.position_x,
            self.position_y -1,
            self.size_x,
            1)
        
        self.rect_glow_bottom_2 = pygame.Rect(
            self.position_x,
            self.position_y -2,
            self.size_x,
            1)

        self.rect_glow_top_1 = pygame.Rect(
            self.position_x,
            self.position_y + 1,
            self.size_x,
            1)

        self.rect_glow_top_2 = pygame.Rect(
            self.position_x,
            self.position_y + 2,
            self.size_x,
            1)

    def get_glow_color(self, amount=0.5):
        return (self.color[0] * amount, self.color[1] * amount, self.color[2] * amount)


    def draw(self):
        pygame.draw.rect(
            self.surface,
            self.color,
            self.rect,
            0,
            0)
        
        pygame.draw.rect(
            self.surface,
            self.get_glow_color(amount=0.4),
            self.rect_glow_bottom_1,
            0,
            0)
        
        pygame.draw.rect(
            self.surface,
            self.get_glow_color(amount=0.1),
            self.rect_glow_bottom_2,
            0,
            0)

        pygame.draw.rect(
            self.surface,
            self.get_glow_color(amount=0.4),
            self.rect_glow_top_1,
            0,
            0)
        
        pygame.draw.rect(
            self.surface,
            self.get_glow_color(amount=0.1),
            self.rect_glow_top_2,
            0,
            0)