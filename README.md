# Genpass

### How to run project?
* Fork this project on youre github account.

* Create Virtual envirnment on your local machin
```nashorn js
$ python3 -m venv <nameofvirtualenv>

``` 
* Activate virtual envirnment 
```nashorn js

$ source nameofvirtualenv/bin/activate

```
* Make a local directory.

* Clone project in your directory.
```nashorn js
$ git clone https://github.com/paint-it/genpass.git

```
* Install setup.py
```nashorn js
$ python3 setup.py install

```
* Use command **manpass**

* You just need to install first setup.py file 

#### Command line options
```sh 
$ python3 setup.py install
 
Options:
  --help  Show this message and exit.

Commands:
  createpass  Enter required data
  savepass    Provide your password
  showpass    Printing data
```
#### Examples
* This command will ask for portal name
```sh 
$ manpass createpass
Enter portal name [None]: 
```
* Save password
```sh
$ manpass savepass
Enter portal name [None]:
Enter your password [None]:
```
* Show Password
```nashorn js
$ manpass showpass
Enter portal name [None]:
```

### How to contribute to this project?
* Please read [contribute.md](https://github.com/paint-it/genpass/blob/master/contributing.md)

### Information about libraries used in this project?
* [**Click**](https://pypi.org/project/click/) - It is a third party tool which we have used creatoing commands. We have commands like ```createpass``` and ```showpass```

* [**Diceware**](https://pypi.org/project/diceware/) - It is used to generate random passsword for user. As we are just managing these passwords in encrypted format to secure your password


