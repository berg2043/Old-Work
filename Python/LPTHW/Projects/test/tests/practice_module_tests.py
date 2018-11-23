from nose.tools import *
import practice_module

def setup():
	print("SETUP")

def teardown():
	print("TEAR DOWN!")
	
def test_basic():
	print("I RAN")