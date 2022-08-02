# 0x00. AirBnB clone - The console

## Description
This repository contains the first tasks of the AirBnB clone project for ALX Holberton.
During this first part of the project we had to:
* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## Files description
* **AUTHORS** This file has a list of individuals that contributed content to the repository.
* **console.py** This file contains a command line interpreter limited to a specific use case. In our case, we want to be able to manage the objects in our project using this console.
* **models** This folder contains all the Class modules of the project, and a folder called engine.
* **tests** This folder contains all the UNITTEST of every module stored in the models folder and the TEST of the console.py file.

## Usage
The console (console.py) works like this in interactive mode:
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
But also in non-interactive mode:
```
$ echo "help" | ./console.py
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

# AUTHORS
* Mardochée GNERAN
* Abdoul MAHAM 
