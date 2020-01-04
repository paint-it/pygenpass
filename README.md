# Genpass

### How to run project?
* Fork this project on your GitHub account

* Create virtual environment on your local machine
```nashorn js
$ python3 -m venv <name_of_virtualenv>

``` 
* Activate virtual environment 
```nashorn js

$ source <name_of_virtualenv>/bin/activate

```
* Make a local directory

* Clone project in your directory
```nashorn js
$ git clone https://github.com/paint-it/genpass.git

```
* Install setup.py
```nashorn js
$ python3 setup.py install

```
* Use command **manpass** 

#### Command line options
```sh 
$ manpass
 
Options:
  --help  Show this message and exit.

Commands:
  createpass  Enter required data
  savepass    Provide your password
  showpass    Printing data
```
#### Examples
* This command will ask for portal name and will create random password
```sh 
$ manpass createpass
Enter portal name [None]: 
```
* This command will ask for portal name and existing password
```sh
$ manpass savepass
Enter portal name [None]:
Enter your password [None]:
```
* This command will show password of particular portal
```nashorn js
$ manpass showpass
Enter portal name [None]:
```

### How to contribute to this project?
* Please read [contributing.md](https://github.com/paint-it/genpass/blob/master/contributing.md)

### Information about libraries used in this project?
* [**Click**](https://pypi.org/project/click/) - It is a third party tool which we have used for creating commands. We have commands like ```createpass```, ```savepass```,```showpass```

* [**Diceware**](https://pypi.org/project/diceware/) - It is used to generate random passsword for user. As we are managing these passwords


