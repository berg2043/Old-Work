indata = open(input('From File? ')).read()
out_file = open(input('To File? '), 'w').write(indata)