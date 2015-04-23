from sys import exit

inventory = []


def cliff_1():
	print "\nSOUTHERN CLIFFS"
	print "You've come upon very steep cliffs."
	print "To the north are more cliffs and to the west is a beach."

	if "matches" not in inventory:
		print "On the ground is a book of matches."
		print "What would you like to do?\n"

		while True:
			next = raw_input("> ")

			if "climb" in next.lower() or "east" in next.lower() or "south" in next.lower():
				dead("\nYou climb just high enough to not survive a fall. Then you slip and land face first.")
			elif "north" in next.lower():
				cliff_2()
			elif "west" in next.lower():
				beach_1()
			elif "take matches" in next.lower():
				print "You take the matches and put them in you pocket.\n"
				inventory.append("matches")
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "Poppycock!"

	else:
		print "It looks like climbing up is a foolish idea."
		print "What would you like to do?\n" 

		while True:
			next = raw_input("> ")

			if "climb" in next.lower() or "east" in next.lower() or "south" in next.lower():
				dead("\nYou climb just high enough to not survive a fall. Then you slip and land face first.")
			elif "north" in next.lower():
				cliff_2()
			elif "west" in next.lower():
				beach_1()
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "Poppycock!"


def cliff_2():
	print "\nEASTERN CLIFFS"
	print "You've come upon very steep cliffs."
	print "To the north and to the south are more cliffs."
	print "To the west is a jungle."
	print "It looks like climbing up is a foolish idea."
	print "What would you like to do?\n"

	while True:
		next = raw_input("> ")

		if "climb" in next.lower() or "east" in next.lower():
			dead("\nYou climb just high enough to not survive a fall. Then you slip and land face first.")
		elif "north" in next.lower():
			cliff_3()
		elif "south" in next.lower():
			cliff_1()
		elif "west" in next.lower():
			jungle()
		elif next.lower() == "inventory":
			print ", ".join(inventory) + "\n"
		else:
			print "C'mon."


def cliff_3():
	print "\nNORTHERN CLIFFS"
	print "You've come upon very steep cliffs."
	print "To the south are more cliffs and to the west is a waterfall."
	print "It seems like climbing up is a foolish idea."
	print "What would you like to do?\n"

	while True:
		next = raw_input("> ")

		if "climb" in next.lower() or "east" in next.lower() or "north" in next.lower():
			dead("\nYou climb just high enough to not survive a fall. Then you slip and land face first.")
		elif "south" in next.lower():
			cliff_2()
		elif "west" in next.lower():
			waterfall()
		elif next.lower() == "inventory":
			print ", ".join(inventory) + "\n"
		else:
			print "Don't be ridiculous."


def beach_1():
	print "\nBEACH"
	print "You are on a beach."
	print "There is a shark's fin visible on the horizon."
	print "To the north is a jungle and to the west is another beach."
	print "To the east there are some cliffs."
	print "What would you like to do?\n"

	while True:
		next = raw_input("> ")

		if "swim" in next.lower() or "south" in next.lower():
			dead("\nThe shark bites off your right leg, swallows it whole, and lets out a huge burp!.")
		elif "north" in next.lower():
			jungle()
		elif "east" in next.lower():
			cliff_1()
		elif "west" in next.lower():
			beach_2()
		elif next.lower() == "inventory":
			print ", ".join(inventory) + "\n"
		else:
			print "How dare you!\n"



def beach_2():
	print "\nBEACH"
	print "You are on a beach."
	print "There appears to be a whale swimming out in the open sea."
	print "To the north you see smoke rising from the crash site."
	print "To the east and to the west are more beaches."
	print "What would you like to do?\n"

	while True:
		next = raw_input("> ")

		if "swim" in next.lower() or "south" in next.lower():
			whale()
		elif "north" in next.lower():
			crash_site()
		elif "west" in next.lower():
			beach_3()
		elif "east" in next.lower():
			beach_1()
		elif next.lower() == "inventory":
			print ", ".join(inventory) + "\n"
		else:
			print "What? Why?\n"


