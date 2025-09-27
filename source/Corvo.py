import pygame
import sys, os
import mach
import domains

print(f"Corvo operating from location: {os.getcwd()}")
DIR = os.getcwd()

os.environ["SDL_VIDEO_CENTERED"] = "1"  # Put it in the middle of user's screen
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Corvo")
clock = pygame.time.Clock()
window = pygame.display.set_mode((1000, 700))  # Fixed window size
# pygame_icon = pygame.image.load('Corvo.ico')
# pygame.display.set_icon(pygame_icon)


def clamp(value, minimum, maximum):
    return max(min(value, maximum), minimum)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
            update_list(tag)
            

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

from text import Text



# CONTROLS UI
controls = '''Click to open project's location, Ctrl+click to open project's .corvo file
Press / to open Corvo's domain config file
'''
controls_text = Text(window, controls, 20, 20, (100, 100, 100), size=14)

# CURRENT FILTER UI
current_filter = Text(window, 'Current filter: all', 20, 48, (100, 100, 100), size=14)

# Assembling the list of
# projects and tags
current_projects = []
tags = mach.tags
tags.append('all')
projects_buttons = []
tags_buttons = []

# Mapping locations
# of tag buttons
x_position = 20
x_spacing = 90
for tag in tags:
    tags_buttons.append(
        Button(
            window,
            f'{tag}',
            x_position,
            70, # Starting vertical position of tags list
            80, # Width of tag button
            28,
            color_normal=(60, 60, 60),
            color_highlighted=(217, 139, 50),
            text_color_normal=(180, 180, 180),
            text_color_highlighted=(250, 250, 250),
            text_size=14
        )
    )
    x_position += x_spacing


def update_list(filter='all'):
    global current_filter
    global current_projects
    global projects_buttons
    current_filter.text = f'Current filter: {filter}'
    projects_buttons = []
    current_projects = mach.get_filtered_entries(filter)
    y_position = 110 # Starting vertical position of projects list
    y_spacing = 34
    for entry in current_projects:
        projects_buttons.append(
            Button(
                window,
                f'{entry.name}   {entry.actions} actions {entry.thoughts} thoughts   [{entry.status}]',
                20,
                y_position,
                960,
                28,
                color_normal=(60, 60, 60),
                color_highlighted=(217, 139, 50),
                text_color_normal=(180, 180, 180),
                text_color_highlighted=(250, 250, 250),
                text_size=14)
            )
        y_position += y_spacing


# First load and update
update_list()


def draw_background():
    color1 = (5, 5, 5)      # Top color
    color2 = (95, 95, 95)   # Bottom color
    # Draw the gradient
    for y in range(700):
        # Interpolate between color1 and color2
        ratio = y / 1000
        interpolated_color = (
            int(color1[0] * (1 - ratio) + color2[0] * ratio),
            int(color1[1] * (1 - ratio) + color2[1] * ratio),
            int(color1[2] * (1 - ratio) + color2[2] * ratio),
        )
        pygame.draw.line(window, interpolated_color, (0, y), (1000, y))


def play_sound(sound_file, volume=1.0, pitch_scale=0.0):
    sound = pygame.mixer.Sound(f"{DIR}/{sound_file}")
    sound.set_volume(volume)
    sound.play()


current_cursor = None
ctrl_pressed = False


# ----------------------------------------
# Run the main loop, where we mostly just
# look at the keyboard input, and put it
# where it needs to go.
r = True
while r:
    draw_background()
    # Render the screen first, starting with
    # background color from theme
    clock.tick(300)  # 300 fps because hawt
    controls_text.draw()
    current_filter.draw()
    hovering_over_button = False
    mouse = pygame.mouse.get_pos()
    for button in tags_buttons:
        button.draw()
        if button.rect.collidepoint(mouse):
            hovering_over_button = True
    for button in projects_buttons:
        button.draw()
        if button.rect.collidepoint(mouse):
            hovering_over_button = True
    # After all buttons are drawn
    if hovering_over_button:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    # Look at input events:
    for event in pygame.event.get():
        # If user clicks the X, quit
        if event.type == pygame.QUIT:
            r = False
        # Anyway, continue to keyboard
        if event.type == pygame.KEYDOWN:
            # When user presses "Enter"
            if event.key == pygame.K_SLASH:
                domains.open_domains()
            if event.key == pygame.K_LCTRL:
                ctrl_pressed = True
                print('Ctrl pressed')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL:
                ctrl_pressed = False
                print('Ctrl released')
        # Mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, button in enumerate(projects_buttons):
                button.mouse_event(event, current_projects[index], tag='', button_type='project', was_ctrl_pressed=ctrl_pressed)
            for index, button in enumerate(tags_buttons):
                button.mouse_event(event, project=None, tag=tags[index], button_type='tag', was_ctrl_pressed=ctrl_pressed)
    # Finally, refresh the screen
    pygame.display.flip()
