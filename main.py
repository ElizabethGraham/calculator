import pygame
import sys

pygame.init()

white = (255, 255, 255)  # Window background color
medium_grey = (170, 170, 170)
dark_grey = (100, 100, 100)
width, height = 400, 600  # Window dimensions

screen = pygame.display.set_mode((width, height))  # Initialize screen
screen.fill(white)  # Fill the background layer with white
pygame.display.set_caption("Calculator")  # Set the title of the window
pygame.display.flip()

# Width and height as variables
width = screen.get_width()
height = screen.get_height()

user_font = pygame.font.SysFont('Corbel', 35)  # Set font
text = user_font.render('quit', True, white)


def create_buttons():
    # setting up a 3 * 3 board in canvas
    board = [[None] * 3, [None] * 3, [None] * 3]


running = True
while running:
    for event in pygame.event.get():
        # If the user quits, end the while loop
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        mouse = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()

        """
        # If mouse is hovered on a button it
        # changes to lighter shade
        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, medium_grey, [width / 2, height / 2, 140, 40])
        else:
            pygame.draw.rect(screen, dark_grey, [width / 2, height / 2, 140, 40])

        # superimposing the text onto our button
        screen.blit(text, (width / 2 + 50, height / 2))
        """
        # updates the frames of the game
        pygame.display.update()
        pygame.display.flip()
