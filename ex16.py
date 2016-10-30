from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL-C (^C)"
print "IF you do, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating file. Bye Bye Butterfree!"
target.truncate()
print "Now I'm gonna ask you for three lines"
line1 = raw_input("#1: ")
line2 = raw_input("#2: ")
line3 = raw_input("#3: ")

print "I'll write those to the file,"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n") 
target.write(line3)
target.write("\n")
print "Lemme see it."
target1 = open(filename)
x = target1.read()

print x

print "And finally, we close it."
target.close()