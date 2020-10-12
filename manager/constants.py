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

TITLE = """
         _
 ___ ___| |_ ._ _ _  ___ ._ _  ___  ___  ___  _ _
<_-<<_-<| . || ' ' |<_> || ' |<_> |/ . |/ ._>| '_>
/__//__/|_|_||_|_|_|<___||_|_|<___|\_. |\___.|_|
                                   <___'
Easy way to remember your ssh conections.
"""

USAGE = """
Usage:
    sshmanager init
    sshmanager (  c |   connect )
    sshmanager (  n |   new )
    sshmanager (  l |   list )
    sshmanager (  r |   remove )
    sshmanager (  u |   update )
    sshmanager (  e |   export )
    sshmanager (  i |   import )
    sshmanager ( -h | --help )
    sshmanager ( -v | --version )

Commands:
    init                Initialize a SSHManager profile.
    connect             Create a new ssh conection to the give id record.
    new                 Save a new data conection.
    remove              Remove a data conection.
    update              Update a data conection.
    list                List available conections.
    export              Export the entired db.
    import              Import the entired db from another sshmanager.

Example:
    sshmanager connect 2
    sshmanager export -p /home/ubuntu -e csv
"""
