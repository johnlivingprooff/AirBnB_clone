#!/usr/bin/python3
"""The Command Interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class that defines the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, *args):
        """Quits the console program"""
        return True

    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