def beach_3():
	print "\nBEACH"
	print "You are on a beach."
	print "To the north and to the east are beaches."

	if "fish" not in inventory: 
		print "You notice a dying fish has just washed up."
		print "What would you like to do?\n"

		while True:
			next = raw_input("> ")

			if "take fish" in next.lower():
				print "\nYou take the fish."
				inventory.append("fish")
				print "What would you like to do?\n"
			elif "eat fish" in next.lower():
				print "\nYou were never a fan of sushi."
			elif "north" in next.lower():
				beach_4()
			elif "south" in next.lower():
				dead("\nThe current quickly pulls you underwater and you drown.")
			elif "east" in next.lower():
				beach_2()
			elif "west" in next.lower():
				dead("\nThe current quickly pulls you underwater and you drown.")
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "Huh? Please.\n"

	else:
		print "What would you like to do?\n"

		while True:
			next = raw_input("> ")

			if "north" in next.lower():
				beach_4()
			elif "south" in next.lower():
				dead("\nThe current quickly pulls you underwater and you drown.")
			elif "east" in next.lower():
				beach_2()
			elif "west" in next.lower():
				dead("\nThe current quickly pulls you underwater and you drown.")
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "Huh? Please.\n"


def beach_4():
	print "\nBEACH"
	print "You are on a beach."
	print "To the north and to the south are more beaches."
	print "To the east you see smoke rising from the crash site."
	print "There appears to be a strong current."
	print "What would you like to do?\n"

	while True:
		next = raw_input("> ")

		if "swim" in next.lower() or "west" in next.lower():
			dead("\nThe current quickly pulls you underwater and you drown.")
		elif "north" in next.lower():
			beach_5()
		elif "south" in next.lower():
			beach_3()
		elif "east" in next.lower():
			crash_site()
		elif next.lower() == "inventory":
			print ", ".join(inventory) + "\n"
		else:
			print "Seriously?\n"


def beach_5():
	print "\nBEACH"
	print "You are on a beach."
	print "To the north is a cliff and to the south is a beach."
	print "To the east you see some bushes."

	if "rag" not in inventory:
		print "There is a torn piece of clothing on the ground from one of the other passengers."
		print "It looks like nothing more than a rag at this point."
		print "What would you like to do?\n"

		while True:
			next = raw_input("> ")

			if "swim" in next.lower() or "west" in next.lower():
				dead("\nThe current quickly pulls you underwater and you drown.")
			elif "north" in next.lower():
				ladder()
			elif "south" in next.lower():
				beach_4()
			elif "east" in next.lower():
				print "\nYou make your way through the bushes and..."
				pit()
			elif "take rag" in next.lower():
				print "You take the rag.\n"
				inventory.append("rag")
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "No comprende.\n"

	else:
		print "There appears to be a strong current."
		print "What would you like to do?\n"

		while True:
			next = raw_input("> ")

			if "swim" in next.lower() or "west" in next.lower():
				dead("\nThe current quickly pulls you underwater and you drown.")
			elif "north" in next.lower():
				ladder()
			elif "south" in next.lower():
				beach_4()
			elif "east" in next.lower():
				print "\nYou make your way through the bushes and..."
				pit()
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "No comprende.\n"


def whale():
	print "\nWHALE"
	print "You decide to go for a swim and the current quickly pulls you underwater."
	print "Just as you think it's the end, the whale comes and swallows you!"
	print "You are now in the stomach of a whale.\n"

	while True:
		next = raw_input("> ")

		if "feather" in inventory and "feather" in next.lower():
			print "You take the feather and lightly brush it against the top of the whale's throat."
			print "The whale lets out a violent sneeze! (and you along with it)"
			print "You fly through the air and land on top of one of the cliffs."
			print "You see a radio tower just a few dozen yards away and go to check it out."
			radio_tower()
			inventory.remove("feather")
		elif next.lower() == "inventory":
			print ", ".join(inventory) + "\n"
		else:
			dead("\nAfter a few days, with salt water all around you, ironically, you die of thirst.")


def waterfall():
	print "\nWATERFALL"
	print "To the south is a jungle and to the east is a cliff."
	print "To the west are some bushes."
	print "There is a beautiful waterfall here, cascading from the top of a cliff."
	print "You sure would like to wash off all the blood from the wreckage."
	print "What would you like to do?\n"

	while True:
		next = raw_input("> ")

		if "rinse" in next.lower() or "wash" in next.lower():
			print "As you rinse off under the cool water, you notice a cave on the other side."
			print "You decide to take a look."
			cave()
		elif "south" in next.lower():
			jungle()
		elif "east" in next.lower():
			cliff_2()
		elif "west" in next.lower():
			print "\nYou make your way through the bushes and..."
			pit()
		elif next.lower() == "inventory":
			print ", ".join(inventory) + "\n"
		else:
			print "Hmm. That didn't seem to work.\n"


