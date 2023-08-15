from core.config.functions import msg, warn, path, exec_command, CURRTENTDIR


def start_browser_anonymization():
    msg("firefox browser anonymization started")
    if path.isdir("/etc/firefox-esr") == True or path.isdir("/etc/firefox") == True:
        exec_command(f"cp {CURRTENTDIR}/core/sources/anongt.js /etc/firefox-esr > /dev/null")
        exec_command(f"cp {CURRTENTDIR}/core/sources/anongt.js /etc/firefox > /dev/null")
    else:
        warn("Browser anonymization only supports firefox and firefox not found on your system")


def stop_browser_anonymization():
    exec_command("rm -fr /etc/firefox-esr/anongt.js > /dev/null")
    exec_command("rm -fr /etc/firefox/anongt.js > /dev/null")
    msg("firefox browser anonymization stoped")
