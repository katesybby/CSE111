import time

def load():
    pass

def save(filename, todos):
    '''save all todo items to a file'''
    with open(filename, "w") as file:
        for item in todos:
            file.write(f'{item[0]},{item[1]},{item[2]},{item[3]}\n ')

def display():
    '''display all items to the screen'''
    pass

def add_todo(todos, description, date, location, done):
    '''add one item to the todo list'''
    todos.append([description, date, location, done])
    

def main():
    pass

if __name__ == '__main__':
    main()