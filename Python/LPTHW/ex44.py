# this is a lesson to teach about inheritance and composition, so far
# inheritance doesn't seem bad but i guess i'll get a stern warning lol

# Inheritance

class Parent(object):
	
	def override(self):
		print("PARENT override()")
		
	def implicit(self):
		print("PARENT implicit()")
		
	def altered(self):
		print("PARENT altered()")
		
class Child(Parent):
	
	def override(self):
		print("CHILD override()")
	#this only calls the parent for that brief moment. it does not overwrite the child	
	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super().altered() #in python 3 you can write it this way
		#super(Child, self).altered() #this is how you have to write it in 2.7
		print("CHILD, AFTER PARENT altered()")
		
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

#composition

#set up other class to be called later
class Other(object):
	
	def override(self):
		print("OTHER override()")
		
	def implicit(self):
		print("OTHER implicit()")
		
	def altered(self):
		print("OTHER altered()")
		
class Thing(object):
	
	#defines the other class as self.other
	def __init__(self):
		self.other = Other()
	
	#calls the other implicit so the Things implicit is just a copy of Other
	def implicit(self):
		self.other.implicit()
	
	def override(self):
		print("THING override()")
	
	def altered(self):
		print("THING, BEFORE OTHER altered()")
		self.other.altered()
		print("THING, AFTER OTHER altered()")

print("\n")
		
thing = Thing()
other = Other()

other.implicit()
thing.implicit()

other.override()
thing.override()

other.altered()
thing.altered()
