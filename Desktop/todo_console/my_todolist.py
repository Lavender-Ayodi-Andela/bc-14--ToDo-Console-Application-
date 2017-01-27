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

    """ 
    DESCRIPTION: Enter TO DO Category and its items into the database.
    """


def data_entry():
    todo = input('ENTER TO DO LIST CATEGORY:\n')
    item = input('ENTER THE ITEM YOU WANT TO INCLUDE IN IT:\n')
    c.execute('INSERT INTO toDo_5 (todo, item) VALUES (?, ?)',
              (todo, item))
    con.commit()

    item_id = c.lastrowid
    sync_firebase(item_id, todo, item)

    print ('DATA ENTERED SUCCESSFULLY\n')
    add_item_prompt = input('DO YOU WANT TO ADD ANOTHER ITEM? y/n\n ')

    while add_item_prompt == 'y' or add_item_prompt == 'Y':
        todo = input('ENTER TO DO LIST CATEGORY:\n')
        item = input('ENTER THE ITEM YOU WANT TO INCLUDE IN IT:\n')
        c.execute('INSERT INTO toDo_5 (todo, item) VALUES (?, ?)',
                  (todo, item))
        con.commit()

        item_id = c.lastrowid
        sync_firebase(item_id, todo, item)

        print ('DATA ENTERED SUCCESSFULLY\n')
        add_item_prompt = input('DO YOU WANT TO ADD ANOTHER ITEM? y/n \n')

        if add_item_prompt == 'n' or add_item_prompt == 'N':
            break

    """ 
    DESCRIPTION: View the TO-DO List Categories available in the database.
    """


def view_todo():
    c.execute(
        'SELECT todo,count (todo) FROM toDo_5 GROUP BY todo HAVING count(todo) >1')
    todo_present = c.fetchall()
    for todo_category in todo_present:
        t.add_rows([[todo_category[0]]])
        print (t.draw())

    """ 
    DESCRIPTION: View the items per TO-DO List Category available 
    in the database.
    """


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

    """ 
    DESCRIPTION: View all the items available in the database.
    """


def view_items():
    c.execute('SELECT * FROM toDo_4')
    rows = c.fetchall()
    for row in rows:
        t.add_rows([[[row[1]]]])
        print (t.draw())

    """ 
    DESCRIPTION: User Interface
    """


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
        elif x == 5:
            delete_entry()
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
