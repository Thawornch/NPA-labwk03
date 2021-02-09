from router import *

def create_router():
    r1 = Router("Cisco", "R3745", "R1")
    r2 = Router("Cisco", "R3745", "R2")
    return r1,r2

def test_add_interface():
    r1,r2 = create_router()
    r1.add_interface("Gigabitethernet 0/0")
    r2.add_interface("Gigabitethernet 0/1")
    assert r1.interfaces == {"Gigabitethernet 0/0": {'IP-Address' : 'unassigned', 'Status' : 'administratively down', 'Protocol' : 'down'}}
    assert r2.interfaces == {"Gigabitethernet 0/1": {'IP-Address' : 'unassigned', 'Status' : 'administratively down', 'Protocol' : 'down'}}

def test_show_interfaces():
    r1,r2 = create_router()
    r1.add_interface("Gigabitethernet 0/0")
    r1.add_interface("Gigabitethernet 0/1")
    r1.add_interface("Gigabitethernet 0/2")
    r2.add_interface("Gigabitethernet 0/0")
    r2.add_interface("Gigabitethernet 0/1")
    r2.add_interface("Gigabitethernet 0/2")
    assert r1.show_interfaces() == "Show interfaces of R1\nR1 has 3 interfaces\nGigabitethernet 0/0\nGigabitethernet 0/1\nGigabitethernet 0/2\n"
    assert r2.show_interfaces() == "Show interfaces of R2\nR2 has 3 interfaces\nGigabitethernet 0/0\nGigabitethernet 0/1\nGigabitethernet 0/2\n"
    
    