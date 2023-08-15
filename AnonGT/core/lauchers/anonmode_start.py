from core.config.imports import *


# Anonymous Mode Start
def anonmode_start():
    print(red(logo))
    msg("Start Anonymous Mode")
    if is_started() == 0:
        error("anongt is already started")

    # killing dangerous applications
    safekill()

    # clean configs
    wipe()

    # start browser anonymization
    start_browser_anonymization()

    # check backup dir
    check_backup_dir()

    # backup torrc
    backup_torrc()

    # backup resolve.conf
    backup_resolv_conf()

    # backup iptables rules
    backup_iptables()

    # backup sysctl rules
    backup_sysctl()

    # flush iptables
    flush_iptables()

    # generate new torrc
    gen_torrc()

    # generate new resolv.conf
    gen_resolv_conf()

    # start tor service
    start_service("tor")

    # apply new iptables rules
    apply_iptables_rules()

    # apply new sysctl rules
    apply_sysctl_rules()

    # clear logs
    log_killer()

    msg("all traffic is being redirected through tor")

    exec_command(f"touch {BACKUPDIR}/started")
