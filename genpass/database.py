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

import sqlite3 #library for database

class DatabaseConnection(object):
	""" Class of database entries for users information."""

	def __init__(self):
		"""Used to create database and then to connect with generated databse file"""

		self.con = sqlite3.connect('generated_password.db')
		self.cursor_obj = self.con.cursor()

	def create_table(self):
		"""Checked for table is created? if not then created as per input """
		
		self.cursor_obj.execute(
			"""
			CREATE TABLE IF NOT EXISTS passwords(id integer PRIMARY KEY, portal_name text, password varchar )
			"""
		)
		self.con.commit()
	
	def insert_data(self, portal_name, password):
		"""Adding values into database"""
		self.portal_name = portal_name
		self.password = password

	# TODO: addition of values Url,Email,Tag,Creation date,Notes,Level(strong, low,medium)
		#  importance(Stared/Unstarred),Last modified.

		self.cursor_obj.execute(
			"""
			INSERT INTO passwords(portal_name, password) VALUES (?, ?)
			""",
			(self.portal_name, self.password),
		)
		self.con.commit()
	
	def show_data(self):
		"""All inserted data will showed"""
		 
		self.cursor_obj.execute("SELECT * FROM passwords")
		rows = self.cursor_obj.fetchall()
		for row in rows:
			print(row)
		self.con.commit()

	# TODO: def update_data(self):
