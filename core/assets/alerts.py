from core.config.colors import *


# print error and exit
def error(e):
    print(red(f"[-] {e}"))
    exit(1)


# print warning
def warn(m):
    print(yellow(f"[!] {m}"))


# print message
def msg(m):
    print(green(f"[+] {m}"))


# print info
def info(m):
    print(blue(f"[*] {m}"))
