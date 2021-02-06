from Router import *
r1 = Router("Cisco", "Model-A", "R1")
r2 = Router("Amazon", "R0uterX", "R2")
r3 = Router("Huawei", "R7777", "R3")

print(r1.show_info())
print(r2.show_info())
print(r3.show_info())

r1.add_interface("Gigabit 0/0")
r1.add_interface("Gigabit 0/1")
r1.add_interface("Gigabit 0/2")
r2.add_interface("Gigabit 0/0")
r2.add_interface("Gigabit 0/1")
r3.add_interface("Gigabit 0/0")

r1.add_ip("Gigabit 0/0", "192.168.1.1")
r2.add_ip("Gigabit 0/0", "192.168.1.2")

r1.connect_to("Gigabit 0/0", r2, "Gigabit 0/0")
r1.connect_to("Gigabit 0/1", r3, "Gigabit 0/0")

r1.change_status("Gigabit 0/0", "no-shutdown")
r2.change_status("Gigabit 0/0", "no-shutdown")
r3.change_status("Gigabit 0/0", "no-shutdown")
print(r1.show_interfaces())
print(r2.show_interfaces())
print(r3.show_interfaces())

print(r1.show_cdp())
print(r2.show_cdp())
print(r3.show_cdp())

