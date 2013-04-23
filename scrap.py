class Room(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_in_back_of(self, other):
        return self.y > other.y

    def is_in_front_of(self, other):
        return other.in_back_of(self)

    def is_left_of(self, other):
        return self.x < other.x

    def is_right_of(self, other):
        return other.is_left_of(self)


class World(object):

    def __init__(self, animals):
        self.animals = {}
        for a in animals:
            self.animals[a] = None

    def set_position(self, animal, x, y):
        if self.animals[animal] is None:
            room = Room(x, y)
            self.animals[animal] = room
            return room
        else:
            raise ValueError("animal %s is already set" % animal)

    def test_constraint(self, constaint):
        animal1, relation, animal2 = constraint
        if self.animals[animal1] is None:
            return True
        if self.animals[animal2] is None:
            return True
        if relation == "in front of":
            return self.animals[animal1].is_in_front_of(self.animals[animal2])

    def copy(self):
        pass


# Possible relations:
# in front of
# in back of
# left of
# right of
constraints = [
    ('cat', 'in front of', 'dog')
]

animals = ['cat', 'dog']


possible_worlds = []
for x in xrange(6):
    for y in xrange(6):
        world = World(animals)
        world.set_position(animals[0], x, y)
        possible_worlds.append(world)


for animal in animals[1:]:
    new_possible_worlds = []
    for world in possible_worlds:
        new_worlds = []
        for x in xrange(6):
            for y in xrange(6):
                new_world = world.copy()
                new_world.set_position(animal, x, y)
                good = True

                for constraint in constraints:
                    good = new_world.test_constraint(constraint)
                    if not good:
                        break

                if good:
                    new_worlds.append(new_world)

        if len(new_worlds) > 0:
            new_possible_worlds.append(new_worlds)

    possible_worlds = new_possible_worlds