def cave():
	print "\nCAVE"
	print "The exit is to the south."
	print "It's fairly dark here."
	dark = True

	if "leg bone" not in inventory:
		print "But you see a few large leg bones just inside the entrance."

		while True:
			print "What would you like to do?\n"
			next = raw_input("> ")

			if "take bone" in next.lower() or "take bones" in next.lower():
				print "You take a leg bone.\n"
				inventory.append("leg bone")
			elif "north" in next.lower() and dark == False:
				bear_room()
			elif "north" in next.lower() and dark == True:
				print "It's too dark to see."
			elif "leave" in next.lower() or "south" in next.lower() or "exit" in next.lower():
				waterfall()
			elif "make torch" in next.lower() and "matches" in inventory and "rag" in inventory and "leg bone" in inventory and "lighter fluid" in inventory:
				print "You wrap the rag tightly around the leg bone, douse it in lighter fluid, and light it with the matches."
				print "You can now see! There is another room just ahead to the north."
				dark = False
				inventory.remove("matches")
				inventory.remove("rag")
				inventory.remove("leg bone")
				inventory.remove("lighter fluid")
				inventory.append("torch")
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "I don't do that.\n"

	else:
		while True:
			print "What would you like to do?\n"
			next = raw_input("> ")

			if "north" in next.lower() and dark == False:
				bear_room()
			elif "north" in next.lower() and dark == True:
				print "It's too dark to see."
			elif "leave" in next.lower() or "south" in next.lower():
				waterfall()
			elif next.lower() == "inventory":
				print inventory
			elif "make torch" in next.lower() and "matches" in inventory and "rag" in inventory and "leg bone" in inventory:
				print "You wrap the rag tightly around the leg bone and light it with the matches."
				print "You can now see! There is another room just ahead to the north."
				dark = False
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "I don't do that.\n"


def bear_room():
	print "\nBEAR ROOM"
	print "There is a huge bear in here and he looks hungry."
	print "To the north and to the east are entrances to seperate chambers."
	bear_moved = False

	while True:
		print "What would you like to do?\n"
		next = raw_input("> ") 

		if "north" in next.lower() and bear_moved == False:
			dead("\nAs you try to enter the room, the bear slaps your face off.")
		elif "south" in next.lower():
			dead("\nAs you try to leave, the bear runs over and hugs you. Hard.")
		elif "east" in next.lower() and bear_moved == False:
			dead("As you try to enter the room, the bear slaps your face off.")
		elif "shoot" in next.lower():
			dead("\nThe bear didn't like that very much and decides to maul you(to death).")
		elif "fish" in next.lower() and bear_moved == False:
			bear_moved = True
			inventory.remove("fish")
			print "You throw the fish at the bear and he peacefully takes it to a corner to munch on.\n"
		elif "north" in next.lower() and bear_moved == True:
			junk_room()
		elif "east" in next.lower() and bear_moved == True:
			gold_room()
		elif next.lower() == "inventory":
			print ", ".join(inventory) + "\n"
		else:
			print "I don't do that.\n"


def bear_room_2():
	print "\nBEAR ROOM"
	print "The bear is still eating the fish in a far corner"
	print "To the north and to the east are entrances to seperate chambers."
	print "The exit is to the south."

	while True:
		print "What would you like to do?\n"
		next = raw_input("> ") 

		if "south" in next.lower() or "exit" in next.lower():
			cave()
		elif "shoot" in next.lower():
			dead("\nThe bear didn't like that very much and decides to maul you to death.")
		elif "north" in next.lower():
			junk_room()
		elif "east" in next.lower():
			gold_room()
		elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
		else:
			print "I don't do that.\n"

def junk_room():
	print "\nJUNK ROOM"
	print "The exit is to the south."
	print "All around you are what appear to be random parts for various electronics."

	if "radio console" not in inventory:
		print "One piece in particular looks like a small radio console."

		while True:
			print "What would you like to do?\n"
			next = raw_input("> ")

			if "take radio" in next.lower():
				print "You take the radio console.\n"
				inventory.append("radio console")
			elif "exit" in next.lower() or "south" in next.lower() or "leave" in next.lower():
				bear_room_2()
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "I don't think so.\n"

	else:
		while True:
			print "What would you like to do?\n"
			next = raw_input("> ")

			if "exit" in next.lower() or "south" in next.lower() or "leave" in next.lower():
				bear_room_2()
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "I don't think so.\n"


