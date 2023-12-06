#!/usr/bin/python3
"""Defines entry point of the command interpreter"""

import cmd, os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """A class that inherits a suclass named Cmd in a module named cmd"""

    prompt = '(hbnb) '

    def help_quit(self):
        """docstring for quit command"""
        print("Quit command to exit the program")

    def emptyline(self):
        """Does nothing if it's an empty line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the program, on Ctrl+D [EOF]"""
        print()
        exit() # same as return True 
    
    do_q = do_quit
    def help_EOF(self):
        """Help Doc for EOF"""
        print("Exits the program with a newline")

    def do_create(self, args):
        """creates an instance of a model class"""
        if not args:
            print("** class name missing **")
            return
        
        separate_args = args.split(" ")
        class_name = separate_args[0]
        if class_name == "BaseModel":
            instance = BaseModel()
            print(instance.id)
            storage.save()
        else:
            print("** class doesn't exist **")
            return

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

    def do_clear(self):
        """Clears the screen"""
        os.system('clear')

    def help_clear(self):
        """Help documentation for clear screen"""
        print("Clears the screen")

    do_cls = do_clr = do_clear

if __name__ == '__main__':
    HBNBCommand().cmdloop()
