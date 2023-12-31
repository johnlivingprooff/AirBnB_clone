#!/usr/bin/python3
"""Defines entry point of the command interpreter"""

import cmd
import re    # Module for Regular Expression
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from shlex import split
import models


def _parse(arg):
    """Using regular expressions to find curly braces
    and square brackets
    """
    curly_braces_match = re.search(r"\{(.*?)\}", arg)
    parentheses_match = re.search(r"\[(.*?)\]", arg)

    if curly_braces_match is None:
        if parentheses_match is None:
            return [token.strip(",") for token in split(arg)]
        else:
            tokens_list = split(arg[:parentheses_match.span()[0]])
            tokens = [token.strip(",") for token in tokens_list]
            tokens.append(parentheses_match.group())
            return tokens
    else:
        tokens_list = split(arg[:curly_braces_match.span()[0]])
        tokens = [token.strip(",") for token in tokens_list]
        tokens.append(curly_braces_match.group())
        return tokens


class HBNBCommand(cmd.Cmd):
    """A class that inherits a suclass named Cmd in a module named cmd"""

    prompt = '(hbnb) '
    all_classes = ["Amenity", "BaseModel", "City", "Place",
                   "State", "Review", "User"]

    def default(self, arg):
        """Default behaviour of cmd if input is invalid"""
        command_dict = {
                    "all": self.do_all,
                    "count": self.do_count,
                    "show": self.do_show,
                    "destroy": self.do_destroy,
                    "update": self.do_update,
                }
        match = re.search(r"\.", arg)
        if match:
            args = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])
            if match:
                command = [args[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in command_dict:
                    func_call = f"{args[0]} {command[1]}"
                    return command_dict[command[0]](func_call)
        print(f"*** Unknown syntax: {arg}")
        return False

    def do_create(self, class_name):
        """Creates a new instance of class and saves it"""
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval("{}()".format(class_name))
            models.storage.save()
            print(new_instance.id)

    def help_create(self):
        """Docstring for create command"""
        print("Creates a new instance of specified class")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = _parse(line)
        all_instances = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in all_instances:
            print("** no instance found **")
        else:
            print(all_instances[f"{args[0]}.{args[1]}"])

    def help_show(self):
        """Docstring for show command"""
        print("Prints the string repr based on class")

    def do_destroy(self, line):
        """Destroys an instance based on the class name and id"""
        args = _parse(line)
        all_instances = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in all_instances:
            print("** no instance found **")
        else:
            del all_instances[f"{args[0]}.{args[1]}"]
            models.storage.save()

    def help_destroy(self):
        """Docstring for destroy command"""
        print("Deletes an instance based on class name and id")

    def do_all(self, line):
        """Prints the string representation of all instances or
        not on the class name
        """
        args = _parse(line)
        all_objects = models.storage.all()

        if len(args) == 0:
            all_instances = []
            for obj in all_objects.values():
                all_instances.append(obj.__str__())
            print(all_instances)
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            all_instances = []
            for obj in all_objects.values():
                if args[0] == obj.__class__.__name__:
                    all_instances.append(obj.__str__())
            print(all_instances)

    def help_all(self):
        """Docstring for help command"""
        print("Prints the string representation of all instances")

    def do_update(self, line):
        """Updates an instance based on class name and id by
        adding or updating attributes
        """
        args = _parse(line)
        all_instances = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        elif f"{args[0]}.{args[1]}" not in all_instances:
            print("** no instance found **")
            return False
        elif len(args) == 2:
            print("** attribute name missing **")
            return False
        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            obj = all_instances[f"{args[0]}.{args[1]}"]
            if args[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = value_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = all_instances[f"{args[0]}.{args[1]}"]
            for key, value in eval(args[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key] in
                             {str, int, float})):
                    value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type(value)
                else:
                    obj.__dict__[key] = value
        models.storage.save()

    def help_update(self):
        """Docstring for update command"""
        print("Updates an instance with new attributes or values")

    def do_count(self, line):
        """Retrieves the number of instances of a class"""
        args = _parse(line)
        all_instances = models.storage.all()
        number_of_instances = 0

        for obj in all_instances.values():
            if args[0] == obj.__class__.__name__:
                number_of_instances += 1

        print(number_of_instances)

    def help_count(self):
        """Docstring for count method"""
        print("Returns number of instances of a class")

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
