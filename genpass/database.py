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

import sqlite3  # library for database


class DatabaseConnection:
    """ Class of database entries for user's information."""

    def __init__(self):
        """Used to create database and then to connect with generated databse file
        Checked for table is created? if not then created as per required values """
        self.con = sqlite3.connect("generated_password.db")
        self.cursor_obj = self.con.cursor()
        self.cursor_obj.execute(
            """CREATE TABLE IF NOT EXISTS passwords
    		  (id integer PRIMARY KEY,portal_name text NOT NULL UNIQUE, password varchar,
    		  creation_date varchar, email varchar, portal_url varchar)
    		"""
        )
        self.con.commit()

    def insert_data(self, portal_name, password, creation_date, email, portal_url):
        """Adding values into database"""
        self.password = password
        self.creation_date = creation_date
        self.email = email
        self.portal_name = portal_name
        self.portal_url = portal_url
        self.cursor_obj.execute(
            """INSERT INTO passwords
            (portal_name, password, creation_date, email, portal_url)
            VALUES (?, ?, ?, ?, ?)""",
            (self.portal_name, self.password, self.creation_date, self.email, self.portal_url,),
        )
        self.con.commit()

    def delete_data(self, portal_name):
        """Deleting values from database"""
        self.portal_name = portal_name
        self.cursor_obj.execute(
            """DELETE from passwords where portal_name = ?""", (self.portal_name,)
        )
        self.con.commit()

    def update_data(self, portal_name, password):
        """Updating values in database"""
        self.portal_name = portal_name
        self.password = password
        self.cursor_obj.execute(
            """UPDATE passwords SET password =? WHERE portal_name =?""",
            (self.password, self.portal_name),
        )
        self.con.commit()

    def show_data(self, portal_name):
        """All inserted data will showed"""
        self.portal_name = portal_name
        self.cursor_obj.execute(
            """SELECT password FROM passwords WHERE portal_name=?""", (self.portal_name,),
        )
        rows = self.cursor_obj.fetchall()

        for row in rows:
            return row[0]

        self.con.commit()

    def show_all_data(self):
        """Showing all data saved in database"""
        self.cursor_obj.execute("""SELECT * FROM passwords""")
        rows = self.cursor_obj.fetchall()
        return rows
        self.con.commit()
