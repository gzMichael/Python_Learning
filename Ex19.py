#定义函数cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#打印cheesses数量（输入参数1）
	print ("You have %d cheeses!" % cheese_count )
	#打印crackers数量（输入参数2）
	print ("You have %d boxes of crackers!" % boxes_of_crackers )
	#打印文字
	print ("Man that's enough for a party!" )
	#打印文字
	print ("Get a blanket.\n")
	
#打印文字	
print ("We can just give the function numbers directly:")	
#直接输入具体常量调用
cheese_and_crackers(20, 30)

#打印文字	
print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#通过输入变量调用
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#打印文字	
print ("We can even do math inside too:")
#通过常量算术式调用
cheese_and_crackers(10 + 20, 5 + 6)

#打印文字
print ("And we can combine the two, variables and math:")
#通过变量算术式调用
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)