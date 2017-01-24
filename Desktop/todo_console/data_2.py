import sys
import sqlite3

con = sqlite3.connect('database_2.db')
c = con.cursor()

def create_table():
	c.execute ('CREATE TABLE IF NOT EXISTS toDo_2(todo TEXT, item TEXT)')

create_table()