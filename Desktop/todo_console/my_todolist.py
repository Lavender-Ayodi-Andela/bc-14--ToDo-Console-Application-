# Forget Me Not Command Line Application
# Author : Lavender Ayodi for Andela Kenya
# Date: 26th January 2017
# Version 1.0

from colorama import Fore, Back, Style
from colorama import init
import pyrebase
import sqlite3
import sys
from texttable import Texttable
init()


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
    DESCRIPTION: View the items per TO-DO List Category
    available in the database.
    """


def view_item_per_todo():
    print('ENTER THE TO-DO LIST CATEGORY TITLE: \n')
    print('For example: Books To Read \n')
    key_word = input('Enter keyword: \n')
    c.execute('SELECT * FROM toDo_5 WHERE item LIKE ?',
              ('%' + key_word + '%',))
    todo_word = c.fetchall()
    for item_word in todo_word:
        t.add_rows([[item_word[1]]])
        print (t.draw())

    """
    DESCRIPTION: View all the items available in the database.
    """


def view_items():
    c.execute('SELECT * FROM toDo_5')
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
        Message_1 = Fore.YELLOW + 'FORGET ME NOT'
        print('{:^80}'.format(Message_1))
        print(Style.RESET_ALL)
        print('*' * 80)
        print()
        print('_' * 80)
        Message_2 = Fore.YELLOW + 'Your Favourite To-Do List App'
        print('{:^80}'.format(Message_2))
        print(Style.RESET_ALL)
        print('_' * 80)
        print('_' * 80)
        a = '-'
        Message_3 = Fore. CYAN + "ENTER 1 \n"
        print('{:^80}'.format(Message_3))
        Message_8 = "TO ADD TO-DO CATEGORIES AND ITEMS \n"
        print('{:^80}'.format(Message_8))
        Message_4 = "ENTER 2\n"
        print('{:^80}'.format(Message_4))
        Message_9 = "VIEW YOUR TO DO COLLECTIONS \n"
        print('{:^80}'.format(Message_9))
        Message_5 = "ENTER 3\n"
        print('{:^80}'.format(Message_5))
        Message_10 = "VIEW ALL THE ITEMS YOU WANT TO DO \n"
        print('{:^80}'.format(Message_10))
        Message_6 = "ENTER 4\n"
        print('{:^80}'.format(Message_6))
        Message_11 = "VIEW THE ITEMS TO BE DONE FROM EACH TO DO CATEGORY \n"
        print('{:^80}'.format(Message_11))
        Message_7 = "ENTER 0\n"
        print('{:^80}'.format(Message_7))
        Message_12 = "QUIT\n"
        print('{:^80}'.format(Message_12))
        print('_' * 80)
        print(Style.RESET_ALL)
        x = input("WELCOME! PLEASE CHOOSE AN OPTION AS SPECIFIED ABOVE: ")
        x = int(x)
        print(Style.RESET_ALL)
        print('_' * 80)
        print()
        if x == 0:
            print (Fore.YELLOW + 'GOOD-BYE! DO NOT FORGET TO COME BACK!')
            # exit
            break
            pass
        elif x == 1:
            data_entry()
            pass
        elif x == 2:
            print(Fore.YELLOW + 'THE TO-DO LISTS AVAILABLE INCLUDE:')
            print(Style.RESET_ALL)
            print('-' * 34)
            print()
            view_todo()
            pass
        elif x == 3:
            print(Fore.YELLOW + 'THE ITEMS IN THE TO-DO LISTS ARE:')
            print(Style.RESET_ALL)
            print('-' * 48)
            print()
            view_items()
            pass
        elif x == 4:
            view_item_per_todo()
        else:
            print(Fore.RED + "INVALID INPUT")
            print(Style.RESET_ALL)

if __name__ == "__main__":
    console()
