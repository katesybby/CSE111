import pytest
import random
from Lessons.today import *

'''
todo item:
- description
- date
- location
- done
'''

def test_load():
    pass

def test_save():
    # create todos
    todos = [
        ['call joe', "2023-01-24", "home", False],
        ["Bread", "2003-01-24", "store", False]
    ]

    # call save
    save('temp.dat', todos)

    # does the file exist?
    

    # check that the file created matches our data
    with open('temp.dat') as file:
        lines = file.readlines()    #HOW TO COMPARE LISTS
    
    assert len(lines) == len(todos)
    
    for i in range(len(lines)):
        parts = lines[i].split(',')
        assert parts[0] == todos[i][0]
        assert parts[1] == todos[i][1]
        assert parts[2] == todos[i][2]
        if todos[i][3]:
            assert parts[3] == 'True\n'
        else:
            assert parts[3] == 'False\n'



def test_display():
    pass

def test_add_todo():
    description = 'call joe'
    date = "2023-01-24"
    location = "home"
    done = False
    todos = []
    add_todo(todos, description, date, location, done)
    assert len(todos) == 1
    assert todos == [['call joe', "2023-01-24", "home", False]]

    add_todo(todos, "Bread", "2003-01-24", "store", False)
    assert len(todos) == 2
    assert todos == [['call joe', "2023-01-24", "home", False],
                    ["Bread", "2003-01-24", "store", False]]

pytest.main(["-v", "- - tb=line", " -rN", __file__])