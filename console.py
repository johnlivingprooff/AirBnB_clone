#!/usr/bin/python3
"""Defines entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """A class that inherits a suclass named Cmd in a module named cmd"""

    prompt = '(hbnb) '

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        pass

    def do_quit(self, line):
        return True

    do_EOF = do_quit
    help_EOF = help_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
