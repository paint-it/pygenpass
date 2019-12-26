import sqlite3


class DatabaseConnection():
	def __init__(self):
		# Connecting to sqlite3 database
		self.con = sqlite3.connect('generated_password.db')
		self.cursor_obj = self.con.cursor()
	def create_table(self):
		# Creating table
		self.cursor_obj.execute("CREATE TABLE passwords(id integer PRIMARY KEY, portal_name text, portal_url real, user_email text, tag text, creation_date text, last_modified text, notes text, level text, importance text)")
		self.con.commit()
	def insert_data(self):
		# Insert data in table
		self.cursor_obj.execute('INSERT INTO passwords VALUES(1, "paytm", "www.paytm.com", "mlhanae@gmail.com", "money", "25 dec", "24 dec", "using for food wallet", "strong", "starred")')
		self.con.commit()
	def show_data(self):
		# Show databse entries
		self.cursor_obj.execute("SELECT * FROM passwords")
		rows = self.cursor_obj.fetchall()
		for row in rows:
			print(row)
		self.con.commit()

	def update_data(self):
		#update data
		self.cursor_obj.execute('UPDATE passwords SET portal_name = "ola",portal_url = "www.ola.com" where id = 1')
		self.con.commit()

db = DatabaseConnection()
#db.create_table()
#db.insert_data()
db.show_data()
db.update_data()
db.show_data()
