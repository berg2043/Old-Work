tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"

fat_cat = '''
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

#testing stuff to see what it looks like
#didn't really do anything
print ('abcd\aefg')
#backspace, but idk why that's useful yet
print ('abcd\befg')
#random character
print ('abcd\fefg')
#random character
print ('abcd\vefg')
#didn't actually do anything... huh
print ('abcd \ooo efg')
# print ('abcd \xhh efg') #broken

#warning this runs forever so you need ^c
while True:
	for i in ['/','-','|','\\','|']:
		print ("%s\r" %i,)