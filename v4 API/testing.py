## This was to figure out how the hell to make a dataframe lol


import pandas as pd

import numpy as np

import ast

file_object = open ('fuck.txt', 'r')

a = file_object.read()

b = ast.literal_eval(a)

c = b['reports']

#currently trying to figure out adding things to the data frame

print('Column headers in df')

for d in b["reports"]:
	global df
	df = pd.DataFrame(columns=(d['columnHeader']['dimensions']))
	for e in (d['columnHeader']['metricHeader']['metricHeaderEntries']):
		df = pd.concat([df,pd.DataFrame(columns=([e['name']]))])
#	for g in d['data']['rows']:
#		df = pd.concat([df,pd.DataFrame((g['dimensions']))])
#		for h in g['metrics']:
#			df = df.append(h['values'])

print(df)

print('\nlists')

for l in b['reports']:
	global list
	list = l['columnHeader']['dimensions']
	for m in l['columnHeader']['metricHeader']['metricHeaderEntries']:
		list.append(m['name'])
	global datas
	datas = []
	for q in l['data']['rows']:
		for y in q['dimensions']:
			datas.append(y)
		for t in q['metrics']:
			for u in t['values']:
				datas.append(u)
print(list)
print(datas)

df1= pd.DataFrame(np.array(datas).reshape(int(len(datas)/len(list)),len(list)), columns=list)

df1['ga:date'] = pd.to_datetime(df1['ga:date'].astype(str)).dt.strftime('%m/%d/%y')

print('\n',df1)

#df = pd.DataFrame(columns=['A'], index = False)

#print('\nColumn and Metric headers')

#for d in b["reports"]:
#	print(d['columnHeader']['dimensions'])
#	for e in (d['columnHeader']['metricHeader']['metricHeaderEntries']):
#		print(e['name'])

#print('\ndata')	
		
#for f in b["reports"]:
#	print(f['data']['rows'])
#	for g in f['data']['rows']:
#		print(g['dimensions'])
#		for h in g['metrics']:
#			print(h['values'])
#print(b["reports"]['columnHeader'])

#df = pd.DataFrame(b)
#df.columns = ['source', 'medium', 'sessions', 'bounces']

#{'reports': [{'columnHeader': {'dimensions': ['ga:date', 'ga:source', 'ga:medium'], 'metricHeader': {'metricHeaderEntries': [{'name': 'ga:sessions', 'type': 'INTEGER'}, {'name': 'ga:bounces', 'type': 'INTEGER'}]}}, 'data': {'rows': [{'dimensions': ['20180618', '(direct)', '(none)'], 'metrics': [{'values': ['1', '0']}]}, {'dimensions': ['20180618', 'google', 'organic'], 'metrics': [{'values': ['1', '1']}]}], 'totals': [{'values': ['2', '1']}], 'rowCount': 2, 'minimums': [{'values': ['1', '0']}], 'maximums': [{'values': ['1', '1']}]}}]}