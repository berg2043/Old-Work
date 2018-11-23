from sys import argv

script, filename = argv

print ('We\'re going to erase %r.' %filename)
print ('If you don\'t want that, hit CTRL-C (^C).')
print ('If you do want that, hit RETURN.')

input('?')

print ('Opening the file..')
target = open(filename, 'r') #changed w to r

#added this
print ('Here\'s what it said')
print (target.read())
target.close()
target = open(filename, 'w')

print ('Truncating the file. Goodbye!')
#this is redundant because w truncates
target.truncate()

print ('Now I\'m going to ask you for three lines.')

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print ('I\'m going to write these to the file.')

#added this
rtrn = '\n'
target.write('%s%s%s%s%s%s' %(line1, rtrn, line2, rtrn, line3, rtrn))

#disabled this
#target.write(line1)
#target.write('\n')
#target.write(line2)
#target.write('\n')
#target.write(line3)
#target.write('\n')

#added this
print ('Here\'s what it now says')
target.close()
target = open(filename, 'r+')
print (target.read())

print('And finaly, we close it')
target.close()

#spoiler alert, use while for doing both reading and writing otherwise it's 
#bulky