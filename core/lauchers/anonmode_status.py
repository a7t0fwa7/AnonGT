from core.config.imports import *


# print status
def anonmode_status():
    print(red(logo))
    cmd = ["systemctl", "is-active", "tor"]
    TORSTATUS = get_process(cmd)

    if is_started() == 0:
        msg("anongt is started")
    else:
        warn("anongt is stopped")

    if TORSTATUS == "active":
        msg("tor service is: " + TORSTATUS)
        exec_command("xterm -geometry 140x40 -e nyx &")
    else:
        warn("tor service is: " + TORSTATUS)

    get_ip()
