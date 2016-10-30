name = 'Osman Rawr Meist'
age =  14 # spins around the sun
height = 70.50 # inches
weight = 60
eyes = 'Brown'
teeth = 'Whitish'
hair = 'Black'
inch = height
cm = 2.540
heightconvert = height * cm
pounds = 2.2
weightconvert = weight * pounds

print "Let's talk about %s." %  name
print "He's %d inches tall." % height
print "In cm, that's %d." % heightconvert
print "He's about %d kgs heavy." % weight
print "Actually that's really heavy, and in pounds, that's about %d." % heightconvert
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are almost always kind of usually %s." % teeth

# This line is tricky, try to get it right
print "If I add %d, %d, and %d, I get %d." % (
   age, height, weight, age + height + weight)

