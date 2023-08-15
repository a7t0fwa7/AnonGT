#!/bin/python3
from core.config.imports import *
from core.lauchers.anonmode_start import anonmode_start
from core.lauchers.anonmode_stop import anonmode_stop
from core.lauchers.anonmode_status import anonmode_status
from core.lauchers.change_id import change_id
from core.lauchers.change_mac import change_mac
from core.lauchers.restore_mac import restore_mac


################################################################################
#                                                                              #
# anongt - redirect all traffic through tor network                            #
#                                                                              #
# DESCRIPTION                                                                  #
# Script to redirect all traffic through tor network including                 #
# dns queries for anonymizing entire system                                    #
# killing dangerous applications                                               #
# clear configs & logs                                                         #
# firefox browser anonymization                                                #
#                                                                              #
#                                                                              #
# AUTHORS                                                                      #
# https://t.me/gtsec                                                           #
#                                                                              #
################################################################################

def anongt():
    check_root()

    cmd = listToString(sys.argv[1:])
    # if len(cmd) == 0:
    #     banner()
    if cmd == "start":
        clear()
        anonmode_start()
    elif cmd == "stop":
        clear()
        anonmode_stop()
    elif cmd == "status":
        clear()
        anonmode_status()
    elif cmd == "chngid":
        clear()
        change_id()
    elif cmd == "chngmac":
        clear()
        change_mac()
    elif cmd == "rvmac":
        clear()
        restore_mac()
    elif cmd == "wipe":
        clear()
        print(red(logo))
        safekill()
        log_killer()
        wipe()

    elif cmd == "about":
        clear()
        about()
    else:
        clear()
        banner()


if __name__ == '__main__':
    anongt()
