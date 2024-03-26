#!/usr/bin/python3
'''
Contains entry point of command interpretter
'''
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

cmd_Class_Dict = {"BaseModel": BaseModel,
              "User": User,
              "Place": Place,
              "State": State,
              "Amenity": Amenity,
              "Review": Review,
              "City": City}


class HBNBCommand(cmd.Cmd):
    '''
    console class
    
    Attributes:
        prompt (str): The command prompt.
    '''
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "State": State,
               "Amenity": Amenity,
               "Review": Review,
               "City": City}

    def do_quit(self, command):
        '''
        Quit command to exit the program
        '''
        exit()

    def help_quit(self):
        '''
        Help for quitting the program
        '''
        print('Quit command to exit the program\n')

    def do_EOF(self, command):
        '''
        End of file cmd
        '''
        print()
        exit()

    def help_EOF(self):
        '''
        Help for EOF cmd
        '''
        print('EOF command to exit the program\n')

    def emptyline(self):
        '''
        Guard against 'enter' cmd
        '''
        pass

    def do_create(self, argsv):
        '''
        cmd Create new instance of BaseModel
        '''
        if not argsv:
            print('** class name missing **')
            return
        elif argsv in cmd_Class_Dict:
            for key, value in cmd_Class_Dict.items():
                if key == argsv:
                    new_instance = cmd_Class_Dict[key]()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        '''
        Help for create cmd
        '''
        print('Create command to create new instance\n')

    def do_show(self, argsv):
        '''
        cmd Print str repr of an instance
        bases on class name and id
        '''
        new_instance = argsv.partition(' ')
        cmd_class_name = new_instance[0]
        cmd_class_id = new_instance[2]

        if not argsv:
            print('** class name missing **')
            return
        if cmd_class_name not in cmd_Class_Dict:
            print("** class doesn't exist **")
            return
        if not cmd_class_id:
            print('** instance id missing **')
            return
        new_key = cmd_class_name + '.' + cmd_class_id
        try:
            print(storage._FileStorage__objects[new_key])
        except BaseException:
            print("** no instance found **")

    def help_show(self):
        '''
        Help for showing cmd
        '''
        print('Show command to show string representation\n')

    def do_destroy(self, argv):
        '''
        cmd Deletes an instance basesd on
        class name and id
        '''
        new_args = ""
        cmd_class_name = ""
        cmd_class_id = ""
        try:
            new_args = argv.split(" ")
            cmd_class_name = new_args[0]
            cmd_class_id = new_args[1]
        except BaseException:
            pass
        if not cmd_class_name:
            print('** class name missing **')
        elif cmd_class_name not in cmd_Class_Dict:
            print("** class doesn't exist **")
        elif not cmd_class_id:
            print("** instance id missing **")
        else:
            new_key = cmd_class_name + '.' + cmd_class_id
            try:
                del(storage._FileStorage__objects[new_key])
                storage.save()
            except KeyError:
                print("** no instance found **")

    def help_destroy(self):
        '''
        cmd Help for destroy
        '''
        print('Destroy command to show delete an instance based\
        on class name and id\n')

    def do_all(self, argv):
        """
        cmd Prints all instances based on class
        """
        new_list = []
        if argv:
            if argv not in cmd_Class_Dict:
                print("** class doesn't exist **")
                return
            for key, value in storage._FileStorage__objects.items():
                if key.split(".")[0] == argv:
                    new_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                new_list.append(str(value))
        print(new_list)

    def help_all(self):
        """
        cmd displays all instances [based on class if chosen]
        """
        print("displays all instances [based on class if chosen]")
        print("all [class]")

    def do_update(self, args):
        """
        cmd updates object
        """
        new_object = ""
        cmd_class_name = ""
        cmd_class_id = ""
        cmd_at_name = ""
        cmd_at_val = ""
        cmd_objects = ""
        try:
            new_object = args.split(" ")
            cmd_class_name = new_object[0]
            cmd_class_id = new_object[1]
            cmd_at_name = new_object[2]
            cmd_at_val = new_object[3]
            cmd_objects = storage._FileStorage__objects.items()
        except (IndexError, NameError):
            pass
        if not cmd_class_name:
            print("** class name missing **")
            return
        if cmd_class_name not in cmd_Class_Dict:
            print("** class doesn't exist **")
            return
        if not cmd_class_id:
            print("** instance id missing **")
            return
        if not cmd_at_name:
            print("** attribute name missing **")
            return
        if not cmd_at_val:
            print("** value missing **")
            return

        new_key = cmd_class_name + "." + cmd_class_id
        cmd_no_touchy = ["id", "created_at", "updated_at"]
        for key, value in storage._FileStorage__objects.items():
            if new_key not in cmd_no_touchy:
                if new_key == key:
                    setattr(value, cmd_at_name, cmd_at_val)
                    new = value
                    new.save()
        print("** no instance found **")
        if new_key not in storage._FileStorage__objects.keys():
            print("** no instance found **")

    def help_update(self):
        """
        cmd Help for update
        """
        print("updates and objects with new information")
        print("update <class> <id> <attribute> <value>")

    def do_count(self, argv):
        """
        cmd count number of instances by class
        """
        counter = 0

        new_arg = argv.split(" ")
        if new_arg[0] not in cmd_Class_Dict:
            print("** class doesn't exist **")
            return
        new_list = storage._FileStorage__objects.items()
        for key, value in new_list:
            temp_key = str(key)
            new_key = temp_key.split(".")
            if new_key[0] == new_arg[0]:
                counter = (counter + 1)
        print(counter)

    def help_count(self):
        """
        cmd counts the number of instances of a class
        """
        print("count <class>")

    def default(self, line):
        '''
        cmd Advanced
        '''
        _cmd = storage.all()
        if '.' in line:
            cmd_parse = line.split('.')
            cmd_class_name = cmd_parse[0]
            method_name = cmd_parse[1]
            if cmd_class_name in cmd_Class_Dict:
                if method_name[0:5] == 'all()':
                    self.do_all(cmd_class_name)
                if method_name[0:7] == 'count()':
                    self.do_count(cmd_class_name)
                if method_name[0:5] == 'show(':
                    method_name2 = method_name.split('"')
                    show_id = method_name2[1]
                    argv = cmd_class_name + ' ' + show_id
                    print(argv)
                    self.do_show(argv)
                if method_name[0:8] == 'destroy(':
                    method_name2 = method_name.split('"')
                    show_id = method_name2[1]
                    argv = cmd_class_name + ' ' + show_id
                    self.do_destroy(argv)
                if method_name[0:7] == 'update(':
                    method_name2 = method_name.split('"')
                    show_id = method_name2[1]
                    show_att_name = method_name2[3]
                    show_att_val = method_name2[5]
                    argv = cmd_class_name + ' ' + show_id +\
                        ' ' + show_att_name + ' ' + show_att_val
                    print(argv)
                    self.do_update(argv)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
