# Forget Me Not Command Line Application
# Author : Lavender Ayodi for Andela Kenya
# Date: 26th January 2017
# Version 1.0

import pyrebase
import sqlite3
import sys
from texttable import Texttable


t = Texttable()

con = sqlite3.connect('database_2.db')
c = con.cursor()


def create_table():

    c.execute('CREATE TABLE IF NOT EXISTS toDo_5(todo TEXT, item TEXT)')

create_table()


def sync_firebase(item_id, todo, item):
    # TO DO: Hide API KEY IN .env file
    config = {
        "apiKey": "AIzaSyAYepra5SLJDtm_aVrSiLNkEofnwdpRixE",
        "authDomain": "to-do-list-fdebf.firebaseapp.com",
        "databaseURL": "https://to-do-list-fdebf.firebaseio.com",
        "storageBucket": "to-do-list-fdebf.appspot.com"
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    data = {"todo": todo, "item": item}
    db.child("todos").child(item_id).set(data)


def data_entry():
    print('For example : Books To Read \n')
    todo = input('Enter the TITLE of the TO-DO List:\n')
    print('Insert in this format : Books To Read: Bible \n')
    item = input('Enter the Item you want to include in the List:\n')

    c.execute('INSERT INTO toDo_4 (todo, item) VALUES (?, ?)', (todo, item))
    con.commit()
    item_id = c.lastrowid
    sync_firebase(item_id, todo, item)
    print ('Data entered successfully')
    add_item_prompt = input(('Do you want add another item? y/n \n ').lower())

    while add_item_prompt != 'n' or add_item_prompt != 'no':
        print('\n')
        todo = input('Enter the TITLE of the TO-DO List:\n')
        item = input('Enter the Item you want to include in the List:\n')

        c.execute('INSERT INTO toDo_4 (todo, item) VALUES (?, ?)',
                  (todo, item))
        con.commit()
        item_id = c.lastrowid
        sync_firebase(item_id, todo, item)
        print ('Data entered successfully')
        add_item_prompt = input('Do you want add another item? y/n ')
        if add_item_prompt == 'n':
            break


def view_todo():
    c.execute(
        'SELECT todo,count (todo) FROM toDo_4 GROUP BY todo HAVING count(todo) >1')
    todo_present = c.fetchall()
    for todo_category in todo_present:
        t.add_rows([[todo_category[0]]])
        print (t.draw())


def view_item_per_todo():
    print('Enter the TITLE of TO-DO List to delete items you have done.\n')
    print('For example: Books To Read \n')
    key_word = input('Enter keyword: \n')
    c.execute('SELECT * FROM toDo_4 WHERE item LIKE ?',
              ('%' + key_word + '%',))
    todo_word = c.fetchall()
    for item_word in todo_word:
        t.add_rows([[item_word[1]]])
        print (t.draw())


def view_items():
    c.execute('SELECT * FROM toDo_4')
    rows = c.fetchall()
    for row in rows:
        t.add_rows([[[row[1]]]])
        print (t.draw())


def delete_entry():
    print('Enter the TITLE of TO-DO List to delete items you have done.')
    print()
    print('For example: Books To Read')
    print()
    key_word = input('Enter keyword: ')
    print()
    c.execute('SELECT * FROM toDo_4 WHERE item LIKE ?',
              ('%' + key_word + '%',))
    word = c.fetchall()
    for s in word:
        t.add_rows([[s[1]]])
        print (t.draw())

    print ('Enter The Item That you have already done:')
    delete_word = input('Enter the Name of the Item: ')
    print()
    mydata = c.execute("DELETE FROM toDo_4 WHERE Item = ?",
                       (delete_word,))
    print ('DELETED SUCCESSFULLY')


def console():
    while True:
        print('\n')
        print('*' * 80)
        print("Forget Me Not")
        print('*' * 80)
        print()
        print('_' * 80)
        print("Your Favourite To-Do List App")
        print('_' * 80)
        print('_' * 80)
        a = '-'
        print("Enter 1")
        print("-".center(20, a))
        print("To Add To Do Categories and Items \n")
        print("Enter 2")
        print("-".center(20, a))
        print("View Your To Do Collections \n")
        print("Enter 3")
        print("-".center(20, a))
        print("View All The Items You Want To Do \n")
        print("Enter 4")
        print("-".center(20, a))
        print("View The Items to be Done From each To Do Category \n")
        print("Enter 0")
        print("-".center(20, a))
        print("Quit")
        print('_' * 80)
        print()
        x = input("Welcome! Please choose an option:")
        x = int(x)
        print('_' * 80)
        print()
        if x == 0:
            print ('Goodbye! Do Not Forget To Come Back!')
            # exit
            break
            pass
        elif x == 1:
            data_entry()
            pass
        elif x == 2:
            print('The TO-DO Lists available include:')
            print('-' * 34)
            print()
            view_todo()
            pass
        elif x == 3:
            print('The Items in the TO-DO Lists available include:')
            print('-' * 48)
            print()
            view_items()
            pass
        elif x == 4:
            view_item_per_todo()
        else:
            print("Invalid input")

if __name__ == "__main__":
    console()

    # check if record already exists
    #c.execute("SELECT * FROM toDo_4 WHERE item = ?", (item,))
    #dat = c.fetchall()
    # for d in dat:
    # if not d:
    #c.execute ('INSERT INTO toDo_4 (todo, item) VALUES (?, ?)', (todo, item))
    # con.commit()
    #item_id = c.lastrowid
    #sync_firebase(item_id, todo, item)
    #print ('Data entered successfully')
    #que = input ('Do you want add another item? y/n ')
    # else:
    #print ('EXISTS')

    # check at unique
    # for s in word:
    # if s in word:
    #t.add_rows ([[s [1]]])
    #print (t.draw())
    # else:
    #msg_ = 'Entry Does Not Exist'
    #t.add_rows ([[msg_]])
    #print (t.draw())
