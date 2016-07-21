"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)



pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE

player_x = random.randint(0,100)
player_y = random.randint(0,100)

speed_x = random.randint(-10, 10)
speed_y = random.randint(-10, 10)

size = random.randint(20, 80)

bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True



	# --- Game logic should go here
	
	color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

	# makes circle glide with random speed
	player_x += speed_x
	player_y += speed_y
	if player_x > 700 or player_x < 1:
		speed_x = -speed_x
	if player_y > 500 or player_y < 1:
		speed_y = -speed_y
	
	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(bg_color)

	# --- Drawing code should go here

	pygame.draw.circle(screen, color, (player_x, player_y), size)

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(20)
# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
