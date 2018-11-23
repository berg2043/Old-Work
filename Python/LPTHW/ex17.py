from sys import argv
#from os.path import exists

script, from_file, to_file = argv

#print ('Copying from %s to %s' %(from_file, to_file))

#we could do these two on one line, how: indata = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()

#print ('The input file is %d bytes long' % len(indata))

#print ('Does the output file exist? %r' % exists(to_file))
#print ('Ready, hit RETURN to continue, CTRL-C to abort.')
#input ()

out_file = open(to_file, 'w')
out_file.write(indata)

#print ('Alright, all done.')

out_file.close()
in_file.close()

#how short can you do it? 2 lines
#indata = open(input('From File? ')).read()
#out_file = open(input('To File? '), 'w').write(indata)