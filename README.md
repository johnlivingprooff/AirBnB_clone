# AirBnB Clone Project

This Project is aimed to build a clone of the AirBnB website, using technologies that include: Python packages, MySQL, Web Framework, RESTful API, etc.

## The Console

**The Command interpreter**
In our project, the console serves as a robust utility for data management, allowing you to create a flexible data model. With this console, you can efficiently handle object operations such as creation, updating, and deletion through a command interpreter.

_**Key Features**_

- Create, modify, and delete objects
- Store & Persist Objects to a ```json``` file

## Deployment

To deploy the command interpreter run:

```bash
  $ ./console.py

  (hbnb) 
```

To use the command interpreter, simply type in any of these commands: ```create```, ```update```, ```delete``` to manipulate objects, and ```help``` to see all the available commands to utilize  

***Starting the Console:***

First clone the repository to you local device:
```bash
$ git clone https://github.com/johnlivingprooff/AirBnB_clone.git

```
Then enter into the repository:
```bash
$ cd AirBnB_clone/
```
Run the `console.py` file
```bash
$ ./console.py
```
```bash
(hbnb) 
```
This would start the `console`, to use the console, we can use any of above commands, e.g.

## Create an Object:

```bash
(hbnb) create User
0c4d4ec-51c5-4741-8bbe-17ba0c0b65f0
(hbnb)
```
This creates a User class object, and prints out the `User.id`

## Show an Object:
This shows the string representation of an Object, to find out more about the `show` command, you could do this:
```bash
(hbnb) ? show
```
```bash
This command shows the string representation an Object
Usage: show <class_name> <class_id>
(hbnb) 
```
***Example:***
```bash
(hbnb) show User 70c4d4ec-51c5-4741-8bbe-17ba0c0b65f0
[User] (70c4d4ec-51c5-4741-8bbe-17ba0c0b65f0) {'id': '70c4d4ec-51c5-4741-8bbe-17ba0c0b65f0', 'created_at': datetime.datetime(2023, 12, 9, 14, 26, 45, 351538), 'updated_at': datetime.datetime(2023, 12, 9, 14, 26, 45, 351564)}
(hbnb) 
```

## Delete an Object:
This deletes an Object from storage, to find out more about the `destroy` command, you could do this:
```bash
(hbnb) ? destroy
```
```bash
This command destroys an Object instance
Usage: destroy <class_name> <class_id>
(hbnb) 
```
***Example:***
```bash
(hbnb) destroy User 70c4d4ec-51c5-4741-8bbe-17ba0c0b65f0
(hbnb) show User 70c4d4ec-51c5-4741-8bbe-17ba0c0b65f0
** no instance found **
(hbnb) 
```
