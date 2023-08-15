from core.config.imports import *


def anonmode_stop():
    print(red(logo))
    # check if stopped
    if is_started() == 1:
        error("anongt is already stopped")

    # killing dangerous applications
    safekill()

    # stop browser anonymization
    stop_browser_anonymization()

    # check backup dir
    check_backup_dir()

    # restore sysctl rules
    restore_sysctl()

    # flush iptables rules
    flush_iptables()

    # restore iptables rules
    restore_iptables()

    # stop tor service
    stop_service("tor")

    # restore torrc
    restore_torrc()

    # restore resolv.conf
    restore_resolv_conf()

    # clean config
    wipe()

    # clear logs
    log_killer()

    exec_command(f"rm -f {BACKUPDIR}/started")
