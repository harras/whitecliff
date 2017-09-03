import room
import castle
import desc
import sys
import time
import pickle
import npc

castle.shuffle()
#desc.desc()
playing = True
current = None
counter = 0

# Something analogous to a 'menu screen'
print "Welcome to Whitecliff Castle!"
print 
print "Load previous game?"

var = raw_input("> ")
if(var[0].lower() == 'y'):
	castle.castle = pickle.load(open("save/rooms.p", "rb"))
	current = pickle.load(open("save/current.p", "rb"))
	castle.read_castle()
while(not current):	
	print "Where are you?"
	var = raw_input("> ")
	current = castle.find_room(var)

print "Awesome. You're in (the) " + current.name + "."
print "What would you like to do?"

# Main game loop
while(playing):
	#castle.throw_npc_exception(current)
	var = raw_input("> ")

	if(var.lower() == 'help'):
		print "Commands"
		print "========"
		print
		print "look:            prints description of the room"
		print "open <number>:   shows what is behind that door"
		print "step <number>:   moves you to that room"
		print "move <room>:     moves player to any room"
		print "wave wand:       shuffles the doors again"
		print "save:            saves the game"
		print "load:            loads last saved game"
		print "exit:            ends the game"

	elif(var[:4].lower() == 'save'):
		castle.write_castle()
		pickle.dump(castle.castle, open("save/rooms.p", "wb"))
		pickle.dump(current, open("save/current.p", "wb"))

	elif(var[:4].lower() == 'load'):
		castle.castle = pickle.load(open("save/rooms.p", "rb"))
		current = pickle.load(open("save/current.p", "rb"))
		castle.read_castle()

	elif(var[:4].lower() == 'look'):
		if (var[5:] == '-d'):
			print current.door_num
		if (var[5:] == '-n'):
			print current.name
		else:
			# Here you may consider adding beautiful descriptions
			print current.name
			print str(current.door_num) + " doors"

	elif(var[:4].lower() == 'open'):
		if(len(var) <= 5):
			print "Enter a value after 'open'."
			continue
		elif(var[5:8].lower() == 'all'):
			current.print_adj()

		else:
			try:
				n = int(var[4:])
				if(n > current.door_num):
					print "There aren't that many doors."
				else:
					n = n-1
					print(current.adj[n].name)
					castle.step(castle.monsters)
					# castle.throw_npc_exception(current, current.adj[n])
			except ValueError:
				print "Enter an *integer* value after 'open'."

	elif(var[:4].lower() == 'step'):
		if(len(var) <= 5):
			print "Enter a value after 'step'."
			continue
		try:
			n = int(var[4:])
			if(n > current.door_num):
				print "There aren't that many doors."
			else:
				n = n-1
				current = current.adj[n]
				print "You are now in " + current.name + "."
				castle.step()
		except ValueError:
			castle.print_locations()
			# print "Enter an *integer* value after 'step'."

	elif(var[:4].lower() == 'wave'):
		while(var[0].lower() != 'y' and var[0].lower() != 'n'):
			print "Are you sure?"
			var = raw_input("? ")
			if(not var):
				var = " "
			elif(var[0].lower() == 'y'):		
				castle.shuffle()
				print "Doors have been rearranged."
			elif(var[0].lower == 'n'):
				break
			else:
				continue

	elif(var[:4].lower() == 'move'):
		temp = None
		while(not temp):
			print("Where would you like to move to?")
			var = raw_input("> ")
			current = castle.find_room(var)
			temp = current
			print("You are now in " + current.name + ".")

	elif(var.lower() == 'eagle eye'):
		castle.print_rooms()

	elif(var.lower() == 'end game' or var.lower() == 'exit'):
		while(var[0].lower() != 'y' and var[0].lower() != 'n'):
			print "Are you sure you want to end the game?"
			var = raw_input("? ")
			if(not var):
				var = " "
			elif(var[0].lower() == 'y'):		
				print "Thanks for playing, adventurer!"
				playing = False
			elif(var[0].lower == 'n'):
				break
			else:
				continue
	else:
		print "I don't understand...?"
		counter =+1
		if counter > 3:
			print "Type 'help' for help."
			counter = 0

exit()
