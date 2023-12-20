# 09 Team Activity: CSV Files

'''
CORE REQUIREMENTS:
1. Open the students.csv file for reading, skip the first line of text in the file because
it contains only headings, and read the other lines of the file into a dictionary. 
The program must store each student I-Number as a key and each I-Number name pair or 
each name as a value in the dictionary. 

2. Get an I-Number from the user, use the I-Number to find the corresponding student name 
in the dictionary, and print the name.

3. If a user enters an I-Number that doesn’t exist in the dictionary, your program must
print the message, "No such student" (without the quotes).
'''

import csv


def main():
    ID_INDEX = 0
    NAME_INDEX = 1

    students_dict = read_dictionary("students.csv", NAME_INDEX)

    i_number = input(f"Please enter an I-Number (xx-xxx-xxxx): ")
    i_number = i_number.replace("-", "")

    if not i_number.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(i_number) < 9:
            print("Invalid I-Number: too few digits")
        elif len(i_number) > 9:
            print("Invalid I-Number: too many digits")
        else:
            if i_number not in students_dict:
                print("No such student")
            else:
                value = students_dict[i_number]
                name = value[NAME_INDEX]

                print(name)


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}    
    with open(filename, "rt") as students_file:
        reader = csv.reader(students_file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list

    return dictionary 

if __name__ == "__main__":
    main()