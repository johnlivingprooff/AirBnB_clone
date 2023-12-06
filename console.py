#!/usr/bin/python3
"""Defines entry point of the command interpreter"""

import cmd
import models
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
    all_classes = [ "Amenity", "BaseModel", "City", "Place", "State", "Review", "User" ]

    def do_create(self, class_name):
        """Creates a new instance of class and saves it"""
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval("{}()".format(class_name))
            new_instance.save()
            print(new_instance.id)

    def help_create(self):
        """Docstring for create command"""
        print("Creates a new instance of specified class")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        all_instances = models.storage.all()

        if key not in all_instances:
            print("** no instance found **")
        else:
            print(all_instances[key])

    def help_show(self):
        """Docstring for show command"""
        print("Prints the string representation of \
              an instance based on the class name and id")
        print("Usage: show <class_name> <class_id>")

    def do_destroy(self, line):
        """Destroys an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        all_instances = models.storage.all()

        if key not in all_instances:
            print("** no instance found **")
        else:
            del all_instances[key]
            models.storage.save()

    def help_destroy(self):
        """Docstring for destroy command"""
        print("Deletes an instance based on class name and id")

    def do_all(self, line):
        """Prints the string representation of all instances or
        not on the class name
        """
        args = line.split()
        all_objects = models.storage.all()

        if len(args) == 0:
            all_instances = []
            for value in all_objects.values():
                str_obj = str(value)
                all_instances.append(str_obj)
            print(all_instances)
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            all_instances = []
            for obj in all_objects.values():
                if args[0] == obj.__class__.__name__:
                    all_instances.append(str(obj))
            print(all_instances)

    def help_all(self):
        """Docstring for help command"""
        print("Prints the string representation of all instances")

    def do_update(self, line):
        """Updates an instance based on class name and id by
        adding or updating attributes
        """
        args = line.split()
        all_instances = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in all_instances:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = f"{class_name}.{obj_id}"
            attribute = args[2]
            attr_value = args[3]
            for k, value in all_instances.items():
                if k == key:
                    if attr_value.isdecimal():
                        setattr(value, attribute, int(attr_value))
                    else:
                        try:
                            setattr(value, attribute, float(attr_value))
                        except ValueError:
                            setattr(value, attribute, str(attr_value))
            models.storage.save()

    def help_update(self):
        """Docstring for update command"""
        print("Updates an instance with new attributes or values")

    def help_quit(self):
        """docstring for quit command"""
        print("Quit command to exit the program")

    help_EOF = help_quit

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
