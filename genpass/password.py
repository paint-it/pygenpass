import click
import diceware
from datetime import datetime
from passlib.context import CryptContext


@click.group()
def main():
    pass

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

# password encryption
def encrypt_pass():
	password = diceware.get_passphrase()
	return pwd_context.encrypt(password)


@main.command(help="Enter required data")
def create_pass():
    portal_name = click.prompt('Enter portal name', default="None")
    portal_url = click.prompt('Enter portal_url',default="None")
    user_email = click.prompt('Enter mail-id',default="None")
    tag = click.prompt('Enter tags',default="None")
    notes = click.prompt('Enter notes',default="None")
    password = encrypt_pass()
    creation_date = datetime.now()
    print("\n\n Portal Name: {portal_name}\n Portal URL: {portal_url}\n User Email: {user_email}\n Tags: {tag}\n Notes: {notes}\n Password: {password}\n Creation Date: {creation_date}".format(portal_name=portal_name, portal_url=portal_url, user_email=user_email, tag=tag, notes=notes, password=password, creation_date=creation_date))
main.add_command(create_pass)

@main.command(help="printing data")
def print_data():
    pass

main.add_command(print_data)


if __name__ == '__main__':
    main()
