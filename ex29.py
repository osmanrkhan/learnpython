people = int(raw_input("How many people?"))
cats = int(raw_input("How many kitties?"))
dogs = int(raw_input("And dogs?"))

if people < cats:
	print "CATS EVERYWHERE! NO ONE WILL BE SPARED!"

if people > cats:
	print "PEOPLE EVERYWHERE! NATURE IS DONE FOR!"

if people < dogs:
	print "dogsS RULE THE EARTH"

if people > dogs:
	print "PEOPLE ENSLAVE ALL dogsS!"

dogs += 5

print "Now there are %d dogss." % dogs

if people >= dogs: 
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are dogs. All of them"






