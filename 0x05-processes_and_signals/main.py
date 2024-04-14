#!/usr/bin/python3

class Orange:
	__nb_instances = 0

	def __init__(self):
		Orange.__nb_instances += 1
		self.id = Orange.__nb_instances
	
class User(Orange):
	name = "me"

	def __init__(self, name=None):
		self.id = 99
		self.name = name

u = User("Hello")
print(u.name)
