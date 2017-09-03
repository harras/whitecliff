import room
import npc
import random

castle ={}
rooms = []
npcs = {}
npcs_ = {}
monsters = {}
monsters_ = {}

# Initializing all the rooms
# Floor 1
rooms.append(room.Room("Front Porch", 1))	# 0
rooms.append(room.Room("Forier", 10))		# 1
rooms.append(room.Room("Closet", 1))		# 2
rooms.append(room.Room("Den", 2))			# 3
rooms.append(room.Room("Patio", 1))			# 4
rooms.append(room.Room("Hallway 1", 5))		# 5
rooms.append(room.Room("Bathroom 1", 1))	# 6
rooms.append(room.Room("Kitchen", 1))		# 7
rooms.append(room.Room("Dining Room", 3))   # 8
rooms.append(room.Room("Green House", 3))	# 9
rooms.append(room.Room("Garden Path", 1))	# 10

#Floor 2
rooms.append(room.Room("Guest Bed 1", 2))	# 11
rooms.append(room.Room("Guest Bed 2", 2))	# 12
rooms.append(room.Room("Tower Study", 1))	# 13
rooms.append(room.Room("Library", 2))		# 14
rooms.append(room.Room("Staircase", 4))		# 15

#Floor 3
rooms.append(room.Room("Hallway 2", 5)) 	# 16
rooms.append(room.Room("Attic", 1))			# 17
rooms.append(room.Room("Training Room", 1))	# 18
rooms.append(room.Room("Bathroom 2", 1))	# 19
rooms.append(room.Room("Ilta's Room", 2))	# 20
rooms.append(room.Room("Ilta's Balcony", 1))# 21

#Roof
rooms.append(room.Room("Roof", 1))			# 22

#Basement
rooms.append(room.Room("Toto's Chamber", 2))# 23
rooms.append(room.Room("Basement Hall", 8))	# 24 
rooms.append(room.Room("Cave", 1))			# 25
rooms.append(room.Room("Cell 1", 1))		# 26
rooms.append(room.Room("Cell 2", 1))		# 27
rooms.append(room.Room("Cell 3", 1))		# 28
rooms.append(room.Room("Cell 4", 1))		# 29
rooms.append(room.Room("Cell 5", 1))		# 30
rooms.append(room.Room("Cell 6", 1))		# 31
rooms.append(room.Room("Mansion Core", 1))	# 32


# Creates defualt castle layout
# Painstaking... should've been a dict
# Human readability is important, dammit!
# This all looks like nonsense
def init_castle():
	rooms[0].add_adj(rooms[1])
	rooms[1].add_adj(rooms[0], rooms[5], rooms[8], rooms[2], rooms[3], rooms[13], rooms[14], rooms[15], rooms[11], rooms[12])
	rooms[2].add_adj(rooms[1])
	rooms[3].add_adj(rooms[1], rooms[4])
	rooms[4].add_adj(rooms[3])
	rooms[5].add_adj(rooms[6], rooms[7], rooms[9], rooms[8], rooms[1])
	rooms[6].add_adj(rooms[5])
	rooms[7].add_adj(rooms[5])
	rooms[8].add_adj(rooms[5], rooms[9], rooms[1])
	rooms[9].add_adj(rooms[10], rooms[8], rooms[5])
	rooms[10].add_adj(rooms[9])
	
	rooms[11].add_adj(rooms[1], rooms[12])
	rooms[12].add_adj(rooms[1], rooms[13])
	rooms[13].add_adj(rooms[1])
	rooms[14].add_adj(rooms[15], rooms[1])
	rooms[15].add_adj(rooms[14], rooms[1], rooms [16], rooms[22])
	
	rooms[16].add_adj(rooms[17], rooms[15], rooms[18], rooms[19], rooms[20])
	rooms[17].add_adj(rooms[16])
	rooms[18].add_adj(rooms[16])
	rooms[19].add_adj(rooms[16])
	rooms[20].add_adj(rooms[16], rooms[21])
	rooms[21].add_adj(rooms[20])
	
	rooms[22].add_adj(rooms[15])
	
	rooms[23].add_adj(rooms[25], rooms[24])
	rooms[24].add_adj(rooms[31], rooms[30], rooms[29], rooms[23], rooms[26], rooms[27], rooms[28], rooms[32])
	rooms[25].add_adj(rooms[23])
	rooms[26].add_adj(rooms[24])
	rooms[27].add_adj(rooms[24])
	rooms[28].add_adj(rooms[24])
	rooms[29].add_adj(rooms[24])
	rooms[30].add_adj(rooms[24])
	rooms[31].add_adj(rooms[24])
	rooms[32].add_adj(rooms[24])



