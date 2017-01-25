import sys
import sqlite3
from collections import defaultdict


con = sqlite3.connect('database_2.db')
c = con.cursor()

def create_table():
	c.execute ('CREATE TABLE IF NOT EXISTS toDo_4(todo TEXT, item TEXT)')

create_table()


#def hjt():
	#b_list = c.fetchall()


#user = input('Enter your first name: ')
todo = input('Enter the activity you want to do:')
item = input('Enter the item you want to do:')
c.execute ('INSERT INTO toDo_4 (todo, item) VALUES (?, ?)', (todo, item))
con.commit()
print ('Data entered successfully')
que = input ('Do you want add another item? y/n')
print ('Data entered successfully')
while que == 'y':
	todo = input('Enter the activity you want to do:')
	item = input('Enter the item you want to do:')
	c.execute ('INSERT INTO toDo_4 (todo, item) VALUES (?, ?)', (todo, item))
	con.commit()
	print ('Data entered successfully')
	que = input ('Do you want add another item? y/n')
	
	if que == 'n':
		break

def view_todo ():
	c.execute('SELECT * FROM toDo_4')

	rows = c.fetchall()

	for row in rows:
		print (row)

		d = defaultdict(dict)
		for a, b in row:
			d[a] = b
			print (d)
view_todo()



