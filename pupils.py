# 11 Team Activity: Functional Programming
'''
REQUIREMENTS
1. A function named print_list that takes a list as a parameter and prints the list
 with each element of the list on a separate line.
2. A function named main that calls read_compound_list and print_list.
3. Statements in the main function that sort the students_list by birthdate from oldest to youngest.
'''

import csv

GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def main():
    try: 
    # Call the read_compound_list function to read the pupils.csv file into a list named students_list.
        students_list = read_compound_list("pupils.csv")

    # Write a lambda function that will extract the birthdate from a student.
        birthdate = lambda student: student[BIRTHDATE_INDEX]
        
    # Write a call to the Python built-in sorted function that will sort the students_list by birthdate from oldest to youngest.
        sorted_list = sorted(students_list, key=birthdate)

    # Print the students_list by calling the print_list function.
        print_list(sorted_list)

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(list):
    """takes a list as a parameter and prints each element of the list on a separate line. 
    In other words, this print_list function should include a for loop that prints each element on a separate line."""
    
    list = {}

    for element in list:
        print(element)
    print()


if __name__ == "__main__":
    main()