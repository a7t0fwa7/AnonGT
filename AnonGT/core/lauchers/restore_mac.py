from core.config.imports import *


# reverting mac addresses
def restore_mac():
    print(red(logo))
    warn("reverting mac addresses")
    IFACES = netifaces.interfaces()
    for IFACE in IFACES:
        if IFACE != "lo":
            exec_command(f'ip link set {IFACE} down > "/dev/null"')
            exec_command(f'macchanger -p {IFACE} > "/dev/null"')
            exec_command(f'ip link set {IFACE} up > "/dev/null"')

    msg("reverted mac addresses")
