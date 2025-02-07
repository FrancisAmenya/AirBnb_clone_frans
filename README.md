# <center>0x00. AirBnB clone - The console</center>

## Background
This project is the first part ongoing Airbnb Clone.

In this project I am building the backend of the Airbnb. I created a Command Line Interpreter (CLI). This is similiar the Shell project in C, but with Python's high level `cmd` framwork makes this as simple as importing `cmd` and beginning each function with `do_*`.

The command intepreter is written in the console.py file. It has several methods which allow us to manage the objects of the project:

* Create a new object (ex: a new User or * a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

The CLI is linked to several other classes:
* BaseModel, User, FileStorage, amenity, City, State, Place, Review

`BaseModel` is the parent class. It takes care of initiliazing, serializing and deserializing each instance.

The flow of the serialization and deserialization is:
`instantce <-> Dictionary <-> JSON string <-> file`

In file_storage.py I created a storage engine for the project. The methods for creating a new instance, saving and reloading it are in the `FileStorage` class.

The following is a tree diagram of this projects folders and files:

📦models\
 ┣ 📂engine\
 ┃ ┗ 📜[file_storage.py](models/engine/file_storage.py)\
 ┣ 📜amenity.py\
 ┣ 📜[base_model.py](models/base_model.py)\
 ┣ 📜[city.py](models/city.py)\
 ┣ 📜[place.py](models/place.py)\
 ┣ 📜[review.py](models/review.py)\
 ┣ 📜[state.py](models/state.py)\
 ┗ 📜[user.py](models/user.py)

 The Unit Tests are:

📦tests\
 ┣ 📂test_models\
 ┃ ┣ 📂test_engine\
 ┃ ┃ ┗📜[test_file_storage.py](tests/test_models/test_engine/test_file_storage.py)\
 ┃ ┣ 📜[test_amenity.py](tests/test_models/test_amenity.py)\
 ┃ ┣ 📜[test_base_model.py](tests/test_models/test_base_model.py)\
 ┃ ┣ 📜[test_city.py](tests/test_models/test_city.py)\
 ┃ ┣ 📜[test_place.py](tests/test_models/test_place.py)\
 ┃ ┣ 📜[test_review.py](tests/test_models/test_review.py)\
 ┃ ┣ 📜[test_state.py](tests/test_models/test_state.py)\
 ┃ ┗ 📜[test_user.py](tests/test_models/test_user.py)

## Use
Run the console:
```
./console.py
```
This is the start of the console:
```
(hbnb)
```
Type `help` for a list of commands:
```
(hnbn) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hnbn)        
```
Typing help followed by a command returns a useful text that describes the command, for example:
 ```
 (hnbn) help create
Create command to create new instance

(hnbn)
 ```
 To create a new instance of a class, type `create` followed by a class name:
 ```
 (hnbn) create User
2320c56a-574f-43bb-ab2d-d2cfce74ae47
 ```

 This returns a unique id from the `UUID` import class. This is a unique number that is tagged to an instance. The `show` command displays a string representation of an instance based on it's class name and user id:
 ```
 (hnbn) show User 2320c56a-574f-43bb-ab2d-d2cfce74ae47
[User] (2320c56a-574f-43bb-ab2d-d2cfce74ae47) {'id': '2320c56a-574f-43bb-ab2d-d2cfce74ae47', 'created_at': datetime.datetime(2020, 2, 19, 22, 25, 51, 185609), 'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 25, 946631)}
 ```

 The `create` commands saves a dictionary representation of the instance, which includes:
* Class name
* Unique ID number
* Created at (date/time)
* Updated at (date/time)

The `update` command allows users to add additional attributes to the dictionary representation:
```
(hbnb) update User 2320c56a-574f-43bb-ab2d-d2cfce74ae47 first_name "Geoff"
```

Using `show` again, I see that the `JSON` file now reads:
```
(hbnb) show User 2320c56a-574f-43bb-ab2d-d2cfce74ae47
[User] (2320c56a-574f-43bb-ab2d-d2cfce74ae47) {'id': '2320c56a-574f-43bb-ab2d-d2cfce74ae47', 'created_at': datetime.datetime(2020, 2, 19, 22, 25, 51, 185609), 'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 25, 946631), 'first_name': 'Geoff'}
```

Further, the `destroy` method deletes the instance, so when I run it:
```
(hnbn) destroy User 2320c56a-574f-43bb-ab2d-d2cfce74ae47
```

And try to `show` it again, I get this message:
```
** no instance found **
```
The instance has been deleted.

The `all` command prints a string representation of all instances, regardless of it's class.

Finally, the `show`, `all`, `update` and `destroy` commands can also be called with the following syntax:
```
(hbnb) <class name>.command()
``` 
For example, `User.all()` is equivelent to the `all` command.

Commands that require an `id` can be called like this:
```
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
```


In addition to the previoulsy mentioned commands, you can find the number of instances of a class using the `count` command in the above described format:
```
(hbnb) <class name>.count()
```
<br>
<br>

0x00. AirBnB clone - The console

Francis Amenya <amenyafrancis@gmail.com>
