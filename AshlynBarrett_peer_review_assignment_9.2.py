# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.
# Peer review: Ashlyn Barrett
# Reviewed on: 10/26/2022

import random
import time


def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''') 

	print()
	
def chooseCave():
    cave = '' 
	while cave != '1' and cave != '2': 
		print('Which cave will you go into? (1 or 2)')	
		cave = input()
		
	return caves #should say return cave 
	
def checkCave(chosenCave): #(choseCave) not chosencave
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3) #should be time.sleep(2) not (3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!' #should be print('Gobbles you down in one bite!')
		
playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y': #use playAgain == 'yes' or playAgain == 'y': 
	displayIntro()
	caveNumber = choosecave() #chooseCave() use correct type case
	checkCave(caveNumber)
	
	print('Do you want to play again? (yes or no)')
	playAgain = input() #this should be placed under the if statement print statement
	if playAgain == "no": #change "no" to 'no'
		print("Thanks for planing") #typo change from planing to playing
		#insert a break

