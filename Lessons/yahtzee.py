import time

# def check1(roll):
#      if not isinstance(roll, list):
#         return False

#     #are there 5 values in the list
#     if len(roll) != 5:
#         return False

#     for thing in roll:
#         if not isinstance(thing, int):
#             return False
#     return True 


def three(roll):
    if not isinstance(roll, list):
        return False

    #are there 5 values in the list
    if len(roll) != 5:
        return False

    for thing in roll:
        if not isinstance(thing, int):
            return False

    #is there 3 of a kind
    for number in range (1, 7):
        if roll.count(number) == 3:
            return True

    return False

def four(roll):
    if not isinstance(roll, list):
        return False

    #are there 5 values in the list
    if len(roll) != 5:
        return False

    for thing in roll:
        if not isinstance(thing, int):
            return False
            
    #is there 4 of a kind
    for number in range (1, 7):
        if roll.count(number) == 4:
            return True

def full():
    # if not check(roll):
    #     return False

    for number1 in range (1, 7):
        for number2 in range (1, 7):
            if roll.count(number1) == 2 and roll.count(number2) == 3:
                return True

def ss():
    pass

def ls():
    pass
