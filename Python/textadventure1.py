start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''


print(start)
done = False
while not done:
	print("Type 'left' to go left or 'right' to go right.")
	user_input = input()
	if user_input == "left":
		print("You decide to go left and there is a giant, green troll, holding a wooden club with nails sticking out of it, in your way. Do you run away or fight?") # finished the story by writing what happens
		done_2 = False
		while not done_2:
			print("Type 'run' to run away or 'fight' to fight.")
			user_left = input()
			if user_left == "fight":
				print("There is a sword to one side of you and a wand to the other. Which one so you use against the troll?")
				done_3 = False
				while not done_3:
					print("Type 'sword' or 'wand'.")
					user_troll = input()
					if user_troll == "sword":
						print("The troll hits you on the head and you die.")
						done_3 = True
					elif user_troll == "wand":
						print("You defeat the troll, make it out of the maze, and go back to bed.")
						done_3 = True
				done_2 = True	
			elif user_left == "run":
				print("The troll laughs as you run away like a baby.")
				done_2 = True
		done = True
	elif user_input == "right":
		print("You choose to go right and you start walking down a swampy path. After a few minutes, you end up at a murky river. Do you swim across?") # finished the story writing what happens
		done_5 = False
		while not done_5:
			print("Type 'yes' or 'no'.")
			user_right = input()
			if user_right == "yes":
				print("The current is too strong and you die.")
				done_5 = True
			elif user_right == "no":
				print("You turn around and keep walking. You come across a candy-covered cabin with lollypops leading up to the enterance. Do you go inside?")
				done_4 = False
				while not done_4:
					print("Type 'yes' or 'no'.")
					user_cabin = input()
					if user_cabin == "yes":
						print("When you enter, you meet a friendly witch who gives you food and helps you find your way out.")
						done_4 = True
					elif user_cabin == "no":
						print("You get lost in the maze and die.")
						done_4 = True
				done_5 = True		
		done = True	
		

