"""
spatial_learning.py


"""
    
class Room(object):
    """A Room has position (x, y) knows its relations to other Room objects"""

    def __init__(self, x, y):
        """Constructs a Room with the given position (x, y)"""
        self.x = x
        self.y = y

    def is_in_back_of(self, other):
        """Returns true if self is in the back of other, false otherwise
           An object is considered in back of if its y-coordinate is greater"""
        return self.y > other.y

    def is_in_front_of(self, other):
        """Returns true if self in in front of other, false otherwise"""
        return other.is_in_back_of(self)

    def is_left_of(self, other):
        """Returns true if self is left of other, false otherwise"""
        return self.x < other.x

    def is_right_of(self, other):
        """Returns true if self is right of other, false otherwise"""
        return other.is_left_of(self)

    def copy(self):
        new_room = Room(self.x, self.y)
        return new_room

    def __str__(self):
        """Returns the string representation of this Room"""
        return "Room at (%d, %d)" % (self.x, self.y)



class World(object):
    """A World has animals and sets them to Rooms given constraints"""

    def __init__(self, animals=None):
        """Constructs a World with the given animals with Rooms initialized to None"""
        if type(animals) is dict:
            self.animals = animals
        else:
            self.animals = {}
            if animals is None:
                animals = []
            for a in animals:
                self.animals[a] = None

    def set_position(self, animal, x, y):
        """Sets the given animal to a new Room at position (x, y) and returns the room.
            Adds the animal to animals if it does not already exist.
            Raises a ValueError if the animal is already set."""
        if animal not in self.animals:  
            self.animals[animal] = None
        if self.animals[animal] is None:
            room = Room(x, y)
            self.animals[animal] = room
            return room
        else:
            raise ValueError("Animal %s is already set at (%d, %d)" % (animal, self.animals[animal].x, self.animals[animal].y))

    def test_constraint(self, constraint):
        """Tests whether the given constraint is satisfied"""
        animal1, relation, animal2 = constraint
        if self.animals[animal1] is None:
            return True
        if self.animals[animal2] is None:
            return True
        if relation == "in front of":
            return self.animals[animal1].is_in_front_of(self.animals[animal2])
        elif relation == "in back of":
            return self.animals[animal1].is_in_back_of(self.animals[animal2])
        elif relation == "left of":
            return self.animals[animal1].is_left_of(self.animals[animal2])
        else:
            return self.animals[animal1].is_right_of(self.animals[animal2])

    def copy(self):
        """Creates and returns a copy of this World"""
        new_animals = {}
        for a in self.animals:
            if self.animals[a] is None:
                new_animals[a] = None
            else:
                new_animals[a] = self.animals[a].copy()
        new_world = World(new_animals)
        return new_world

    def __str__(self):
        """Returns the string representation of this World"""
        output = ""
        for animal in self.animals:
            output += "Animal is %s \n" % animal
            for room in [self.animals[animal]]:
                if room is None:
                    output += "Room is None"
                else:
                    output += str(room)
                output += "\n"
        return output



class Experiment(object):

    def __init__(self, animals=None, constraints=None):
        """Initializes an experiment with all possible worlds given animals and constraints"""
        self.valid_relations = ['left of', 'right of', 'in front of', 'in back of']

        if animals is None:
            animals = []
        if constraints is None:
            constraints = []

        self.animals = animals
        self.constraints = constraints
        self.possible_worlds = []
        self.update()

    def update(self):
        """Updates the possible worlds for this Experiment"""
        num_animals = len(self.animals)

        #Initialize the first animal (constraints trivial) to all positions
        self.possible_worlds = []
        for x in xrange(num_animals):
            for y in xrange(num_animals):
                world = World(self.animals)
                world.set_position(self.animals[0], x, y)
                self.possible_worlds.append(world)

        for animal in self.animals[1:]:
            new_possible_worlds = []

            for world in self.possible_worlds:
                new_worlds = []
                if animal not in world.animals.keys():
                    world.animals[animal] = None

                for x in xrange(num_animals):
                    for y in xrange(num_animals):
                        new_world = world.copy()
                        new_world.set_position(animal, x, y)
                        valid = True

                        for constraint in self.constraints:
                            valid = new_world.test_constraint(constraint)
                            if not valid:
                                break

                        if valid:
                            new_worlds.append(new_world)

                if len(new_worlds) > 0:
                    for w in new_worlds:
                        new_possible_worlds.append(w)

            self.possible_worlds = new_possible_worlds

    def add_animal(self, animal):
        """Adds the animal to the list of animals in this Experiment.
           Does nothing if the animal already exists."""
        if animal not in self.animals:
            self.animals.append(animal)
            self.update()

    def add_constraint(self, constraint):
        """Adds the constraint to the list of constraints in this Experiment.
           Adds animals included in the constraint as needed."""
        if type(constraint) is not tuple or len(constraint) < 3:
            raise ValueError("Invalid constraint format")
        elif constraint[1] not in self.valid_relations:
            raise ValueError("Invalid relation %s" % constraint[1])
        self.add_animal(constraint[0])
        self.add_animal(constraint[2])
        self.constraints.append(constraint)
        self.update()

    def main(*args):
        animals = []
        constraints = []
        while True:
            animal = raw_input("Enter animal (or \"done\"): ")
            if animal == 'done':
                break
            animals.append(animal)
        experiment = Experiment(None, constraints)
        for a in animals:
            experiment.add_animal(a)

        print("\nConstraint format: animal1, relation, animal2")
        print("Valid relations are %s" % experiment.valid_relations)
        while True:
            try:
                constraint = raw_input("Enter constraint (or \"done\"): ")
                if constraint == 'done':
                    break
                constraint_tuple = tuple(x.strip() for x in constraint.split(','))
                experiment.add_constraint(constraint_tuple)
            except ValueError as e:
                print(e)
                pass

        #End result print statements
        # print("animals: %s" % experiment.animals)
        # print("constraints: %s" % experiment.constraints)
        # print("worlds:\n%s" % experiment.possible_worlds)
        print(len(experiment.possible_worlds))
        for w in experiment.possible_worlds:
            print(w)

if __name__ == "__main__":
    Experiment().main()


