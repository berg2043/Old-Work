from nose.tools import *
from ex48 import lexicon
from ex48 import parser
# test components i guess
def test_splitter():
	words = 'fuck me dude'
	assert_equal(lexicon.splitter(words), ['fuck', 'me', 'dude'])

def test_tupples():
	word = 'go'
	assert_equal(lexicon.create_tupple(word), ('verb', 'go'))
	


# the function should be able to scan the word north an return the tupple
# direction, north
def test_direction():
	assert_equal(lexicon.scan("north"), [('direction', 'north')])
	result = lexicon.scan("north south east")
	assert_equal(result, [('direction', 'north'),
						  ('direction', 'south'),
						  ('direction', 'east')])

# the function should be able to scan the word go and return the tupple
# verb, go						  
def test_verbs():
	assert_equal(lexicon.scan("go"), [('verb', 'go')])
	result = lexicon.scan("go kill eat")
	assert_equal(result, [('verb', 'go'),
						  ('verb', 'kill'),
						  ('verb', 'eat')])

def test_stops():
	assert_equal(lexicon.scan("the"), [('stop', 'the')])
	result = lexicon.scan("the in of")
	assert_equal(result, [('stop', 'the'),
						  ('stop', 'in'),
						  ('stop', 'of')])

						  
def test_numbers():
	assert_equal(lexicon.scan("1234"), [('number', 1234)])
	result = lexicon.scan("3 91234")
	assert_equal(result, [('number', 3),
						  ('number', 91234)])
						
	
def test_erros():
	assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
	result = lexicon.scan("bear IAS princess")
	assert_equal(result, [('noun', 'bear'),
						  ('error', 'IAS'),
						  ('noun', 'princess')])

# this also tests that lexicon is shooting shit out as you'd expect
# not sure how to test if word_list but it looks like it should always be true lol
def test_peak():
	assert_equal(parser.peak(lexicon.scan('north')), 'direction')
	assert_equal(parser.peak(lexicon.scan('bear')), 'noun')
	assert_equal(parser.peak(lexicon.scan('go')), 'verb')
	assert_equal(parser.peak(lexicon.scan('ASD')), 'error')
	assert_equal(parser.peak(lexicon.scan('1')), 'number')
	assert_equal(parser.peak(lexicon.scan('north south east')), 'direction')
	
def test_match():
	assert_equal(parser.match(lexicon.scan('north'), 'direction'), ('direction', 'north'))
	assert_equal(parser.match(lexicon.scan('north'), 'verb'), None)

# i'm thinking i'll have to test this as a part of the parse testing and not alone
#def test_skip():
#	assert_equal(parser.skip(lexicon.scan('north'), 'direction'), None)
#	assert_equal(parser.skip(lexicon.scan('north'), 'stop'), ('direction', 'north'))

def test_parse_verb():
	assert_equal(parser.parse_verb(lexicon.scan('go')), ('verb', 'go'))
	assert_raises(parser.ParserError, parser.parse_verb, lexicon.scan('north'))
	assert_equal(parser.parse_verb(lexicon.scan('the go')), ('verb', 'go'))
	assert_equal(parser.parse_verb(lexicon.scan('the the go')), ('verb', 'go'))
	assert_raises(parser.ParserError, parser.parse_verb, lexicon.scan('the the north go'))

def test_parse_object():
	assert_equal(parser.parse_object(lexicon.scan('north')), ('direction', 'north'))
	assert_raises(parser.ParserError, parser.parse_object, lexicon.scan('go'))
	assert_equal(parser.parse_object(lexicon.scan('the north')), ('direction', 'north'))
	assert_equal(parser.parse_object(lexicon.scan('the the north')), ('direction', 'north'))
	assert_raises(parser.ParserError, parser.parse_object, lexicon.scan('the the go north'))
	assert_equal(parser.parse_object(lexicon.scan('bear')), ('noun', 'bear'))
	
def test_parse_subject():
	assert_equal(parser.parse_subject(lexicon.scan('go north'), ('noun', 'player')), ('player', 'go', 'north'))

def test_parse_sentence():
	assert_equal(parser.parse_sentense(lexicon.scan('go north')), ('player', 'go', 'north'))
	assert_equal(parser.parse_sentense(lexicon.scan('bear go north')), ('bear', 'go', 'north'))
	assert_raises(parser.ParserError, parser.parse_sentense, lexicon.scan('fuck all shit'))
	assert_raises(parser.ParserError, parser.parse_sentense, lexicon.scan('5 bear go north'))