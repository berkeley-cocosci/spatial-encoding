from spatial_learning import Room, World, Experiment

"""Tests for Room"""

def test_room_init():
    return None

def test_room_relations():
    print("Testing left_of")
    test_room_left_of()
    print("Testing right_of")
    test_room_right_of()
    print("Testing in_front_of")
    test_room_in_front_of()
    print("Testing in_back_of")
    test_room_in_back_of()

def test_is_left_of():
    r1 = Room(1, 1)
    r2 = Room(2, 2)
    assert r1.is_left_of(r2)
    assert not r2.is_left_of(r1)

def test_is_right_of():
    r1 = Room(2, 2)
    r2 = Room(1, 1)
    assert r1.is_right_of(r2)
    assert not r2.is_right_of(r1)

def test_is_in_front_of():
    r1 = Room(2, 2)
    r2 = Room(1, 1)
    assert r1.is_in_front_of(r2)
    assert not r2.is_in_front_of(r1)

def test_is_in_back_of():
    r1 = Room(1, 1)
    r2 = Room(2, 2)
    assert r1.is_in_back_of(r2)
    assert not r2.is_in_back_of(r1)



"""Tests for World"""

def test_world_init():
    return None

def test_set_position():
    return None

def test_test_constraint():
    return None

def test_copy():
    w1 = World()
    w2 = w1.copy()
    assert w1 is w2 #not the same object
    assert w1.toString() == w2.toString() #but the identical contents



"""Tests for Experiment"""

def test_experiment_init():
    animals = ['dog', 'cat']
    constraints = [('dog', 'left of', 'cat')]
    exp = Experiment(animals, constraints)
    assert exp.animals == animals
    assert exp.constraints == constraints
    

def test_add_animal():
    exp = Experiment()
    exp.add_animal('dog')
    exp.add_animal('cat')
    assert exp.animals == ['dog', 'cat']

def test_add_constraint():
    c1 = ('dog', 'left of', 'cat')
    c2 = ('dog', 'in front of', 'frog')
    exp = Experiment(['dog', 'cat'])
    exp.add_constraint(c1)
    exp.add_constraint(c2)
    assert exp.animals == ['dog', 'cat', 'frog']
    assert exp.constraints == [c1, c2]

def test_update():
    return None



"""Main testing method"""
@main
def main(*args):
    print("Testing Room")
    test_room_init()
    test_room_relations()

    print("Testing World")
    test_world_init()
    test_set_position()
    test_test_constraint()
    test_copy()

    print("Testing Experiment")


main()

