import pygame
import projects

class Button:

    def __init__(self, surface, text, position_x, position_y, size_x, size_y, color_normal, color_highlighted, text_color_normal, text_color_highlighted, text_size=18):
        self.surface = surface
        self.position_x = position_x
        self.position_y = position_y
        self.text = text
        self.size_x = size_x
        self.size_y = size_y
        self.color_normal = color_normal
        self.color_highlighted = color_highlighted
        self.text_color_normal = text_color_normal
        self.text_color_highlighted = text_color_highlighted
        self.focused = False
        self.clicked = False
        self.font = pygame.font.Font('DinaRemasterCollection.ttc', text_size)
        self.rect = pygame.Rect(
            self.position_x,
            self.position_y,
            self.size_x,
            self.size_y)
    
    def click(self, project, tag, button_type, was_ctrl_pressed):
        print(f'You clicked button {project}')
        print(f'Button type: {button_type}')
        if button_type == 'project':
            if was_ctrl_pressed:
                projects.open_project_corvo(project)
            else:
                projects.open_project_location(project)
        elif button_type == 'tag':
            print(f'tag: {tag}')

    def mouse_event(self, event, project, tag, button_type, was_ctrl_pressed):
        if self.rect.collidepoint(event.pos):
            if self.focused:
                self.click(project, tag, button_type, was_ctrl_pressed)

    def draw(self):
        
        # hover
        self.mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.mouse):
            self.focused = True
            # pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            self.focused = False
            # pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        # draw
        pygame.draw.rect(
            self.surface,
            self.color_highlighted if self.focused else self.color_normal,
            self.rect,
            0,
            4)
        
        self.text_surface = self.font.render(
            self.text,
            True,
            self.text_color_highlighted if self.focused else self.text_color_normal)

        self.text_position_x = self.position_x + ((self.size_x/2) - (self.text_surface.get_width()/2))
        self.text_position_y = self.position_y + ((self.size_y/2) - (self.text_surface.get_height()/2))
        self.surface.blit(self.text_surface, (self.text_position_x, self.text_position_y))