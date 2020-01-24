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
from pygenpass.database import DatabaseConnection
from datetime import date
from beautifultable import BeautifulTable  # display output in table format


db_obj = DatabaseConnection()


@click.command(help="Show Version")
def version():
    click.echo("PyGenpass v0.2")


@click.command(help="Show all passwords")
def allpass():
    all_pass = db_obj.show_all_data()
    if all_pass == []:
        print("No records found")
    table = BeautifulTable()
    table.left_border_char = "|"
    table.right_border_char = "|"
    table.top_border_char = "="
    table.header_separator_char = "="
    table.column_headers = ["ID", "PORTAL_NAME", "PASSWORD", "DATE", "EMAIL", "PORTAL_URL"]
    for row in all_pass:
        table.append_row([row[0], row[1], row[2], row[3], row[4], row[5]])
        print(table)


@click.command(help="Delete password")
def delpass():
    """used to delete existing password"""
    portal_name = click.prompt("Enter portal name", default="None")
    value_check = db_obj.show_data(portal_name)
    if value_check is None:
        print("No records found")
    else:
        db_obj.delete_data(portal_name=portal_name)


@click.command(help="Update password")
def modpass():
    """Update existing password"""
    portal_name = click.prompt("Enter portal name", default="None")
    mod_check = db_obj.show_data(portal_name)
    if mod_check is None:
        print("No records found")
    else:
        mod = click.prompt("Enter new password", default="None", hide_input=True)
        db_obj.update_data(portal_name=portal_name, password=mod)


@click.command(help="Save existing passwords")
def savepass():
    """Used to take portal name and password from user"""
    portal_name = click.prompt("Enter portal name", default="None")
    pwd = click.prompt("Enter your password", default="None", hide_input=True)
    creation_date = date.today()
    email = click.prompt("Enter email id", default="None")
    portal_url = click.prompt("Enter portal url", default="None")
    db_obj.insert_data(
        portal_name=portal_name,
        password=pwd,
        creation_date=creation_date,
        email=email,
        portal_url=portal_url,
    )


@click.command(help="Create new password")
def createpass():
    """Used for taking input from user to create password"""
    portal_name = click.prompt("Enter portal name", default="None")
    password = diceware.get_passphrase()
    creation_date = date.today()
    email = click.prompt("Enter email id", default="None")
    portal_url = click.prompt("Enter portal url", default="None")
    db_obj.insert_data(
        portal_name=portal_name,
        password=password,
        creation_date=creation_date,
        email=email,
        portal_url=portal_url,
    )


@click.command(help="Show password")
def showpass():
    portal_name = click.prompt("Enter portal name", default="None")
    spass = db_obj.show_data(portal_name)
    if spass is None:
        print("No records found")
    else:
        print(spass)
