from router import *

r1 = Router("Cisco", "R3745", "R1")
r2 = Router("Cisco", "R3745", "R2")
R3 = Router("Cisco", "R3745", "R3")

r1.add_interface("Gigabitethernet 0/0")
r1.add_interface("Gigabitethernet 0/1")
r1.add_interface("Gigabitethernet 0/2")

print(r1.show_interfaces())