def gold_room():
	print "\nGOLD ROOM"
	print "You Enter a chamber filled with gold."
	print "The exit is to the west."
	print "What do you do?\n"

	next = raw_input("> ")

	while True:
		if "take gold" in next.lower():
			dead("\nAs soon as you touch the gold, poison arrows shoot from every direction hitting you in several places.")
		elif "leave" in next.lower() or "west" in next.lower() or "exit" in next.lower():
			bear_room_2()
		elif next.lower() == "inventory":
			print ", ".join(inventory) + "\n"
		else:
			print "Does not compute.\n"


def ladder():
	print "\nLADDER"
	print "There is a cliff here with a rope ladder hanging over."
	print "However, it doesn't seem to be reachable from the ground."
	print "To the south is a beach and to the east are some shrubs."

	while True:
		print "What would you like to do?\n"
		next = raw_input("> ")

		if "climb" in next.lower() or "up" in next.lower() or "north" in next.lower():
			print "You can't seem to reach the ladder, no matter how hard you try."
		elif "east" in next.lower():
			shrubs()
		elif "south" in next.lower():
			beach_5()
		elif next.lower() == "inventory":
			print ", ".join(inventory) + "\n"
		else:
			print "Sorry, I don't get it."



def shrubs():
	print "\nSHRUBS"
	print "There are shrubs all around you."
	print "To the west is a cliff and to the south are some bushes."

	if "lighter fluid" not in inventory:
		print "There is an old can of lighter fluid on the ground."

		while True:
			print "What would you like to do?\n"
			next = raw_input("> ")

			if "take lighter fluid" in next.lower():
				print "You take the lighter fluid."
				inventory.append("lighter fluid")
			elif "west" in next.lower():
				ladder()
			elif "south" in next.lower():
				print "\nYou make your way through the bushes and..."
				pit()
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "Hmm."

	else:
		while True:
			print "What would you like to do?\n"
			next = raw_input("> ")

			if "west" in next.lower():
				ladder()
			elif "south" in next.lower():
				print "\nYou make your way through the bushes and..."
				pit()
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "Hmm."


def radio_tower():
	print "\nRADIO TOWER"
	print "You go into the radio tower."
	print "Inside you see a small part of the tower's console is missing."
	print "The main power switch is turned off."
	print "To the south of the tower is a rope ladder that goes down the cliffs."
	main_power = False
	radio_console_in = False


	if "radio console" in inventory:

		while True:
			print "What would you like to do?\n"
			next = raw_input("> ")

			if "power" in next.lower() and main_power == False and radio_console_in == True:
				print "\nYou turn on the power and the whole tower lights up!"
				print "You hear a voice on the other end and tell them your whole story."
				print "Later that day a helicopter comes to rescue you."
				print "Holy balls, you did it!\n"
				end()
			elif "power" in next.lower() and main_power == False and radio_console_in == False:
				main_power = True
				print "You turn on the power and the whole tower lights up!"
			elif "power" in next.lower() and main_power == True and radio_console_in == False:
				print "The power is now off."
				main_power = False
			elif "radio console" in next.lower() and main_power == True and radio_console_in == False:
				dead("You elecricute yourself as you try to plug in the radio console with the main power turned on.")
			elif "radio console" in next.lower() and main_power == False and radio_console_in == False:
				radio_console_in = True
				inventory.remove("radio console")
				print "The radio console fits perfectly into the tower's main console"
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "That doesn't work."

	else:
		while True:
			print "What would you like to do?\n"
			next = raw_input("> ")

			if "power" in next.lower() and main_power == False:
				main_power = True
				print "You turn on the power and the whole tower lights up!"
			elif "power" in next.lower() and main_power == True:
				print "The power is now off."
				main_power = False
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "That doesn't work."


def pit():
	print "\nSMELLY TAR PIT"
	dead("Oh no! You fall into a tar pit that smells REALLY bad. Also you die.")


def tree():
	print "\nTREE"
	print "What would you like to do?\n"

	next = raw_input("> ")

	if "take feather" in next.lower():
		print "You take the feather."
		inventory.append("feather")
		print "Inside the nest is a large egg."
		tree()
	elif "climb" in next.lower() and "down" in next.lower():
		print "You climb back down the tree to the jungle floor."
		jungle()
	elif "take egg" in next.lower():
		dead("\nSuddenly, a large and very angry condor swoops down to snack on your face.")
	elif next.lower() == "inventory":
		print ", ".join(inventory) + "\n"
	else:
		print "Je ne sais pas."
		tree()

