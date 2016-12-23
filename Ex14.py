from sys import argv
script, user_name = argv
prompt = '> '
print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions." )
print ("Do you like me %s?" % user_name)
likes = input(prompt)
print ("What kind of computer do you have? %s" % user_name)
computer = input(prompt)
print ("Which computer game do you like %s?" % user_name)
game = input(prompt)
print ("How many times did you win? %s?" % user_name)
times = input (prompt)
print ("""
Alright, so you said %r about liking me.
You have a %r computer. Nice.
And you like %r, that's cool. Warcraft III is my favourite game.
You won %r times! You are so great, however, I never win.
""" % (likes, computer, game, times))