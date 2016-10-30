#makes all below part of function cheese and crackers. Whenever
#cheeseandcrackers is defined again with new values, all will appear
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "That's enough for a party!"
	print "Get a blanket. \n"


print "We can just give the function numbers directly:"
#Self-explanatory
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
#Made 2 numerical variables
amount_of_cheese = 10
amount_of_crackers = 50
#Keep in mind the amount variables are normal variables, not functions	
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do maths inside too:"
#Adds numbers inside function cheese_and_crackers
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
#Adds Variables made above to numbers and stuffs them in the function 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)