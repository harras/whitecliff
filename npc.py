import room
import random

class NPC():

	def __init__(self, name, location, is_mobile=True, stagger = 1):
		self.name = name
		self.location = location
		self.is_mobile = is_mobile
		self.stagger = stagger
		self.counter = 0

	def step(self):	
		self.counter = self.counter + 1
		if(self.counter >= self.stagger and self.is_mobile):
			rand = int(random.random()*self.location.door_num)
			self.location = self.location.adj[rand]
			self.counter = 0
		#print self.location.name

	def set_mobility(self, bool):
		self.is_mobile = bool

	def set_location(self, location):
		self.location = location

	def print_vars(self):
		print "Name: " + str(self.name)
		print "Location: " + str(self.location.name)
		print "Mobilitiy: " + str(self.is_mobile)
		print "Stagger: " + str(self.stagger)
		print "Counter: " + str(self.counter)