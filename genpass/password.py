import click
import diceware
from datetime import datetime

@click.group()
def main():
    pass


@main.command(help="Enter required data")
def create_pass():
    portal_name = click.prompt('Enter portal name', default="None")
    portal_url = click.prompt('Enter portal_url',default="None")
    user_email = click.prompt('Enter mail-id',default="None")
    tag = click.prompt('Enter tags',default="None")
    notes = click.prompt('Enter notes',default="None")
    password = diceware.get_passphrase()
    creation_date = datetime.now()
    print(f"\n\nPortal Name: {portal_name}\n Portal URL: {portal_url}\n User Email: {user_email}\n Tags: {tag}\n Notes: {notes}\n Password: {password}\n Creation Date: {creation_date}")

main.add_command(create_pass)

@main.command(help="printing data")
def print_data():
    pass

main.add_command(print_data)


if __name__ == '__main__':
    main()