def jungle():
	print "\nJUNGLE"
	print "You are now in a dark, damp jungle."
	print "One of the trees looks good to climb."
	print "To the north is a waterfall and to the south is a beach."
	print "To the east are some cliffs and to the west there is smoke rising from the crash site."
	print "What would you like to do?\n"

	while True:
		next = raw_input("> ")

		if "climb" in next.lower() or "up" in next.lower():
			print "\nYou climb to the top of the tree and see a nest."
			if "feather" not in inventory:
				print "Inside the nest is a feather and a large egg."
				tree()
			else:
				print "Inside the nest is a large egg."
				tree()
		elif "north" in next.lower():
			waterfall()
		elif "south" in next.lower():
			beach_1()
		elif "east" in next.lower():
			cliff_2()
		elif "west" in next.lower():
			crash_site()
		elif next.lower() == "inventory":
			print ", ".join(inventory) + "\n"
		else:
			print "I don't understand.\n"


def crash_site():
	print "\nCRASH SITE"
	print "To the south and to the west are beaches."
	print "To the north are some bushes."
	print "To the east is a jungle with cliffs in the distance."

	if "gun" not in inventory:
		print "The dead man on the ground next to you appears to have been the air marshall."
		print "You can see his handgun falling out of its holster."
		print "What would you like to do?\n"

		while True:
			next = raw_input("> ")

			if "north" in next.lower():
				print "\nYou leave the crash site and make your way through the bushes and..."
				pit()
			elif "south" in next.lower():
				beach_2()
			elif "east" in next.lower():
				jungle()
			elif "west" in next.lower():
				beach_4()
			elif "gun" in next.lower():
				print "You carefully take his gun out of its holster and tuck it down your pants.\n"
				inventory.append("gun")
				print "What would you like to do?\n"
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "Try using a cardinal direction: north, west, etc., or a command with the verb take.\n"

	else:
		print "What would you like to do?\n"

		while True:
			next = raw_input("> ")

			if "north" in next.lower():
				print "\nYou leave the crash site and make you way through the bushes and..."
				pit()
			elif "south" in next.lower():
				beach_2()
			elif "east" in next.lower():
				jungle()
			elif "west" in next.lower():
				beach_4()
			elif next.lower() == "inventory":
				print ", ".join(inventory) + "\n"
			else:
				print "Try using a cardinal direction: north, west, etc., or a command with the verb take.\n"


def dead(why):
	print why, "Way to go!"
	print "GAME OVER\n"
	print "Play again? (Y/n)"

	next = raw_input("> ")

	if next.lower() == "y" or next == "":
		__start__()
	else:
		exit(0)


def end():
	print """Congratulations,
 __   __  _______  __   __    _     _  ___   __    _  __  
|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | ||  | 
|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| ||  | 
|       ||  | |  ||  |_|  |  |       ||   | |       ||  | 
|_     _||  |_|  ||       |  |       ||   | |  _    ||__| 
  |   |  |       ||       |  |   _   ||   | | | |   | __  
  |___|  |_______||_______|  |__| |__||___| |_|  |__||__| 
	"""
	print "Play again? (Y/n)"

	next = raw_input("> ")

	if next.lower() == "y" or next == "":
		__start__()
	else:
		exit(0)


def __start__():
	print "\n\n\n\n\n\n\n\n\n\n\n\n\nSTART"
	print "Welcome to:"
	print """                                                       
 (                                                   
 )\ )  (                )     )       )      )    )  
(()/(  )\ (   (  (   ( /(  ( /(    ( /(   ( /( ( /(  
 /(_))((_))\  )\))(  )\()) )\())   )\())  )\()))\()) 
(_))_| _ ((_)((_))\ ((_)\ (_))/   ((_)\  ((_)\((_)\  
| |_  | | (_) (()(_)| |(_)| |_   |__ (_)|__  //  (_) 
| __| | | | |/ _` | | ' \ |  _|   |_ \    / /| () |  
|_|   |_| |_|\__, | |_||_| \__|  |___/   /_/  \__/   
             |___/                                    
                                       """
	print "Your flight has crashed on a deserted island and you are the only survivor!"
	print "You must find a way to get off the island...\n"
	inventory[:] = []
	crash_site()

__start__()