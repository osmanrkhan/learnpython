from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "Lemme ask you sumthing."
print "Do you like me %r?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?" 
computer = raw_input(prompt)

print """
\tAlright. So you said %r about liking me.
\tYou live in %r. Not sure where that is.
\tAnd you have a %r computer. Nice.
""" % (likes, lives, computer)