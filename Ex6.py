#定义X，字符放入字符处：1
x = "There are %d types of people." % 10
#定义binary
binary = "binary"
#定义do_not
do_not = "don't"
#定义Y，字符放入字符处：2
y = "Those who know %s and those who %s." % (binary, do_not)
#打印X
print (x) 
#打印y
print (y)
#打印文字，调用X，字符放入字符处：3
print ("I said: %r." % x )
#打印文字，调用y，字符放入字符处：4
print ("I also said: '%s'." % y)
#定义hilarious
hilarious = True
#定义joke_evaluation，字符放入字符处：5
joke_evaluation = "Isn't that joke so funny?! %r"
#打印joke_evaluation
print (joke_evaluation % hilarious)
#定义w
w = "This is the left side of..."
#定义e
e = "a string with a right side."
#打印w+e
print (w + e)