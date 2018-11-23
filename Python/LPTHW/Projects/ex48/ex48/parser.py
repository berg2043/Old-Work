#ex 40
class ParserError(Exception):
	pass

	
class Sentence(object):

	#def __init__(self, subject, verb, object):
		# remember we take ('noun', 'princess') tuples and convert them
		#self.subject = subject[1]
		#self.verb = verb[1]
		#self.object = object[1]
		
		
	#I assume there is some problem with 2.7 to 3 here so I added this and turned off that
	def work(subject, verb, object): 
		subject = subject[1]
		verb = verb[1]
		object = object[1]
		return (subject, verb, object)
	
def peak(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None
		
		
def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)
		
		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None
		
		
def skip(word_list, word_type):
	while peak(word_list) == word_type:
		match(word_list, word_type)
		

def parse_verb(word_list):
	skip(word_list, 'stop')
	
	if peak(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParserError('Expected a verb next.')
		
		
def parse_object(word_list):
	skip(word_list, 'stop')
	next = peak(word_list)
	
	if next == 'noun':
		return match(word_list, 'noun')
	if next == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expecting a noun or direction next.")
		
		
def parse_subject(word_list, subj):
	verb = parse_verb(word_list)
	obj = parse_object(word_list)
	
	return Sentence.work(subj, verb, obj)
	
def parse_sentense(word_list):
	skip(word_list, 'stop')
	
	start = peak(word_list)
	
	if start == 'noun':
		subj = match(word_list, 'noun')
		return parse_subject(word_list, subj)
	elif start == 'verb':
		# assume the subject is player then
		return parse_subject(word_list, ('noun', 'player'))
	else:
		raise ParserError("Must start with subject, object, or verb not: %s" % start)