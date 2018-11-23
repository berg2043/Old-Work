#i = 0
#numbers = []

#while i < 6:
#	print('at the top of i is %d' %i)
#	numbers.append(i)
#	
#	i += 1
#	print('Numbers now: ', numbers)
#	print('At the bottom i is %d' % i)
	
	
#print('The numbers: ')

#for num in numbers:
#	print(num)
numbers = []
i=0	
while i < 6:
	for n in range(0,6):
		numbers.append(n)
		i += 1
print(numbers)