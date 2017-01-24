import sys

user = 0
dict_todo = {}
if user == 0:
	user = input('Enter your first name: ')
	print ('Welcome:' + user + '.' + 'Your User ID is: ' + user + '@todo')

def add_list():
	maxLengthDict = 10
	todo = input('Enter the activity you want to do:')
	dict_todo [todo] = []
	print ('The activities you have to do are: ')
	print (dict_todo)

	if todo in dict_todo:
		add_item = input('Enter the item you want to do:')
		dict_todo[todo].append(add_item)
		print (dict_todo)

add_list()

def view_list():
	list_todo = list()
	for i in dict_todo.keys():
		list_todo.append(i)
		print (list_todo)

	list_items = list()
	view_item = input ('You want to see items from which to do list: ')
	for  i in dict_todo.keys():
		if view_item == i:
			val = dict_todo.get(i,[])
			print (val)

view_list()

	


