#!/usr/bin/python3
"""Defines entry point of the command interpreter"""

import cmd
import os
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """A class that inherits a suclass named Cmd in a module named cmd"""

    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel, 'Amenity': Amenity,
        'City': City, 'Place': Place,
        'Review': Review, 'State': State,
        'User': User
    }

    def do_create(self, class_name):
        """Creates a new instance of class and saves it"""
        if not class_name:
            print("** class name missing **")
            return

        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = HBNBCommand.classes[class_name]()
            new_instance.save()
            print(new_instance.id)

    def help_create(self):
        """Help documentation for create"""
        print("Creates a new instance of specified class")

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return

        separate_args = args.split(" ")
        class_name = separate_args[0]
        if len(separate_args) > 1:
            class_id = separate_args[1]

        # for separate in separate_args:
        #     print(f"{separate}")

            if class_name != 'BaseModel':
                print("** class doesn't exist **")
                return

            key = f"{class_name}.{class_id}"
            try:
                print(FileStorage._FileStorage__objects[key])
            except KeyError:
                print("** no instance found **")

        else:
            print("** instance id missing **")

    def help_show(self):
        """Help Documentation for show command"""
        print("Prints the string representation of \
              an instance based on the class name and id")
        print("Usage: show <class_name> <class_id>")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """docstring for quit command"""
        print("Quit command to exit the program")

    do_exit = do_quit

    def do_EOF(self, line):
        """Exits the program, on Ctrl+D [EOF]"""
        print()
        exit()   # same as return True

    def help_EOF(self):
        """docstring for EOF command"""
        print("EOF command to exit the program")

    def emptyline(self):
        """Does nothing if it's an empty line"""
        pass

    def do_clear(self, line):
        """Clears the screen"""
        os.system('clear')

    def help_clear(self, line):
        """Help documentation for clear screen"""
        print("Clears the screen")

    do_cls = do_clr = do_clear


if __name__ == '__main__':
    HBNBCommand().cmdloop()
