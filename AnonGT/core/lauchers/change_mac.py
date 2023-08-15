from core.config.imports import *


# changing mac addresses
def change_mac():
    print(red(logo))
    warn("changing mac addresses")
    IFACES = netifaces.interfaces()
    for IFACE in IFACES:
        if IFACE != "lo":
            exec_command(f'ip link set {IFACE} down > "/dev/null"')
            exec_command(f'macchanger -r {IFACE} > "/dev/null"')
            exec_command(f'ip link set {IFACE} up > "/dev/null"')
    msg("changed mac addresses")
