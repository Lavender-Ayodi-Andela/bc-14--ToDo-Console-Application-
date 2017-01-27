# Forget Me Not
*Forget Me Not* is a To Do List Command Line application written in the Python language.

### Features
* Alows the user to add a list of topics for each To Do category.
* Enables the user to add a list of items under each category.
* Items in the List are stored in an online firebase storage.
* Data inserted by the user can be synced in a realime basis.
* Easy to user interface to interact with.

### Dependencies | Requirements
* [Python 3.6.0] (https://www.python.org/downloads/release/python-360/) : Python Interpreter

* [requests 2.10.0] (http://docs.python-requests.org/en/master/) : Enables connection between Quizzler and Firebase
           ```pip install requests==1.1.0```

* [tqdm 4.5.0] (https://pypi.python.org/pypi/tqdm) : Enables implementation of progress bars
           ```pip install tqdm```

* [python-firebase 1.2] (https://pypi.python.org/pypi/python-firebase/1.2) : Enables easy connection between Firebase and Python
           ```pip install python-firebase```

* [Colorama==0.3.7 ]  (https://pypi.python.org/pypi/colorama) : Colour and font enhancing for python applications. ```pip install colorama```

* [pyfiglet==0.7.5] (https://pypi.python.org/pypi/pyfiglet): Takes ASCII text and renders it in ASCII art fonts.
```pip install https://pypi.python.org/packages/source/p/pyfiglet/pyfiglet-0.7.5.tar.gz```

* [termcolor==1.1.0] (https://pypi.python.org/pypi/termcolor): ANSII Color formatting for output in terminal. 
```pip install termcolor```

       
#### To install all requirements, download the [requirements.txt] (https://github.com/emabishi/bc-7-Quiz-Application/blob/master/requirements.txt) file then type this in your terminal application:
             pip install -r /path/to/requirements.txt

* To get you started, after installation, use the commands, listonline and download quiz <quiz name> or copy the quizzes in [this] (https://github.com/emabishi/bc-7-Quiz-Application/tree/master/QuizApp/quizzes) project's github repository and use the importquiz <quiz source path> command to import them into the Quizzler library. 


### Commands

|Command| Description|
|-----|---------------------------------------------------------|
|help | Displays all available commands and their descriptions |
| help (command) | Describes the command |
| listquizzes | Displays available local quizzes |
| takequiz (quiz name) | Launches the local quiz quiz name |
| listonline | Display available online quizzes |
| download (quiz) | Add a quiz to the local collection from online source |
| upload (quiz source path | Add quiz to online collection |
| importquiz (quiz source path) | Add quiz to local collection from external source |

### Copyright and Licensing
MIT license. For detailed licence information, see [license] (https://github.com/emabishi/bc-7-Quiz-Application/blob/master/LICENSE)

### Contact Information
Find the author at [@emabishi] (https://github.com/emabishi) on github.


