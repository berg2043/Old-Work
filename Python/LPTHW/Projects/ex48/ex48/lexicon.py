# create lists containing words to be recognized
directions = ['north', 'south', 'east', 'west', 'up', 'down', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat', 'open']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

#create tupples to be used later
def create_tupple(word):
	
	universal = word.lower()
	
	if universal in directions:
		return('direction', word)
	
	elif universal in verbs:
		return('verb', word)
	
	elif universal in stop_words:
		return('stop', word)
	
	elif universal in nouns:
		return('noun', word)
	
	#test to see if the word isn't any of the above, if it's a number or else error
	else:
		try:
			return('number', int(word))
		except ValueError:
			return('error', word)

# splits sentences into words
def splitter(sentence):
	return sentence.split(" ")
	
	
# requirement, function called scan
def scan(user_input):
	words = splitter(user_input)
	return [create_tupple(word) for word in words]