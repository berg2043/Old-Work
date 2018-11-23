#defines x as the joke
x = 'There are %d types of people.' %10
#definition of binary
binary = 'binary'
#definition of don't
do_not = 'don\'t'
#definition of the punch line
y = 'Those who know %s and those who %s.' %(binary, do_not)

#printing the joke
print (x)
print (y)

#printing the joke explaination
print ('I said: %r.' %x)
print ('I also said: \'%s\'.' %y)

#self deprecation
hilarious = False
joke_evaluation = 'isn\'t that joke so funny?! %r'

#printing the self deprecation
print (joke_evaluation %hilarious)

#strings that get stitched
w = 'This is the left side of...'
e = 'a string with a right side.'

#adding the strings
print (w + e)