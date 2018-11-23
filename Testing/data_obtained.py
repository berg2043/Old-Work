# this is me figuring out how to extract the header data in a useable form from
# a GA result. it's largely unecessary as you specify what data you want in
# what order when you write the script to begin with. it's probably a good
# idea to put a prompt in the code to remind you to rename the columns when you
# change the information you are pulling.

# this is used to treat the code i'll be optaining as code and not a string
import ast

import pandas as pd

import numpy as np

# i stored the output from a result pull in this txt file, so i need to retrieve it
obtained = open('data_obtained.txt', 'r')

a = obtained.read()

d = ast.literal_eval(a)

# this was to visualize what was in the results file, it's muted because i wanted
# to keep it around to know my thought process
#for z , a in d.items():
#	print(z+"\t", a)

headers = []

for n in d.get('columnHeaders'):
	headers.append(n.get('name'))

df = pd.DataFrame(d.get('rows'), columns = headers) # columns = d.get('columnHeaders'))

print(df)