# NPCs and Monsters
# Consider dropping the name attribute...
def init_npcs():	
	npcs['witch1'] = npc.NPC("Witch 1", rooms[17], False) 
	npcs['witch2'] = npc.NPC("Witch 2", rooms[3])
	npcs['shadow1'] = npc.NPC("Shadow 1", rooms[3])
	npcs['shadow2'] = npc.NPC("Shadow 2", rooms[3])
	npcs['shadow3'] = npc.NPC("Shadow 3", rooms[3])

	monsters['beast'] = npc.NPC("Displacer Beast", rooms[26], False, 4)
	monsters['cube'] = npc.NPC("Gelatinous Cube", rooms[27], False, 7)
	monsters['ithilid'] = npc.NPC("Ithilid", rooms[28], False, 2) # Int rolls?
	monsters['rust'] = npc.NPC("Rust Monster", rooms[29], False, 8) # Eats weapons
	monsters['grue'] = npc.NPC("Grue", rooms[30], False, 3) # Casts magical darkness, never seen
	monsters['xorn'] = npc.NPC("Xorn", rooms[31], False, 4) # Eats magic items


# Functions related to saving. Restructures rooms into a dict, no pointers
# Creates dict
def write_castle():
	for i in rooms:
		castle[i.name] = []
		for j in range(i.door_num):
			castle[i.name].append(i.adj[j].name)

# Reads dict
def read_castle():
	for i in rooms:
		i.clear()
	parent = None
	for i in castle:
		parent = find_room(i)
		for j in castle[i]:
			child = find_room(j)
			parent.adj.append(child)

# Garbage code
def write_npcs():
	for i in npcs:
		npcs_[i] = npcs[i]
		npcs_[i].location = npcs_[i].location.name
	for i in monsters:
		monsters_[i] = monsters[i]
		monsters_[i].location = monsters_[i].location.name

# I'm sorry, God
def read_npcs():
	for i in npcs_:
		npcs[i] = npcs_[i]
		npcs[i].location = find_room(npcs[i].location)
	for i in monsters_:
		monsters[i] = monsters_[i]
		monsters[i].location = find_room(monsters[i].location)
	


# Helper function
def find_room(s):
	for i in rooms:
		if s.lower() == i.name.lower():
			return i


# Main algorithm. It works, but consider revising.
# An open list that shrinks when rooms become unavailible...
# Would be save time complexity 

# Rereading this now, lol... concerns over runtime
def shuffle():
	open_list = list(rooms)
	for i in open_list:
		i.clear()
	while(open_list):	
		for i in open_list:
			rand = int(random.random()*len(open_list))
			if(not i.is_avail()):
				open_list.remove(i)
			elif(not open_list[rand].is_avail()):
				open_list.remove(open_list[rand])
			elif(i == open_list[rand]):
				if(i.counter + 1) < i.door_num:
					i.add_adj(open_list[rand])
					open_list[rand].add_adj(i)
				else:
					continue
			else:
				i.add_adj(open_list[rand])
				open_list[rand].add_adj(i) 


# Helper function for seeing the full range
# of rooms availible to a player
def dfs(start):
	visited = set()
	stack = []
	stack.append(start)

	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			for i in vertex.adj:
				if i not in visited:
					stack.append(i)
	return visited


# Printing functions
def print_rooms():
	for i in rooms:
		i.print_adj()

# Event functions and helper functions
# Tells DM if monsters are in the same room as NPCs
# figure this out in a bit

# I realize the doubling up for the two lists is bad code.
# I'm owning up to it... it makes it so I don't have to 
# double up in main.
def step(npc_list = None):
	if(npc_list):
		for n in npc_list:
			npc_list[n].step()
	else:
		for n in npcs:
			npcs[n].step()
		for n in monsters:
			monsters[n].step()


