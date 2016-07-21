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
ORANGE = (255, 140, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")

image = pygame.image.load("winter-polar-backgrounds-wallpapers.jpg")
image = pygame. transform.scale(image,size)
class SnowFlake():
	'''
	This class will be used to create the SnowFlake Objects.
	It takes: 
		size - an integer that tells us how big we want the snowflake
		position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
		wind - a boolean that lets us know if there is any wind or not.	 
	'''

	def __init__(self, size, position, wind=False):
		self.size = size
		self.position = position
		self.wind = wind
	
	def fall(self, speed):
		"""
		Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
		A positive integer will have the snowflake falling down the screen. 
		A negative integer will have the snowflake falling up the screen. 
		
		If wind = True
			- the x direction of the snowflake changes
		"""

		self.position[1] += speed
		if self.wind == True:
		   self.position[0] += int(speed/2)
	def draw(self):
		"""
		Uses pygame and the global screen variable to draw the snowflake on the screen
		"""
		global screen
		global WHITE
		pygame.draw.circle(screen, WHITE, self.position, self.size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
speed = 1


#INITIALIZE YOUR SNOWFLAKE HERE! 

# Snow List
snow_list = []


# -------- Main Program Loop -----------

while not done:
	# --- Main event loop
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
   
		
		
	# --- Game logic should go here

	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	#screen.fill(BLACK)
	screen.blit(image, [0,0])  
	# --- Drawing code should go here
	#screen size(700, 500)
	pygame.draw.circle(screen, ORANGE, [313,387], 5)#feet
	pygame.draw.circle(screen, ORANGE, [329,387], 5)#feet
	pygame.draw.circle(screen, BLACK, [320,380], 11)#penguin body
	pygame.draw.circle(screen, WHITE, [320,375], 7)#penguin body
	pygame.draw.circle(screen, BLACK, [320,370], 7)#penguin head
	pygame.draw.circle(screen, ORANGE, [320,371], 1)#beak
	pygame.draw.circle(screen, BLUE, [315,368], 2)#eyes
	pygame.draw.circle(screen, BLUE, [324,368], 2)#eyes
	
	
	# Begin Snow
	
	z = 0
	for i in snow_list:
		snow_list[z].draw()
		snow_list[z].fall(random.randint(5,60))
		z += 1		
	snow_list.append(SnowFlake(random.randint(5,10), [random.randint(10,700),random.randint(0,50)], wind=True))





	# End Snow
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
