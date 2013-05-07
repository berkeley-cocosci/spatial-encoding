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
    w1 = World()
    assert len(w1.animals) == 0
    animals = ['dog', 'cat']
    w2 = World(animals)
    assert len(w2.animals) == 2
    assert w2.animals['dog'] is None
    assert w2.animals['cat'] is None

def test_set_position():
    w1 = World()
    w1.set_position('dog', 1, 1)
    assert w1.animals['dog'].x == 1
    assert w1.animals['dog'].y == 1
    try:
        w1.set_position('dog', 0, 0)
    except Exception as e:
        assert type(e) is ValueError

    w2 = World(['dog'])
    w2.set_position('dog', 1, 1)
    assert w2.animals['dog'].x == 1
    assert w2.animals['dog'].y == 1
    w2.set_position('cat', 0, 0)
    assert w2.animals['cat'].x == 0
    assert w2.animals['cat'].y == 0

def test_test_constraint():
    animals = ['dog', 'cat']
    w1 = World(animals)
    c1 = ('dog', 'left of', 'cat')
    c2 = ('cat', 'right of', 'dog')
    c3 = ('dog', 'in front of', 'cat')
    c4 = ('cat', 'in back of', 'dog')
    w1.set_position('dog', 1, 1)
    w1.set_position('cat', 2, 2)
    assert w1.test_constraint(c1)
    assert w1.test_constraint(c2)
    assert w1.test_constraint(c3)
    assert w1.test_constraint(c4)

def test_copy():
    w1 = World(['dog'])
    w1.set_position('dog', 1, 1)
    w2 = w1.copy()
    assert w1 is not w2 #not the same object
    assert str(w1) == str(w2) #but identical contents



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


