import sys
import sqlite3
import terminaltables

con = sqlite3.connect('database_2.db')
c = con.cursor()

def create_table():
	c.execute ('CREATE TABLE IF NOT EXISTS toDo_4(todo TEXT, item TEXT)')

create_table()


#def hjt():

		
def data_entry():
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

def solve ():
	con.row_factory = lambda cursor, row: row [0]
	rows = c.execute('SELECT todo FROM toDo_4').fetchall()
	for i in rows:
		a = []
		if type(i) == (tuple):
			for j in i:
				a.append(j)
				print (a)

def view_todo():
	c = con.cursor()
	con.row_factory = lambda cursor, row: row [0]
	c.execute('SELECT todo,count (todo) from toDo_4 group by todo having count (todo) >1')
	k = c.fetchall()
	print (k)

def unique():
	key_word = input('Enter keyword: ')
	c = con.cursor()
	word = c.execute('SELECT item FROM toDo_4 WHERE item = ?', (key_word)).fetchall()
	print (word [1])

def view_items():
	c.execute('SELECT * FROM toDo_4')
	rows = c.fetchall()
	for row in rows:
		print (row [1])
def console():
	while True:
		print()
		print("Forget Me Not")
		print()
		print("Your Favourite To-Do List")
		print("1. Add To Do Categories and Items")
		print("2. View Your To Do Collections")
		print("3. View All The Items You Want To Do")
		print("4. View The Items to be Done From each To Do Category")
		print("0. Quit")
		x = input("Welcome! Please choose an option: ")
		x = int(x)
		if x == 0:
			#exit
			break
			pass
		elif x == 1:
			data_entry()
			pass
		elif x == 2:
			view_todo()
			pass
		elif x == 3:
			view_items()
			pass
		elif x == 4:
			unique()
		else:
			print("Invalid input")

if __name__ == "__main__":
	console()