# Make 'open all' not affect this
# add 'flagged rooms' option
def throw_npc_exception(room=None, b=False, room_adj=None):
	s = ['Green House', 'Training Room', 'Toto\'s Chamber', 'Library']
	if(b):
		for n in npcs:
			if npcs[n].location.name in s:
				print "* " + npcs[n].name + " is in (the) " + npcs[n].location.name
		for n in npcs:	
			for m in monsters:
				if npcs[n].location.name == monsters[m].location.name:
					monsters[m].set_mobility(True)
					print("** " + npcs[n].name + " and the " + monsters[m].name + " are both in (the) " + npcs[n].location.name)
		for n in monsters:
			if monsters[n].location.name in s:
				print "* " + monsters[n].name + " is in (the) " + monsters[n].location.name
	for n in npcs:
		if(room_adj):
			if npcs[n].location.name == room_adj.name:
				print("! " + npcs[n].name + " is in that room")
		if(room):
			if npcs[n].location.name == room.name:
				print("!! " + npcs[n].name + " is in the room you're in")

	for n in monsters:
		if(room_adj):
			if monsters[n].location.name == room_adj.name:
				monsters[n].set_mobility(True)
				monsters[n].step()
				if monsters[n].location.name == room_adj.name:
					print("!!! The" + monsters[n].name + " is in that room")
		if(room):
			if monsters[n].location.name == room.name:
				monsters[n].set_mobility(True)
				print("!!!! The " + monsters[n].name + " is in the room you're in")

# Shitty helper functions
def find_dict(s):
	try:	
		if(npcs[s]):
			return npcs
	except KeyError:
		pass
	try:	
		if(monsters[s]):
			return monsters
	except KeyError:
		pass
	return
		

def find_npc(s):
	try:	
		if(npcs[s]):
			return npcs[s]
	except KeyError:
		pass
	try:	
		if(monsters[s]):
			return monsters[s]
	except KeyError:
		pass
	return


def print_npc_locations():
	print
	for n in npcs:
		print(npcs[n].name + " is in (the) " + npcs[n].location.name)
	print 
	for n in monsters:
		print(monsters[n].name + " is in (the) " + monsters[n].location.name)


def print_npc_vars():
	print ""
	for n in npcs:
		print ""
		npcs[n].print_vars()
	print "__________________"
	print ""
	for n in monsters:
		print ""
		monsters[n].print_vars()


# Events players trigger during the game
def event_1(current):
	if(npcs['witch2']):
		npcs['witch2'].location = current
		npcs['shadow5'] = npc.NPC("Shadow 5", current)
	else:
		npcs['shadow5'] = npc.NPC("Shadow 5", current)
		npcs['shadow6'] = npc.NPC("Shadow 6", current)
		npcs['shadow7'] = npc.NPC("Shadow 7*", current)
		npcs['shadow8'] = npc.NPC("Shadow 8", current)
	throw_npc_exception(current, True)

def event_2(current):
	npcs['highchurch'] =  npc.NPC("Captain Highchurch", rooms[8])
	npcs['soldier1'] = npc.NPC("Solider 1", rooms[8])
	npcs['soldier2'] = npc.NPC("Solider 2", rooms[8])
	npcs['soldier3'] = npc.NPC("Solider 3", rooms[8])
	npcs['soldier4'] = npc.NPC("Solider 4", rooms[9])
	npcs['soldier5'] = npc.NPC("Solider 5", rooms[10])
	npcs['soldier6'] = npc.NPC("Solider 6", rooms[1])
	npcs['soldier7'] = npc.NPC("Solider 7", rooms[1])
	npcs['soldier8'] = npc.NPC("Solider 8", rooms[1])
	npcs['soldier9'] = npc.NPC("Solider 9", rooms[15])
	npcs['soldier10'] = npc.NPC("Solider 10", rooms[15])
	npcs['soldier11'] = npc.NPC("Solider 1", rooms[4])
	npcs['soldier12'] = npc.NPC("Solider 1", rooms[4])
	throw_npc_exception(current, True)