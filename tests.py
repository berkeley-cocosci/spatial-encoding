from spatial_learning import Room

def test_room_left_of():
    r1 = Room(1, 1)
    r2 = Room(2, 2)
    assert r1.is_left_of(r2)
