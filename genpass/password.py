"""
Copyright (c) 2019 paint-it

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import click  # Used for command line interface
import diceware  # Used for creating password
from genpass.database import DatabaseConnection

db_obj = DatabaseConnection()


@click.command(help="Show Version")
def version():
    click.echo("Genpass v0.1")


@click.command(help="Save existing passwords")
def savepass():
    """Used to take portal name and password from user"""
    portal_name = click.prompt('Enter portal name', default="None")
    pwd = click.prompt('Enter your password', default="None", hide_input=True)
    db_obj.create_table()
    db_obj.insert_data(portal_name=portal_name, password=pwd)


@click.command(help="Create new password")
def createpass():
    """Used for taking input from user to create password"""
    portal_name = click.prompt('Enter portal name', default="None")
    password = diceware.get_passphrase()
    db_obj.create_table()
    db_obj.insert_data(portal_name=portal_name, password=password)


@click.command(help="Show password")
def showpass():
    portal_name = click.prompt('Enter portal name', default="None")
    spass = db_obj.show_data(portal_name)
    print(spass)
