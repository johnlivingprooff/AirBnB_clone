#!/usr/bin/python3
"""Defines entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """A class that inherits a suclass named Cmd in a module named cmd"""

    prompt = '(hbnb) '

    def do_create(self, class_name):
        """Creates a new instance of class and saves it"""
        if not class_name:
            print("** class name missing **")
        elif class_name != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def help_quit(self):
        """docstring for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """docstring for EOF command"""
        print("EOF command to exit the program")

    def emptyline(self):
        """Does nothing if it's an empty line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit Program"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
