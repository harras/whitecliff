class Room():

	def __init__(self, name, door_num):
		self.name = name
		self.desc = ''
		self.door_num = door_num
		self.counter = 0
		self.adj = []

	def get_name(self):
		print "Name: ", self.name

	def get_desc(self):
		print "Description: ", self.desc

	def count_up(self):
		self.counter = self.counter + 1

	def is_avail(self):
		if(self.counter < self.door_num):
			return True
		else:
			return False

	def add_adj(self, *args):
		for i in args:	
			self.adj.append(i)
			self.counter+=1

	def add_adj_(self, room):
		self.adj.append(room)
		self.counter+=1

	def print_adj(self):
		s1 = str(self.name) + ": "
		s2 = ""
		for i in self.adj:
			if (len(s2) > 0):
				s2 += ", "
			s2 += str(i.name)
		s1 += s2
		print s1

	def clear(self):
		self.adj = None
		self.adj = []
		self.counter = 0