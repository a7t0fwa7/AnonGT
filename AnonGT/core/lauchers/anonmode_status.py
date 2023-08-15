from core.config.imports import exec_command
from core.config.banner import banner


# print status
def anonmode_status():
    banner()
    exec_command("xterm -geometry 140x40 -e nyx &")
