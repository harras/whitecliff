import castle
import sys
import ui

castle.shuffle()
#desc.desc()
#castle.init_castle()
playing = True
current = castle.rooms[8]
counter = 0

# Something analogous to a 'menu screen' 
print "Load previous game?"

var = raw_input("> ")
if(var and var[0].lower() == 'y'):
	current = castle.find_room(ui.load().name)

else:
	castle.init_npcs()
	while(not current):	
		print "Where are you?"
		var = raw_input("> ")
		current = castle.find_room(var)

print ""
print "       - ---=<0>=--- -"
print "Welcome to Whitecliff Castle!"
print "       - ---=====--- -"

print ""
print ""
print "You're in (the) " + current.name + "."
print "What would you like to do?"

# Main game loop
while(playing):
	print ""
	#castle.throw_npc_exception(current)
	var = raw_input("> ")


	if(var[:4].lower() == 'help'):
		print "Commands"
		print "========"
		print "look:            prints description of the room"
		print "open <room>:     shows what is behind that door"
		print "step <room>:     moves you to that room"
		print "move <room>:     moves player to any room"
		print "wave wand:       shuffles the doors again"
		print "save:            saves the game"
		print "load:            loads last saved game"
		print "exit:            ends the game"

		if(var[:8].lower() == 'help -dm'):
			print "throw:           throws the npc warnings"
			print "info:            prints details about npcs"
			print "hault <npc>:     keeps an npc from moving"
			print "release <npc>:   lets haulted npc move"
			print "kill <npc>:      kills npc"
			print "eagle eye:       prints all room adjacencies"


	elif(var[:4].lower() == 'save'):
		ui.save(current)

	elif(var[:4].lower() == 'load'):
		current = castle.find_room(ui.load().name)

	elif(var[:4].lower() == 'look'):
		ui.look(current, var[5:])

	elif(var[:4].lower() == 'open'):
		ui.open_(current, var[5:])
		
	elif(var[:4].lower() == 'step'):
		current = ui.step(current, var[5:])

	elif(var[:4].lower() == 'move'):
		current = ui.move(current, var[5:])

	elif(var[:5].lower() == 'throw'):
		castle.throw_npc_exception(current, True)

	elif(var[:4].lower() == 'info'):
		ui.info()

	elif(var[:4].lower() == 'wave' or var[:7].lower() == 'shuffle'):
		ui.wave()

	elif(var[:5].lower() == 'hault'):
		ui.hault(var[6:])

	elif(var[:7].lower() == 'release'):
		ui.release(var[8:])

	elif(var[:4].lower() == 'kill'):
		ui.kill(var[5:])

	elif(var.lower() == 'eagle eye'):
		castle.print_rooms()

	elif(var.lower() == 'event 1'):
		castle.event_1(current)

	elif(var.lower() == 'event 2'):
		castle.event_2(current)

	elif(var.lower() == 'end game' or var.lower() == 'exit'):
		playing = ui.exit()

	else:
		print "I don't understand...?"
		counter += 1
		if counter >= 3:
			print "Type 'help' for help."
			counter = 0

exit()