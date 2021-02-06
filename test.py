# Test file
# Jakkawan Intaratchaiyakij 61070023

import pytest
from Router import *

def create_router():
    r1 = Router("Huawei", "Special X", "R1")
    r2 = Router("Cisco", "R7777", "R2")
    r1.add_interface("G0/0")
    r2.add_interface("G0/1")
    return r1,r2

def test_add_interface():
    r1,r2 = create_router()
    assert r1.interfaces == {"G0/0": {'ip': 'unassigned', 'status': 'shutdown', 'connect': ['none', 'none']}}
    assert r2.interfaces == {"G0/1": {'ip': 'unassigned', 'status': 'shutdown', 'connect': ['none', 'none']}}

def test_connect_to():
    r1,r2 = create_router()
    r1.connect_to("G0/0", r2, "G0/1")
    assert r1.interfaces["G0/0"]['connect'] == ["R2", "G0/1"]

def test_add_ip():
    r1,r2 = create_router()
    r1.add_ip("G0/0", "192.168.1.1/24")
    assert r1.interfaces['G0/0']['ip'] == "192.168.1.1/24"

def test_change_status():
    r1,r2 = create_router()
    r1.change_status("G0/0", "no-shutdown")
    assert  r1.interfaces["G0/0"]["status"] == "no-shutdown"

def test_show_interfaces():
    r1,r2 = create_router()
    r1.add_interface("G0/1")
    r1.add_interface("G0/2")
    assert r1.show_interfaces() == "Show Interfaces of R1\nR1 has 3 interfaces\nG0/0 IP-Address: unassigned \"shutdown\"\nG0/1 IP-Address: unassigned \"shutdown\"\nG0/2 IP-Address: unassigned \"shutdown\"\n"
    assert r2.show_interfaces() == "Show Interfaces of R2\nR2 has 1 interfaces\nG0/1 IP-Address: unassigned \"shutdown\"\n"

def test_show_cdp():
    r1,r2 = create_router()
    r3 = Router("Amazon", "RX9898", "R3")
    r1.add_interface("G0/1")
    r3.add_interface("G0/0")
    r1.connect_to("G0/0", r2, "G0/1")
    r1.connect_to("G0/1", r3, "G0/0")
    assert r1.show_cdp() == "R1 interface G0/0 connect to R2 on interface G0/1\nR1 interface G0/1 connect to R3 on interface G0/0\n"

def test_show_info():
    r1,r2 = create_router()
    assert r1.show_info() == "Brand: Huawei\nModel: Special X\nHostname: R1\n"
    assert r2.show_info() == "Brand: Cisco\nModel: R7777\nHostname: R2\n"
