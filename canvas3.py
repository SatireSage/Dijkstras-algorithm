import pygame
import sys
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()

X_cords = []
Y_cords = []
counter = 0
White = (225, 225, 225)
line_width = 1
node_radius = 5
screen_width = 800
screen_height = 800
screen_size = [screen_width, screen_height]
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Visualizer")

Running = True
while Running:
    x, y = pygame.mouse.get_pos()

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif events.type == pygame.MOUSEBUTTONDOWN:
            X_cords.append(x)
            Y_cords.append(y)
            pygame.draw.circle(screen, White, (x, y), node_radius)
            if len(X_cords) > 1 and len(Y_cords) > 1:
                start = (X_cords[counter], Y_cords[counter])
                end = (X_cords[counter+1], Y_cords[counter+1])
                pygame.draw.line(screen, White, start, end, line_width)
                counter += 1
            if len(X_cords) == 5 and len(Y_cords) == 5:
                start = (X_cords[counter], Y_cords[counter])
                end = (X_cords[0], Y_cords[0])
                pygame.draw.line(screen, White, start, end, line_width)
                pygame.display.update()
                Running = False
    pygame.display.update()

# click = input("Press")