import os
import getpass
import pwd

USER = getpass.getuser()
USER_HOME = pwd.getpwnam(USER).pw_dir

CONFIG_DIR = os.path.join(os.path.expanduser("~{0}".format(USER)), ".ssh-manager")

VERSION = "0.0.1"
TITLE = """
         _
 ___ ___| |_ _____ ___
|_ -|_ -|   |     | -_|
|___|___|_|_|_|_|_|___|

"""
USAGE = """
Usage:
    sshme init
    sshme (  c |   connect )
    sshme (  n |   new )
    sshme (  l |   list )
    sshme (  r |   remove )
    sshme (  e |   export )
    sshme (  i |   import )
    sshme ( -h | --help )
    sshme ( -v | --version )

Commands:
    init                Initialize a sshme profile.
    connect             Create a new ssh conection from a record.
    new                 Create new record.
    remove              Remove a record.
    list                List available conections.
    export              Export the entire db.
    import              Import the entire db from another sshme.

Example:
    sshme connect
    sshme export --path /home/ubuntu
"""
