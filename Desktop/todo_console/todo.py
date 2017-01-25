import sys
import sqlite3

conn = sqlite3.connect('todolist.db')
c = conn.cursor

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS toDoList(userid TEXT, todo TEXT, items TEXT )')

	create_table()
	def view_todo ():
	con.row_factory = lambda cursor, row: row [0]
	rows = c.execute('SELECT todo FROM toDo_4').fetchall()
	print (rows)

		#d = defaultdict(dict)
		#for a, b in row:
			#d[a] = b
			#print (d)
view_todo()
