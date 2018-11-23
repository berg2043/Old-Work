from sys import argv
#you could replace argv by having filename = some input
script, filename = argv

#makes the file available for python
txt = open(filename)

print ('Here is your file %r:' %filename)
#reads that file and prints it. i'm guessing that it reads whatever is open
#since it lacks parameters
print (txt.read())

print ('Type the filename again:')
file_again = input('> ')

txt_again = open(file_again)

print (txt_again.read())

#don't forget to close shit when you're done with you or else you're a lazy POS
txt.close()
txt_again.close()

#you need to close the file open variable not the file itself. it's interesting