class Room(object):
    """A Room has position (x, y) knows its relations to other Room objects"""

    def __init__(self, x, y):
        """Constructs a Room with the given position (x, y)"""
        self.x = x
        self.y = y

    def is_in_back_of(self, other):
        """Returns true if self is in the back of other, false otherwise"""
        return self.y > other.y

    def is_in_front_of(self, other):
        """Returns true if self in in front of other, false otherwise"""
        return other.in_back_of(self)

    def is_left_of(self, other):
        """Returns true if self is left of other, false otherwise"""
        return self.x < other.x

    def is_right_of(self, other):
        """Returns true if self is right of other, false otherwise"""
        return other.is_left_of(self)


class World(object):
    """A World has animals and sets them to Rooms given constraints"""

    def __init__(self, animals):
        """Constructs a World with the given animals with Rooms initialized to None"""
        self.animals = {}
        for a in animals:
            self.animals[a] = None

    def set_position(self, animal, x, y):
        """Sets the given animal to a new Room at position (x, y) and returns the room.
            Raises a ValueError if the animal is already set."""
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
        World new_world = World(self.animals)
        return new_world


# Possible relations:
# in front of
# in back of
# left of
# right of
constraints = [
    ('cat', 'in front of', 'dog'),
    ('dog', 'left of', 'fish')
]

animals = ['cat', 'dog', 'fish']


possible_worlds = []
for x in xrange(len(animals)):
    """Initialize the first animal (constraints trivial) to all positions"""
    for y in xrange(len(animals)):
        world = World(animals)
        world.set_position(animals[0], x, y)
        possible_worlds.append(world)


for animal in animals[1:]:
    new_possible_worlds = []
    for world in possible_worlds:
        new_worlds = []
        for x in xrange(len(animals)):
            for y in xrange(len(animals)):
                new_world = world.copy()
                new_world.set_position(animal, x, y)
                valid = True

                for constraint in constraints:
                    valid = new_world.test_constraint(constraint)
                    if not valid:
                        break

                if valid:
                    new_worlds.append(new_world)

        if len(new_worlds) > 0:
            new_possible_worlds.append(new_worlds)

    possible_worlds = new_possible_worlds


