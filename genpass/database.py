import sqlite3


class DatabaseConnection():
	''' This is class for database entries of users 
	    as 1.id
	       2.portal_name
	       3.portal_url
	       4.user_email
	       5.tag
	       6.creation_date
	       7.last_modified text
	       8.notes
	       9.level
	       9.importance
	    from the file of password.py which will first take input from user and then pass it to 
	    diceware tool.It will provide password '''	




	def __init__(self):
		
		'''The constructor for database connections to the password file 
		   and for cursor object which used to retrive data from SQL queries '''	
		
		self.con = sqlite3.connect('generated_password.db')
		self.cursor_obj = self.con.cursor()
	
	
	def create_table(self):
		'''This method will create table having columns as given below and will pass to execute function ''' 
		
		self.cursor_obj.execute("CREATE TABLE passwords(id integer PRIMARY KEY, portal_name text, portal_url real, user_email text, tag text, creation_date text, last_modified text, notes text, level text, importance text)")
		self.con.commit()
	
	

	def insert_data(self):
		'''This method will insert data in their respective positional argument'''
		
		self.cursor_obj.execute('INSERT INTO passwords VALUES(1, "paytm", "www.paytm.com", "mlhanae@gmail.com", "money", "25 dec", "24 dec", "using for food wallet", "strong", "starred")')
		self.con.commit()
	
	

	def show_data(self):
		'''This method firstly will show the table named password
		   which uses fetchall()for getting all entries
		    and to get that we have run the loop to for rows'''
		 
		self.cursor_obj.execute("SELECT * FROM passwords")
		rows = self.cursor_obj.fetchall()
		for row in rows:
			print(row)
		self.con.commit()

	
	

	def update_data(self):
		'''This method will update the changes if their is wrong entry by considering unique id '''
		self.cursor_obj.execute('UPDATE passwords SET portal_name = "ola",portal_url = "www.ola.com" where id = 1')
		self.con.commit()

db = DatabaseConnection()
#db.create_table()
#db.insert_data()
db.show_data()
db.update_data()
db.show_data()
