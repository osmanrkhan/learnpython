i = 2
numbers = []

while i < 1000000000000000000000000000000000000000000000000:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i * 2
	print "Numbers now:", numbers
	print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers: 
	print num

