print "You enter a dark room with two doors. Do you go to #1 or #2?"

door = raw_input("Well? ")

if door == "1":
	print "There is a giant bear eating a cheesecake. Either: "
	print " 1. Take his cake."
	print "2. Scream at the bear."
	print "The hidden third option. To do nothing at all"

	bear = raw_input("Whatchu gonna do?")

	if bear == "1":
		print "He bites off your head." 
		print "Try again?"
		
		decision1 = raw_input("Y/N?")
		
		if decision1 == "Y":
			print "Type clear, hit UP arrow key twice then enter."
		if decision1 ==  "N":		
			print "Then get lost."
	elif bear == "2":
		print "He screams in terror back and you die of fright."
		print "Try again?"
		decision2 = raw_input("Y/N?")
		
		if decision2 == "Y":
			print "Type clear, hit UP arrow key twice then enter."
		if decision2 ==  "N":		
			print "Then get lost."

	else:
		print "Well doing %s is probably better. Bear flees." % bear

elif door == "2":
	print "You stare into the endless abyss that is Cthulu's retina."
	print "1. Blueberries?"
	print "2. Yellowjacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("YAHHAHHA????")

	if insanity == "1" or insanity == "2":
		print "Your body survives thanks to a brain of mush. Nice!"
		print "Try again?"
		decision3 = raw_input("Y/N?")
		
		if decision3 == "Y":
			print "Type clear, hit UP arrow key twice then enter."
		if decision3 ==  "N":		
			print "Then get lost."
	else: 
		print "Your eyes rot and your brain flows out your nose. Nice!"
		print "Try again?"
		decision4 = raw_input("Y/N?")
		
		if decision4 == "Y":
			print "Type clear, hit UP arrow key twice then enter."
		if decision4 ==  "N":		
			print "Then get lost."
else:
	print "You get a brain aneurysm and die. Nice! "
	print "Try again?"
	decision5 = raw_input("Y/N?")
		
	if decision5 == "Y":
		print "Type clear, hit UP arrow key twice then enter."
	else:		
		print "Then get lost."





















