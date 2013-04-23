import math

"""
spatial_learning.py


"""

	def __init__(self, obj="X", x=0, y=0):
		self.total_rooms = num #total number of rooms

		self.item = obj #item stored in this Room
		# self.x_coord = x
		# self.y_coord = y

		self.left = [] #list of rooms to the left of this
		self.right = [] #list of rooms to the right of this
		self.top = [] #list of rooms above this
		self.bottom = [] #list of rooms below this

		self.locations = Grid(total_rooms) #2D list of possible locations for this Room

	# def set_location(x_coord, y_coord):
	# 	"""set this Room to location (x, y) in the grid"""
	# 	x_coord = x
	# 	y_coord = y
	# 	locations.add_to(this, x, y)

	def set_left_of(room):
		"""set this Room left of parameter Room x"""
		right.append(room)
		locations.ignore_column(total_rooms-1) #last column becomes invalid for this
		room.locations.ignore_column(0) #first column becomes invalid for room

	def set_right_of(room):
		"""set this Room right of parameter Room x"""
		left.append(room)
		locations.ignore_column(0) #first column becomes invalid for this
		room.locations.ignore_column(total_rooms-1) #last column becomes invalid for room

	def set_above(room):
		"""set this Room above parameter Room x"""
		bottom.append(room)
		locations.ignore_row(total_rooms-1) #last row becomes invalid for this
		room.locations.ignore_row(0) #first row becomes invalid for room

	def set_below(room):
		"""set this Room below parameter Room x"""
		top.append(room)
		locations.ignore_row(0) #first row becomes invalid for this
		room.locations.ignore_row(total_rooms-1) #last row becomes invalid for room



class Grid(object):

	def __init__(self, num=0):
		"""Create a Layout base grid by the given number of items."""
		self.size = num
		self.locs = [[]] #a 2D list

	def add_to(room, x, y):
		"""Adds the given room to location (x,y) in the grid"""
		locs[x][y] = room
		room.set_location(x, y)

	def ignore_column(x):
		"""Sets the column x to Rooms with item 'X', representing an invalid location"""
		for i in range(size-1):
			locs[x][i].item = "X"

	def ignore_row(y):
		"""Sets the row y to Rooms with item 'X', representing an invalid location"""
		for i in range(size-1):
			locs[i][y].item = "X"

	def toString():
		"""Prints the string representation of this grid"""
		output = ""
		for x in range(size):
			for y in range(size):
				if (locs[x][y] == null):
					output = " "
				else:
					output = locs[x][y].item
				print(output+" ")
			print("\n")



class Experiment(object, n):

	def __init__(self):
		self.results = [] #list of Grid obejcts representing all possible layouts





"""For practice with python and reading user input"""
def main(*args):
	test = Experiment()
	input_var = raw_input("Enter constraint: ")
	print("You typed: " + input_var)

main()

