#!/usr/bin/python3
"""Defines the HBnB console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """add empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
