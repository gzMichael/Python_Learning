print ("How old are you?",end='')
#Python 3里面，只有input()
#age = raw_input()
age = input()
print ("How tall are you?",end='')
#height = raw_input()
height = input()
print ("How much do you weigh?",end='')
#weight = raw_input()
weight = input()
print ("So, you're %r old, %r tall and %r heavy." % (
age, height, weight))
print ("So, you're %s old, %s tall and %s heavy." % (
age, height, weight))