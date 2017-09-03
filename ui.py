import castle
import room
import npc
import pickle
import sys

# Helper functions
def simplify(s):
	s = s.strip()
	s = s.lower()
	return s


# UI Functions
def save(current):
	castle.write_castle()
	castle.write_npcs()
	pickle.dump(castle.castle, open("save/rooms.p", "wb"))
	pickle.dump(current, open("save/current.p", "wb"))
	pickle.dump(castle.npcs_, open("save/npcs.p", "wb"))
	pickle.dump(castle.monsters_, open("save/monsters.p", "wb"))


def load():
	current = pickle.load(open("save/current.p", "rb"))
	castle.castle = pickle.load(open("save/rooms.p", "rb"))
	castle.npcs_ = pickle.load(open("save/npcs.p", "rb"))
	castle.monsters_ = pickle.load(open("save/monsters.p", "rb"))
	castle.read_castle()
	castle.read_npcs()
	return current


def look(current, s):
	s = simplify(s)
	if(not s or s == '-n'):
		print current.name
	if(not s or s == '-d'):
		print str(current.door_num) + " door(s)"
	castle.throw_npc_exception(current)


def info():
	for n in castle.npcs:
		print castle.npcs[n].name + " is in (the) " + castle.npcs[n].location.name
	for n in castle.monsters:
		print castle.monsters[n].name + " is in (the) " + castle.monsters[n].location.name


def open_(current, s):
	s = simplify(s)
	if(not s):
		print "Enter a value after 'open'."
	elif(s == 'all'):
		current.print_adj()
	else:
		try:
			n = int(s)
			if(n > current.door_num):
				print "There aren't that many doors."
			else:
				n = n-1
				print(current.adj[n].name)
				castle.throw_npc_exception(current, False, current.adj[n])
		except ValueError:
			print "Enter a value after 'open'."


def step(current, s):
	s = simplify(s)
	if(not s):
		castle.step()
		castle.throw_npc_exception(current, True)
		return current
	elif(s == '-d'):
		# castle.step()
		# castle.print_npc_locations()
		castle.print_npc_vars()
		return current
	for i in range(len(current.adj)):
		if(s == current.adj[i].name.lower()):
			print "You are now in (the) " + current.adj[i].name + "."
			castle.throw_npc_exception()
			return current.adj[i]
	try:
		n = int(s)
		if(n > current.door_num):
			print "There aren't that many doors."
			return current
		else:
			n =  n-1
			print "You are now in (the) " + current.adj[n].name + "."
			castle.throw_npc_exception(current.adj[n])
			return current.adj[n]
	except ValueError:
		print "I don't recognize that room...?"
		return current 
	

def wave():
	var = " "
	while(var[0] != 'y' and var[0] != 'n'):
		print "Are you sure?"
		var = raw_input("? ")
		if(not var):
			var = " "
		elif(var[0] == 'y'):
			castle.shuffle()
		elif(var[0] == 'n'):
			return False


def move(current, s):
	s = simplify(s)
	npc = None
	if(s):
		try:	
			npc = castle.find_npc(s)
			print "Where would you like " + npc.name + " to be moved to?"
		except:
			print "I don't recognize that name...?"
			return current
		var = raw_input("? ")
		try:
			npc.location = castle.find_room(var)
			print npc.name + " is now in the " + npc.location.name
			return current
		except AttributeError:
			print "I don't recognize that room...?"
	else:
		print "Where would you like to move to?"
		var = raw_input("? ")
		try:
			print "You are now in (the) " + castle.find_room(var).name
			castle.throw_npc_exception(castle.find_room(var))
			return castle.find_room(var)
		except AttributeError:
			print "I don't recognize that room...?"


def hault(s):
	s = simplify(s)
	npc = None
	if(s):
		npc = castle.find_npc(s)
		if(npc == None):
			print "I don't recognize that name...?"
			return
		npc.set_mobility(False)
		return
	else:
		print "Put a value after 'hault'."


def release(s):
	s = simplify(s)
	npc = None
	if(s):
		npc = castle.find_npc(s)
		if(npc == None):
			print "I don't recognize that name...?"
			return
		npc.set_mobility(True)
		return
	else:
		print "Put a value after 'hault'."



def kill(s):
	s = simplify(s)
	npc = None
	npc_list = None
	if(s):
		npc = str(castle.find_npc(s))
		npc_list = castle.find_dict(s)
		if(npc == None or npc_list == None):
			print "I don't recognize that name...?"
			return
		del npc_list[s]
		return
	else:
		print "Put a value after 'kill'."


def exit():
	var = " "
	while(var[0] != 'y' and var[0] != 'n'):
		print "Are you sure you want to end the game?"
		var = raw_input("? ")
		if(not var):
			var = " "
		elif(var[0].lower() == 'y'):		
			print 
			print "Thanks for playing, adventurer!"
			return False
		elif(var[0].lower() == 'n'):
			return True