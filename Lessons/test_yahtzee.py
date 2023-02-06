'''
SAVE BEFORE TESTING!!!
can't be interactive
'''

import pytest
# from yahtzee import three
from yahtzee import *       #imports everything


def test_three():
    assert three([1, 2, 3, 4, 5])  == False    #assert == if false, program crash; only seen by developer; need as many as possible
    assert three([1, 2, 3, 1, 5])  == False
    assert three([1, 1, 3, 1, 5])  == True
    assert three([1, 1, 3, 1, 1])  == False
    assert three([1, 1, 1, 1, 1])  == False
    assert three([5, 2, 3, 5, 5])  == True
    assert three([])  == False
    assert three([1, 2, 3, 4, 5, 3, 2, 1])  == False

    assert three("hi")  == False
    assert three(1)  == False
    assert three(2.457)  == False
    assert three(True)  == False

    assert three([1, 2, 3, '4', 5])  == False

def test_four():
    assert four([1, 2, 3, 4, 5])  == False    
    assert four([1, 2, 3, 1, 5])  == False
    assert four([1, 1, 3, 1, 1])  == True
    assert four([1, 1, 3, 1, 1])  == False
    assert four([1, 1, 1, 1, 1])  == False
    assert four([5, 2, 5, 5, 5])  == True
    assert four([])  == False
    assert four([1, 2, 3, 4, 5, 3, 2, 1])  == False

    assert four("hi")  == False
    assert four(1)  == False
    assert four(2.457)  == False
    assert four(True)  == False

    assert four([1, 2, 3, '4', 5])  == False

def full():
    assert full([1, 2, 3, 4, 5])  == False    
    assert full([1, 2, 3, 1, 5])  == False
    assert full([1, 1, 3, 1, 5])  == False
    assert full([1, 1, 3, 1, 1])  == False
    assert full([1, 1, 1, 1, 1])  == False
    assert full([5, 2, 5, 5, 5])  == True
    assert full([])  == False
    assert full([1, 2, 3, 4, 5, 3, 2, 1])  == False

    assert full("hi")  == False
    assert full(1)  == False
    assert full(2.457)  == False
    assert full(True)  == False

    assert full([1, 2, 3, '4', 5])  == False


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])