from router import *

def create_router():
    r1 = Router("Cisco", "R3745", "R1")
    r2 = Router("Cisco", "R3745", "R2")
    r1.add_interface("Gigabitethernet 0/0")
    r2.add_interface("Gigabitethernet 0/1")
    return r1,r2

def test_add_interface():
    r1,r2 = create_router()
    assert r1.interfaces == {"Gigabitethernet 0/0": {'IP-Address' : 'unassigned', 'Status' : 'administratively down', 'Protocol' : 'down'}}
    assert r2.interfaces == {"Gigabitethernet 0/1": {'IP-Address' : 'unassigned', 'Status' : 'administratively down', 'Protocol' : 'down'}}

    