# class—Tell Python to make a new kind of thing.
# object—Two meanings: the most basic kind of thing, and any instance of some thing.
# instance—What you get when you tell Python to create a class.
# def—How you defi ne a function inside a class.
# self—Inside the functions in a class, self is a variable for the instance/object being accessed.
# inheritance—The concept that one class can inherit traits from another class, much like you and your parents.
# composition—The concept that a class can be composed of other classes as parts, much like how a car has wheels.
# attribute—A property classes have that are from composition and are usually variables.
# is- a—A phrase to say that something inherits from another, as in a “salmon” is- a “fi sh.”
#has- a—A phrase to say that something is composed of other things or has a trait, as in “a salmon has- a mouth.”

# oop_test.py

import random
from urllib.request import urlopen #had to change urllib to urllib.request
import sys

# custom function to fix these word issues	
def fix(words_to_fix):
	thing = words_to_fix.replace(', ', '').replace('b\'','',1).replace('\'','')
	return thing

WORD_URL = 'http://learncodethehardway.com/words.txt'
WORDS =[]

PHRASES = {
	'class %%%(%%%):':
	  'Make a class named %%% that is-a %%%.',
	'class %%%(object):\n\tdef __init__(self,***)' :
	  'Class %%% has-a __init__ that takes self and *** parameters.',
	'class %%%(object):\n\tdef ***(self, @@@)':
	  'class %%% has-a function named *** that takes self and @@@ parameters.',
	'*** = %%%()':
	  'Set *** to an instance of clasee %%%.',
	'***.***(@@@)':
	  'From *** get the *** function, and call it with paremeters self, @@@.',
	'***.*** = \'***\'':
	  'From *** get the *** attribute and set it to \'***\'.'
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == 'english':
	PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())
	

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
	 random.sample(WORDS, snippet.count('%%%'))]
	other_names = random.sample(WORDS, snippet.count('***'))
	results = []
	param_names = []
	
	for i in range(0, snippet.count('@@@')):
		param_count = random.randint(1,3)
		param_names.append(', '.join(str(random.sample(WORDS, param_count)))) #had to turn the sample of words into a string
		
	for sentence in snippet, phrase:
		result = sentence[:]
		
		#fake class names
		for word in class_names:
			result = result.replace('%%%', fix(str(word)), 1) #had to turn word into a string
			
		# fake other names
		for word in other_names:
			result = result.replace('***', fix(str(word)), 1) #had to turn word into a string
		
		# fake parameter lists
		for word in param_names:
			result = result.replace('@@@', fix(str(word)), 1) #had to turn word into a string
		
		results.append(result)
		
	return results
	
# keep going until they hit CTRL-D (doesn't work had to CTRL-C)
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(list(snippets))
		
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
			
			print(question)
			
			input('> ')
			print('ANSWER: %s\n\n' % answer)
except EOFError:
	print('\nBye')
	
