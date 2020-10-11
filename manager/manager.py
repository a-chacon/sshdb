# importing the required modules
import os
import sys
import sqlite3
import logger
import constants
import pyinputplus as pyip
import argparse

from logger import logger

def main():
    """Main function"""
    try:
        """Run user's input command."""

        # Initial log values
        logger.debug("###########################")
        logger.debug("### NEW PROCESS STARTED ###")
        logger.debug("###########################")
        logger.debug(sys.argv)
        logger.debug("USER: {0}".format(constants.USER))

        SSHManager()
    except KeyboardInterrupt:
        print("\nQuitting...")
        sys.exit(1)


class SSHManager(object):
    """docstring for SSHManager."""

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog="sshmanager",
            add_help=False
        )

        parser.add_argument("command", nargs="?")
        parser.add_argument("-v", "--version", required=False, action="store_true")
        parser.add_argument("-h", "--help", required=False, action="store_true")

        args = parser.parse_args(sys.argv[1:2])

        logger.debug("Main argument\n{0}".format(args))

        if args.version:
            print("SSHManager CLI v.{}".format(constants.VERSION))
            parser.exit(1)
        elif not args.command or not hasattr(self, args.command) or args.help:
            print(constants.USAGE)
            parser.exit(1)

        getattr(self, args.command)()


    def init(self):
        if os.path.isfile('ssh-manager.db'):

            print("A database is already configured.")
            answer = pyip.inputChoice(['yes', 'no', 'y','n'], "Do you want remove it?(yes/no): ")

            if answer in ['y', 'yes']:
                # Remove old database and re-run this method
                print("remove it")
                os.remove('ssh-manager.db')
            else:
                # Exit from init
                print("Dont remove!")

        else:
            print("Creating new database...")
            conn = sqlite3.connect("ssh-manager.db")
            # The table structure for save configuration of conections
            conn.execute('''CREATE TABLE SSH(id INT PRIMARY KEY NOT NULL,
                alias TEXT NOT NULL,
                user TEXT NOT NULL,
                host TEXT NOT NULL,
                port TEXT DEFAULT '22',
                pem_route TEXT,
                created_at TEXT,
                updated_at TEXT);''')
            print("Database created.")
            # ASk for save the first ssh conection
            answer = pyip.inputChoice(['yes', 'no', 'y','n'], "Do you want to add your first ssh conection?(yes/no): ")
            if answer in ['y', 'yes']:
                #remove old database and re-run this method
                print("call add method")
            else:
                # Exit from init
                print("Dont remove!")
            # closing the connection
            conn.close()

    def new(self):
        print("hola")
        



main()
