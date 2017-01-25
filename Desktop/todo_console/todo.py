import sys
import sqlite3

conn = sqlite3.connect('todolist.db')
c = conn.cursor

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS toDoList(userid TEXT, todo TEXT, items TEXT )')

	create_table()