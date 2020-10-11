# importing the required modules
import os
import sys
import sqlite3
import logger
import constants
import pyinputplus as pyip
import argparse
from datetime import datetime
from pprint import pprint
from tabulate import tabulate

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
                self.init()
            else:
                # Exit from init
                print("Dont remove!")

        else:
            print("Creating new database...")
            conn = sqlite3.connect("ssh-manager.db")
            # The table structure for save configuration of conections
            conn.execute('''CREATE TABLE SSH(id INTEGER PRIMARY KEY AUTOINCREMENT,
                alias TEXT NOT NULL,
                user TEXT NOT NULL,
                host TEXT NOT NULL,
                port TEXT DEFAULT '22',
                is_using_pem INTEGER DEFAULT 0,
                pem_route TEXT,
                created_at TEXT,
                updated_at TEXT);''')
            print("Database created.")
            # ASk for save the first ssh conection
            answer = pyip.inputChoice(['yes', 'no', 'y','n'], "Do you want to add your first ssh conection?(yes/no): ")
            if answer in ['y', 'yes']:
                #remove old database and re-run this method
                self.new()
            else:
                # Exit from init
                print('Init success, for start using add new conections')
            # closing the connection
            conn.close()

    def new(self):
        print("Please enter the necesary data for save and create conections")
        user = pyip.inputStr("User name: ")
        host = pyip.inputStr("Host name: ")
        # Port
        port = pyip.inputStr("Port (default 22): ", blank=True)
        if port == "":
            port = "22"
        # If using pem
        is_using_pem = pyip.inputChoice(['yes', 'no', 'y','n'], "Do you use a pem for this conection?(yes/no): ")
        if is_using_pem in ['y', 'yes']:
            # Remove old database and re-run this method
            is_using_pem = 1
            pem_route = pyip.inputStr("Please give us the route to the pem(ex: /home/ubuntu/mykey.pem): ")
        else:
            is_using_pem = 0
            pem_route = ""
        # An alias
        alias = pyip.inputStr("Finally choice an alias for make it easy to find: ")

        query = "INSERT INTO SSH(alias, user, host, port, is_using_pem, pem_route, created_at, updated_at) VALUES (?,?,?,?,?,?,?,?)"
        data = (alias, user, host, port, is_using_pem, pem_route,datetime.now().strftime("%Y-%m-%d %H:%M:%S"),datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
        conn = sqlite3.connect("ssh-manager.db")
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        conn.close()

    def list(self):
        query = "SELECT id, alias, user || '@' || host || ':' || port, updated_at  FROM SSH"
        conn = sqlite3.connect("ssh-manager.db")
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print(tabulate(rows, headers=["id", "alias", "host" ,"last_update"]))

        conn.close()



main()
