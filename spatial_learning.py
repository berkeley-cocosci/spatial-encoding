""" PLANS

-dictionary of items/animals name strings -> integer representations?

"""

class Constraint(object):

  def __init__(self, piv, pos, item):
		self.pivot = piv
		self.position = pos
		self.item = item

	def __init__(self, msg):
		self.info = interpret(msg)
		self.pivot = info[0]
		self.position = info[1]
		self.item = info[3]

	#parse the user input and returns a list [pivot, position, item]
	def interpret(msg):
		return


class Layout(object):

	def __init__(self, x=0, y=0):
		"""Create a Layout with the given dimensions."""
		self.width = x
		self.height = y
		self.grid = [[]] #A 2D list
		self.constraints = []

	#Adds the constraint to this layout and updates it accordingly
	def add_constraint(rule):
		constraints.append(rule)
		#update the layout

	#Prints out the string representation of each possible layout
	def toString():
		for x in range(width):
			for y in range(height):
				print(grid[x][y]+" ")
			print("\n")


class Experiment(object):

	def __init__(self):
		self.results = [] #list of all possible layouts

	#Generates the valid layouts up to this point
	#for each of the existing possible layouts, add and update with new constraints
	#HOW TO HANDLE IF FOR ONE LAYOUT THE NEW CONSTRAINT CAN HAVE MULTIPLE NEW LAYOUTS?!?!
	def update_layouts(updates):
		for info in updates:
			msg = Constraint(info)
			for layout in results:
				layout.add_constraint(msg)

#To test my hand in python...it's been a while
def main(*args):
	input_var = raw_input("Enter constraint: ")
	print("You typed: " + input_var)

main()
