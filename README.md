# Library-Manager

This concole application allows you to manage your own virtual library. You can do several operations with it such as: adding, deleting, printing, searching and changing.

## Install

For beginning, you should install git and python. If it already exists, open your terminal and switch to particular directory wich you want by `cd [path]` command. Then, use the following command:

`git clone https://github.com/artgor261/Library-Manager.git`

Or you can install this project like `zip-archieve` by `GitHub` GUI on the project page.

## Usage

The project consists of three files: 

1. `lib_manager.py` - main file
2. `book.py` - file which stores a Book class implementation
3. `library.py` - file which stores a Library class implementation

Switch to project directory in your terminal. Then, run the file `lib_manager.py`:

`py lib_manager.py`

Or do this by GUI in your IDE.

After that you should print a json file's path. It can be either relative or absolute. If you printed relative path, the program will find your file in the project directory by default. If file doest not exist, the program will create it into the project directory.

Then you can choose some operations:

1) `add` - adding the book into json file
2) `del` - deleting the book from json file
3) `search` - searching the book or sequence of books based on printed search string
4) `all` - printing all books from json file
5) `status` - change status of particular book. `true` equal `exist`, `false` equal `don't exist`.
6) `end` - quit the program

### add

Print add in terminal. You should input three book's features: `title`, `author` and `year`. For example:

```
Print command: add
Title: War and Peace
Author: Lev Tolstoy
Year: 1863
```

Then, you can check the json file. It will be increased by one object.

### del

Print del. You should input book's ID. Then, check your json file. The item will be deleted. For example:

```
Print command: del
Print book's ID: 2
```

### search

Print search in terminal. Then, you should input a keyword or list of keywords. The program will be searching books based on this string only by values of three book's features such as `title`, `author` and `year`. For example:

```
Print command: search
Search: George Orwell
```

The program returns a list of relevant books:

```
ID: 1,
Title: 1984,
Author: George Orwell,
Year: 1949,
Status: True


ID: 2,
Title: Animal Farm: A Fairy Story,
Author: George Orwell,
Year: 1945,
Status: True
```

## status

After printing status in terminal, you should input the book's id. Then, the program will automatically change the status. For example:

`Print book's ID: 2`

If you check your json file, you will see that book's status was changed.










