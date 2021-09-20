import os
import getpass
import pwd

USER = getpass.getuser()
USER_HOME = pwd.getpwnam(USER).pw_dir

CONFIG_DIR = os.path.join(os.path.expanduser("~{0}".format(USER)), ".sshdb")

VERSION = "0.0.1"
TITLE = """

 ____ ____ ____ ____ ____
||s |||s |||h |||d |||b ||
||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|


"""
USAGE = """
Usage:
    sshdb init
    sshdb (  c | connect    )
    sshdb (  n | new        )
    sshdb (  l | list       )
    sshdb (  r | remove     )
    sshdb (  e | export     )
    sshdb (  i | import     )
    sshdb ( -h | --help     )
    sshdb ( -v | --version  )

Commands:
    init                Initialize a sshdb profile.
    connect             Create a new ssh conection from a record.
    new                 Create new record.
    remove              Remove a record.
    list                List available conections.
    export              Export the entire db.
    import              Import the entire db from another sshdb.

Example:
    sshdb connect
    sshdb export --path /home/ubuntu
"""
