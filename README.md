# 0x00. AirBnB clone - The console

## First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

* Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object


## Requirements

### Python Scripts

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7 or more)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Python Unit Tests

* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
We strongly encourage you to work together on test cases, so that you don’t miss any edge case


## How to use

The console works in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like a Shell)

```
$$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## How the program works

| Function | Description | Usage |
| ------ | ------ | ------ |
| create | Create new instance, saves it (to JSON file) and prints the id. | create <class_name>
| all | Prints all string representation of all instances based or not on | all [class_name]
| destroy | Deletes an instance based on the class name and id. | destroy <class_name> < id > 
| help | List available commands with "help" or detailed help with "help cmd". | help [command] |
| show | Prints string representation of an instance. | show <class_name> < id > |
| update | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) | update < ClassName > < id > <attr_name> "<attr_value>" |
| quit | Quit the program! | quit |


### Other files and folders
* monty.h - doubly linked list representation of a stack (or queue), opcode and its function and prototypes of all functions of the program.
* bc - test cases.
* bf - Other tasks in brainfuck languaje.

## Examples

```
(hbnb) 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help all

Prints all string representation of all instances based or not on

        the class name.

        -> Usage: (hbnb) all <class_name>

        -> Usage: (hbnb) all

(hbnb) all
(hbnb) create
** class name missing **
(hbnb) 
(hbnb) create Base
** class doesn't exist **
(hbnb) 
(hbnb) create BaseModel
9c95b576-fa67-4e7e-b341-2a9ff80c7422
(hbnb) 
(hbnb) create User
7782e0e3-14d4-4270-85a1-9a15ea5ffa86
(hbnb) 
(hbnb) all
["[BaseModel] (9c95b576-fa67-4e7e-b341-2a9ff80c7422) {'id': '9c95b576-fa67-4e7e-b341-2a9ff80c7422', 'created_at': '2020-02-19T10:39:00.987137', 'updated_at': '2020-02-19T10:39:00.987175', '__class__': 'BaseModel'}", "[User] (7782e0e3-14d4-4270-85a1-9a15ea5ffa86) {'id': '7782e0e3-14d4-4270-85a1-9a15ea5ffa86', 'created_at': '2020-02-19T10:39:06.809685', 'updated_at': '2020-02-19T10:39:06.809721', '__class__': 'User'}"]
(hbnb) 
(hbnb) all User
["[User] (7782e0e3-14d4-4270-85a1-9a15ea5ffa86) {'id': '7782e0e3-14d4-4270-85a1-9a15ea5ffa86', 'created_at': '2020-02-19T10:39:06.809685', 'updated_at': '2020-02-19T10:39:06.809721', '__class__': 'User'}"]
(hbnb) 
(hbnb) destroy
** class name missing **
(hbnb) 
(hbnb) destroy Base
** class doesn't exist **
(hbnb) 
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) 
(hbnb) destroy BaseModel 1
** no instance found **
(hbnb) 
(hbnb) destroy BaseModel 9c95b576-fa67-4e7e-b341-2a9ff80c7422
(hbnb) 
(hbnb) all
["[User] (7782e0e3-14d4-4270-85a1-9a15ea5ffa86) {'id': '7782e0e3-14d4-4270-85a1-9a15ea5ffa86', 'created_at': '2020-02-19T10:39:06.809685', 'updated_at': '2020-02-19T10:39:06.809721', '__class__': 'User'}"]
(hbnb) 
(hbnb) create City
b6759f36-d7dc-4eeb-a625-736c70844313
(hbnb) 
(hbnb) all
["[User] (7782e0e3-14d4-4270-85a1-9a15ea5ffa86) {'id': '7782e0e3-14d4-4270-85a1-9a15ea5ffa86', 'created_at': '2020-02-19T10:39:06.809685', 'updated_at': '2020-02-19T10:39:06.809721', '__class__': 'User'}", "[City] (b6759f36-d7dc-4eeb-a625-736c70844313) {'id': 'b6759f36-d7dc-4eeb-a625-736c70844313', 'created_at': '2020-02-19T10:40:06.817788', 'updated_at': '2020-02-19T10:40:06.817824', '__class__': 'City'}"]
(hbnb) 
(hbnb) show
** class name missing **
(hbnb) 
(hbnb) show City
** instance id missing **
(hbnb) 
(hbnb) show City b6759f36-d7dc-4eeb-a625-736c70844313
[City] (b6759f36-d7dc-4eeb-a625-736c70844313) {'id': 'b6759f36-d7dc-4eeb-a625-736c70844313', 'created_at': '2020-02-19T10:40:06.817788', 'updated_at': '2020-02-19T10:40:06.817824', '__class__': 'City'}
(hbnb) 
(hbnb) update
** class name missing **
(hbnb) 
(hbnb) update City
** instance id missing **
(hbnb) 
(hbnb) update City name
** no instance found **
(hbnb) 
(hbnb) update City b6759f36-d7dc-4eeb-a625-736c70844313
** attribute name missing **
(hbnb) 
(hbnb) update City b6759f36-d7dc-4eeb-a625-736c70844313 name
** value missing **
(hbnb) 
(hbnb) update City b6759f36-d7dc-4eeb-a625-736c70844313 name Pereira
(hbnb) 
(hbnb) show City b6759f36-d7dc-4eeb-a625-736c70844313
[City] (b6759f36-d7dc-4eeb-a625-736c70844313) {'id': 'b6759f36-d7dc-4eeb-a625-736c70844313', 'created_at': '2020-02-19T10:40:06.817788', 'updated_at': '2020-02-19T10:40:06.817824', 'name': 'Pereira', '__class__': 'City'}
(hbnb) 
(hbnb) quit
```

### Classes implemented


    class User
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string

    class State
    Public class attributes:
        name: string - empty string

    class City
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string

    class Amenity
    Public class attributes:
        name: string - empty string

    class Place
    Public class attributes:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string - empty list: it will be the list of Amenity.id later

    class Review
    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string


## Authors

* Victor Hernandez. [vik407](https://github.com/vik407)
* Leonardo Calderon J. - [LeoCJJ](https://github.com/leocjj)

02/19/2020
