# Genpass

### How to run project?
* You just need to run __init__.py file 

#### Command line options
```sh 
$ python3 __init__.py

Usage: __init__.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  createpass  Enter required data
  showpass    printing data

```
#### Examples
* This command will ask for portal name
```sh 
$ python3 __init__.py createpass
Enter portal name [None]: 
```
* Show saved passwords
```sh
$ python3 __init__.py showpass
```

### How to contribute to this project?
* Please read [contribute.md](https://github.com/paint-it/genpass/blob/master/contributing.md)

### Information about libraries used in this project?
* [**Click**](https://pypi.org/project/click/) - It is a third party tool which we have used creatoing commands. We have commands like ```createpass``` and ```showpass```

* [**Diceware**](https://pypi.org/project/diceware/) - It is used to generate random passsword for user. As we are just managing these passwords in encrypted format to secure your password


