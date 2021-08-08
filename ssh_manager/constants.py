import os
import getpass
import pwd

USER = getpass.getuser()
USER_HOME = pwd.getpwnam(USER).pw_dir

CONFIG_DIR = os.path.join(os.path.expanduser("~{0}".format(USER)), ".ssh-manager")

VERSION = "0.0.1"
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
    sshmanager (  e |   export )
    sshmanager (  i |   import )
    sshmanager ( -h | --help )
    sshmanager ( -v | --version )

Commands:
    init                Initialize a SSHManager profile.
    connect             Create a new ssh conection from a record.
    new                 Create new record.
    remove              Remove a record.
    list                List available conections.
    export              Export the entire db.
    import              Import the entire db from another sshmanager.

Example:
    sshmanager connect
    sshmanager export --path /home/ubuntu
"""
