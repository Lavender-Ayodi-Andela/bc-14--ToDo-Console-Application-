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
	print('For example : Books To Read')
	print()
	todo = input('Enter the TITLE of the TO-DO List:')
	print()
	print('Insert in this format : Books To Read: Bible')
	print()
	item = input('Enter the Item you want to include in the List:')
	print()
	c.execute ('INSERT INTO toDo_4 (todo, item) VALUES (?, ?)', (todo, item))
	con.commit()
	print ('Data entered successfully')
	que = input ('Do you want add another item? y/n ')
	print ('Data entered successfully')
	while que == 'y':
		print()
		todo = input('Enter the TITLE of the TO-DO List:')
		print()
		item = input('Enter the Item you want to include in the List:')
		print()
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
	#c = con.cursor()
	#con.row_factory = lambda cursor, row: row [0]
	c.execute('SELECT todo,count (todo) from toDo_4 group by todo having count (todo) >1')
	k = c.fetchall()
	for l in k:
		print (l [0])

def unique():
	print('Here enter the TITLE of TO-DO List in order to retrieve items recorded under it.')
	print()
	print('For example: Books To Read')
	print()
	key_word = input('Enter keyword: ')
	print()
	#c = con.cursor()
	c.execute('SELECT * FROM toDo_4 WHERE item LIKE ?' , ('%'+key_word+'%',))
	word = c.fetchall()
	for s in word:
		print (s [1])

def view_items():
	c.execute('SELECT * FROM toDo_4')
	rows = c.fetchall()
	for row in rows:
		print (row [1])
def console():
	while True:
		print()
		print('***************************************************************')
		print("                        Forget Me Not                          ")
		print('***************************************************************')
		print()
		print('_______________________________________________________________')
		print()
		print("                 Your Favourite To-Do List App                 ")
		print('_______________________________________________________________')
		print('_______________________________________________________________')
		print()
		print()
		print("                           Enter 1                             ")
		print("                        --------------                          ")
		print("                To Add To Do Categories and Items                  ")
		print()
		print("                           Enter 2                            ")
		print("                        --------------                          ")
		print("                   View Your To Do Collections                    ")
		print()
		print("                           Enter 3                            ")
		print("                        --------------                          ")
		print("                View All The Items You Want To Do                ")
		print()
		print("                           Enter 4                            ")
		print("                        --------------                          ")
		print("       View The Items to be Done From each To Do Category      ")
		print()
		print("                           Enter 0                            ")
		print("                        --------------                          ")
		print("                            Quit                                ")
		print('_______________________________________________________________')
		print()
		x = input("               Welcome! Please choose an option:    ")
		x = int(x)
		print('_______________________________________________________________')
		print()
		if x == 0:
			#exit
			break
			pass
		elif x == 1:
			data_entry()
			pass
		elif x == 2:
			print('The TO-DO Lists available include:')
			print('----------------------------------')
			print()
			view_todo()
			pass
		elif x == 3:
			print('The Items in the TO-DO Lists available include:')
			print('-----------------------------------------------')
			print()
			view_items()
			pass
		elif x == 4:
			unique()
		else:
			print("Invalid input")

if __name__ == "__main__":
	console()