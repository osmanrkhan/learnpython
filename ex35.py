#A GAME
from sys import exit

def gold_room():
	print "This room is full of gold. How much do you want?"# when gold_room() is invoked this prints, then

	choice = raw_input("Well? \n")                          # The user is prompted with Well? 
	if "0" in choice or "1" in choice:						# If the string the user writes contains the LETTER 0 or 1 then 
		how_much = int(choice)								# how_much is a variable that equals the integer form of the string the user wrote
	else:													# If it doesn't contain 0 or 1
		dead("Man, can you learn how to type a number?")	# You have invoked dead()[See below, ozz]

	if how_much < 500:										# If the integer value of the string the user wrote is less than 500,
		print "Nice, you're not greedy! You win!"			# That's printed
		exit(0)												# And exit command is invoked.
	else:													# If it's greater than or equal to 50,
		dead("Your greed is your undoing!")					# dead() is invoked		


def bear_room():											# bear_room is defined!
	print "There is a bear here."				
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False										# As I understand, bear_moved is a placeholder for a False value?

	while True:												# While apparently creates an infinte loop???
		choice = raw_input("> ")	

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.",)
		elif choice == "taunt bear" and not bear_moved:		# Understood half of this
			print "The bear has moved from the door. You can now go through it."
			bear_moved = True								# WHAT?
		elif choice == "taunt bear" and bear_moved:         # This is an acute confusion
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:			# About half again
			gold_room()	                                       
		else:                                                    
			print "What does that mean?!"                        


def cthulhu_room():
		print "Here you see the great evil Cthulhu!"
		print "He, it, whatever stares at you and you feel your brain turn to mush."
		print "Do you flee for your life or eat your head?"

		choice = raw_input("> ")

		if "flee" in choice:								# If the string flee is typed then
			start()											# You invoke the very beginning
		elif "head" in choice:								# If the string head is typed then
			dead("Well that was tasty!")							
		else:
			cthulhu_room()									# If you fail to do wither you start the room again.


def dead(why):												# why is a placeholder
	print why, "Now you're dead!"							# this will print whatever's b/w () and Now you're dead
	exit(0)													# exits the program

def start():					
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	choice = raw_input(">")

	if "left" in choice:
		bear_room()
	elif "right" in choice:
		cthulhu_room()
	else:
		dead("You stumble in circles till you starve.",)


start()