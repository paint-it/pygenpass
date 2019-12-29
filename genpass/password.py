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
import click # Used for command line interface.
import diceware # Used for creating password.
# TODO:from datetime import datetime

from passlib.context import CryptContext
from database import DatabaseConnection

db_obj = DatabaseConnection()

pwd_context = CryptContext(
schemes=["pbkdf2_sha256"],
default="pbkdf2_sha256",
pbkdf2_sha256__default_rounds=30000
)


def encrypt_pass():
    """Used for encrypting password"""
    password = diceware.get_passphrase()
    return pwd_context.encrypt(password)


@click.command(help="Enter required data")
def create_pass():
    """Used for taking input from user to create password"""
    portal_name = click.prompt('Enter portal name', default="None")

    # TODO: portal_url = click.prompt('Enter portal_url',default="None")
    # TODO: user_email = click.prompt('Enter mail-id',default="None")
    # TODO: tag = click.prompt('Enter tags',default="None")
    # TODO: notes = click.prompt('Enter notes',default="None")
    # TODO: creation_date = datetime.now()
    # TODO: portal_url=portal_url, user_email=user_email)

    password = encrypt_pass()
    db_obj.create_table()
    db_obj.insert_data(portal_name=portal_name, password=password)

@click.command(help="printing data")
def print_data(): # Print data here
        db_obj.show_data()

