import sys
import sqlite3

con = sqlite3.connect('database.db')
c = con.cursor()

def create_table():
	c.execute ('CREATE TABLE IF NOT EXISTS toDo(userid TEXT, todo TEXT)')

create_table()

