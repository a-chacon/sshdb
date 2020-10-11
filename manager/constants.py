import os
import getpass
import pwd

# This implementation is mostly for GUI support. See #168
try:
    USER = pwd.getpwuid(int(os.environ["PKEXEC_UID"])).pw_name
except KeyError:
    try:
        USER = os.environ["SUDO_USER"]
    except KeyError:
        USER = getpass.getuser()

VERSION = "1.0.0"

USAGE = """
SSHManager, easy way to remember your ssh conections.

Usage:
    sshmanager init
    sshmanager ( -c | --connect )
    sshmanager ( -h | --help )
    sshmanager ( -v | --version )
    sshmanager ( -e | --export )

Commands:
    init                Initialize a SSHManager profile.
    connect             Generate a new conection.
    c                   Short way to connect command.

Example:
    sshmanager c
"""
