# I'm supposed to make a game, that's dumb as hell
class player(object):
	pass
gender = ""
race = ""
kit = ""

def start():
	print("-----------------\
	\nWelcome to the character creator. This is a one way creation\
	\nprocess and there is no way to go back and change what you've\
	\nalready selected.\n-----------------.")
	genderselection()

	
def genderselection():
	
	global gender
	genders = {1: "Male", 2: "Female"}
	choice = input("What gender is your character? \n1:Male\n2:Female\n")
	
	if choice == "1" or choice == "2":
		gender = genders[int(choice)]
		raceselection()
	
	else:
		print("-----------------\nI'm sorry, that was not a valid selection\
		\n-----------------")
		genderselection()

		
def raceselection():
	
	global race
	races = {1: "Human", 2: "Elf", 3: "Dwarf", 4: "Tiefling"}
	choice = input("-----------------\nWhat race is your character?\
	\n(For a description of the race, type the number followed by a question mark)\
	\n1:Human\n2:Elf\n3:Dwarf\n4:Tiefling\n")
	
	if choice == "1" or choice == "2" or choice == "3" or choice == "4":
		race = races[int(choice)]
		kitselection()
	
	elif choice == "1?":
		print("Human are the shortest lived race of Galarion.  This has made\
		\nthem ambitious by nature.  A typical human leverages his short life\
		\nby continually working towards betterment.")
		raceselection()
	
	elif choice == "2?":
		print("Elves are the oldest race of Galarion. Originally from another\
		\nworld, Elven thoughts are alien to the races born of Galrion.  Combined\
		\nwith an average lifespan of nearly 1000 years, elves have a unique\
		\nperspective of time and the world around them.  The typical elf plays\
		\nthe long game, takes their time to make decisions, and acts slowly but\
		\ndeliberately.")
		raceselection()
	
	elif choice == "3?":
		print("Dwarves are born from the very earth of Galarion.  They make\
		\ntheir homes in the mountains where their afinity with prescious metals\
		\nhas led to exquisit blacksmithing and marvelous armaments. Dwarves\
		\ntend to be well grounded in the happenings of Galarion through their\
		\nconnection with the rocks. The typical Dwarf is brash, hearty, and\
		\nhonorable.")
		raceselection()

	elif choice == "4?":
		print("pass")
		raceselection()
		
	else:
		print("I'm sorry that is not a valid selection\n-----------------")
		raceselection()
	
def kitselection():
	intro()

		
start()
print(gender)
print(race)
print(kit)