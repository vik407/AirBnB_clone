#!/usr/bin/python3
""" Console module. Used for user command line intructions."""

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Console class. Used for user command line intructions."""

    prompt = '(hbnb) '
    HBNBCommand_classes = ['BaseModel', 'User',
                           'State', 'City', 'Amenity', 'Place', 'Review']

    def do_create(self, line):
        """\nCreate new instance, saves it (to JSON file) and prints the id.\n
        -> Usage: (hbnb) create <class_name>\n"""
        if not line:
            print('** class name missing **')
            return

        args = line.split()
        if args[0] not in self.HBNBCommand_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(args[0] + '()')
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """\nPrints string representation of an instance.\n
        -> Usage: (hbnb) show <class_name> <id>\n"""
        if not line:
            print('** class name missing **')
            return

        args = line.split()
        if args[0] not in self.HBNBCommand_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        if len(args) >= 2:
            try:
                print(storage.all()[args[0] + '.' + args[1]])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """\nDeletes an instance based on the class name and id.\n
        -> Usage: (hbnb) destroy <class_name> <id>\n"""
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        if args[0] not in self.HBNBCommand_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        if len(args) >= 2:
            try:
                del storage.all()[args[0] + '.' + args[1]]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """\nPrints all string representation of all instances based or not on\n
        the class name.\n
        -> Usage: (hbnb) all <class_name>\n
        -> Usage: (hbnb) all\n"""
        if not line:
            a = []
            for key, value in storage.all().items():
                a.append(str(value))
            if len(a) != 0:
                print(a)
        else:
            args = line.split()
            if args[0] not in self.HBNBCommand_classes:
                print("** class doesn't exist **")
                return
            a = []
            for key, value in storage.all().items():
                if str(key.split('.')[0]) == args[0]:
                    a.append(str(value))
            if len(a) != 0:
                print(a)

    def do_update(self, line):
        """\nUpdates an instance based on the class name and id by adding or
        \nupdating attribute (save the change into the JSON file)\n
        -> (hbnb) update <ClassName> <id> <attr_name> "<attr_value>"\n"""
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        if len(args) >= 1 and args[0] not in self.HBNBCommand_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        if len(args) >= 2:
            try:
                storage.all()[args[0] + '.' + args[1]]
            except KeyError:
                print("** no instance found **")
                return
        if len(args) == 2:
            print('** attribute name missing **')
            return
        if len(args) == 3:
            print('** value missing **')
            return
        if len(args) == 4:
            try:
                try:
                    if '.' in args[3]:
                        value = float(args[3])
                    else:
                        value = int(args[3])
                except ValueError:
                    value = str(args[3]).strip("\"':")
                setattr(storage.all()[args[0] + '.' +
                                      args[1]], args[2].strip("\"':"), value)
                storage.save()
            except KeyError:
                print("** no instance found **")
                return

    def do_count(self, line):
        """Counts the number of instances of <class_name>\n
        """
        if not line:
            return
        args = line.split()
        if args[0] not in self.HBNBCommand_classes:
            return
        counter = 0
        for key, value in storage.all().items():
            if str(key.split('.')[0]) == args[0]:
                counter += 1
        print(counter)

    def precmd(self, line):
        """Alternative parser for inputs in the form: <ClassName>.command\n
        """
        args = line.split('.', 1)
        if len(args) == 2:
            try:
                clase = args[0]
                args = args[1].split('(', 1)
                comando = args[0]
                id = ''
                argumentos = ''
                if len(args) == 2:
                    args = args[1].split(')', 1)
                    if len(args) == 2:
                        id = args[0]
                        argumentos = args[1]
                line2 = comando + ' ' + clase + ' ' + id + ' ' + argumentos
                return line2
            except IndexError:
                return line
        else:
            return line

    def do_quit(self, line):
        """Quit the program!"""
        return True

    def do_EOF(self, line):
        """Quit the program!"""
        print()
        return True

    def emptyline(self):
        """Do nothing if empty line is entered!"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
