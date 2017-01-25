import sys
import sqlite3
import itertools


con = sqlite3.connect('database_2.db')
c = con.cursor()

def create_table():
	c.execute ('CREATE TABLE IF NOT EXISTS toDo_4(todo TEXT, item TEXT)')

create_table()


#def hjt():
	#b_list = c.fetchall()
class ToDoList():

def data_entry(self):
    #user = input('Enter your first name: ')
    todo = input('Enter the activity you want to do:')
    item = input('Enter the item you want to do:')
    c.execute ('INSERT INTO toDo_4 (todo, item) VALUES (?, ?)', (todo, item))
    con.commit()
    print ('Data entered successfully')
    que = input ('Do you want add another item? y/n ')
    print ('Data entered successfully')
    while que == 'y':
	    todo = input('Enter the activity you want to do:')
	    item = input('Enter the item you want to do:')
	    c.execute ('INSERT INTO toDo_4 (todo, item) VALUES (?, ?)', (todo, item))
	    con.commit()
	    print ('Data entered successfully')
	    que = input ('Do you want add another item? y/n ')
	    
	    if que == 'n':
		    break



def view_todo (self):
	con.row_factory = lambda cursor, row: row [0]
	rows = c.execute('SELECT todo FROM toDo_4').fetchall()
	#return (rows)
	

	for i in rows:
		a = []
		if type(i) == (tuple):
			for j in i:
				a.append(j)

				print (a)


def solve(self):
	c = con.cursor()
	con.row_factory = lambda cursor, row: row [0]
	c.execute('SELECT todo,count (todo) from toDo_4 group by todo having count (todo) >1')
	k = c.fetchall()

	print (k)


def unique(self):
	key_word = input('Enter keyword: ')
	c = con.cursor()
	word = c.execute('SELECT item FROM toDo_4 WHERE item = ?', (key_word)).fetchall()
	

	print (word)


def view_items(self):
	c.execute('SELECT * FROM toDo_4')
	rows = c.fetchall()

	for row in rows:
		print (row [1])








