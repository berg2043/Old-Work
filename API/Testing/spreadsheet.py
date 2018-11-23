## This was to figure out how the hell to make a dataframe lol


import pandas as pd

import numpy as np

import ast

file_object = open ('testing1.txt', 'r')

## this is me figuring out how the hell to get the text correctly lol
## a holds the file, while b tries to split it (poorly), c copy pastes it
## and d finally correctly does it treating it like code and not a string
## unsure if i could have just used a parser, but ast worked lol

a = file_object.read()

b = a.split(',')

c = [['(direct)', '(none)', '157', '108'], ['alumaxshowerdoor.com', 'referral', '1', '0'], ['aqualityglassco.com', 'referral', '4', '4'], ['bing', 'cpc', '75', '35'], ['bing', 'organic', '15', '8'], ['duckduckgo.com', 'referral', '1', '1'], ['google', 'cpc', '308', '150'], ['google', 'organic', '192', '68'], ['local-biz.me', 'referral', '6', '2'], ['r.search.aol.com', 'referral', '6', '2'], ['searchencrypt.com', 'referral', '3', '3'], ['yahoo', 'organic', '9', '6'], ['zapmetasearch.com', 'referral', '1', '1']]

d = ast.literal_eval(a)

## use d because fuck a and b and c is just too long lol

##only use this if the headers are included in the rows of the file, which it wasn't
##df = pd.DataFrame(c[1:], columns = c[0])

df = pd.DataFrame(d)

df.columns = ['source', 'medium', 'sessions', 'bounces']

df.to_csv('results.csv', index = False)

print(df)


