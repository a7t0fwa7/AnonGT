from core.config.imports import *


# changing tor identity
def change_id():
    print(red(logo))
    # check if stopped
    if is_started() == 1:
        error("anongt is stopped")

    warn("changing tor identity")
    stop_service("tor")
    sleep(1)
    start_service("tor")
    msg("tor identity changed")
