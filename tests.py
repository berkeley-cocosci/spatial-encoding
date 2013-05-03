from spatial_learning import Room, World, Experiment

"""Tests for Room"""

def test_room_init():
    r1 = Room(1, 1)
    r2 = Room(1, 2)
    

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
    r1 = Room(1, 1)
    r2 = Room(2, 2)
    assert r1.is_in_front_of(r2)
    assert not r2.is_in_front_of(r1)

def test_is_in_back_of():
    r1 = Room(2, 2)
    r2 = Room(1, 1)
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
    assert w1 is not w2 #not the same object
    assert w1.to_string() == w2.to_string() #but identical contents



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
    exp.add_animal('frog')
    exp.add_animal('cat')
    assert exp.animals == ['dog', 'cat', 'frog']

def test_add_constraint():
    c1 = ('dog', 'in front of', 'frog')
    exp = Experiment(['dog'])
    exp.add_constraint(c1)
    assert exp.animals == ['dog', 'frog']
    assert exp.constraints == [c1]

def test_update():
    return None


