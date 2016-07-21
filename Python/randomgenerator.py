print("Your top ten spirit animals are: ")

import random

adjectives = ["adventurous",
		  "excited",
		  "crazy",
		  "boudless",
		  "brave",
		  "cheerful",
		  "dynamic",
		  "fun",
		  "energetic",
		  "amused"]
		  
colors = ["red",
		  "orange",
		  "yellow",
		  "green",
		  "blue",
		  "purple",
		  "pink",
		  "brown",
		  "black",
		  "white"]

animals = ["dog",
		  "ant",
		  "cat",
		  "monkey",
		  "tiger",
		  "cheetah",
		  "giraffe",
		  "dolphin",
		  "lion",
		  "elephant"]

for i in range(10):	
	animals_length = len(animals)
	colors_length = len(colors)
	adjectives_length = len(adjectives)
	random_index = random.randint(0,adjectives_length-1)
	random_index_2 = random.randint(0,colors_length-1)
	random_index_3 = random.randint(0,animals_length-1)
	print(adjectives[random_index] + " " + colors[random_index_2] + " " + animals[random_index_3])  
	
	
	


