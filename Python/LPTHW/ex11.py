# python 3 uses input instead of raw_input. you can also just put the question 
# into input instead of the line about
print ('How old are you?'),
age = input()
print ('How tall are you?'),
height = input()
print ('How much do you weight?'),
weight = input()

#who the fuck says you're "blank" old... it's years old
print ('So, you\'re %r old, %r tall, and %r heavy.' %(
	age, height, weight))