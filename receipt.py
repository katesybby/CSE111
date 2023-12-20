# 09 Prove Milestone: Text Files
'''
A local grocery store subscribes to an online service that enables its customers to order groceries online. 
After a customer completes an order, the online service sends a CSV file that contains the customer’s requests to the grocery store. 
The store needs you to write a program that reads the CSV file and prints to the terminal window a receipt 
that lists the purchased items and shows the subtotal, the sales tax amount, and the total.
'''

#PART 1 REQS:
# Download and save the products.cv and request.csv files.
# Write code that reads the rows in the products.csv file into a dictionary named products.
# Write code that prints the products dictionary.
# Write code that reads the rows from the requests.csv file.
# Write code that retrieves the product name and price from the products dictionary.
# Write code that prints the product name, quantity, and price as shown in the Sample
# Run section of this assignment.

#PART 2 REQS:
# Print the store name at the top of the receipt.
# Print the list of ordered items.
# Sum and print the number of ordered items.
# Sum and print the subtotal due.
# Compute and print the sales tax amount. Use 6% as the sales tax rate.
# Compute and print the total amount due.
# Print a thank you message.
# Get the current date and time from your computer’s operating system and print the current date and time.
# Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.



from datetime import datetime

import csv


# Indexes for products.csv
KEY_INDEX = 0
VALUE_INDEX = 1

# Indexes for request.csv
PRODUCT_NUMB_INDEX = 0
QUANTITY_INDEX = 1


def main():
    current_date_and_time = datetime.now()

    products_dict = read_products("products.csv", KEY_INDEX)
    request_dict = read_request("request.csv", PRODUCT_NUMB_INDEX)

    print(products_dict)

# Opens the request.csv file for reading.
# Skips the first line of the request.csv file because the first line contains column headings.
    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)

# Uses a loop that reads and processes each row from the request.csv file. 
# Within the body of the loop, your program must do the following for each row:
# Use the requested product number to find the corresponding item in the products_dict.
# Print the product name, requested quantity, and product price.
        for row_list in reader:
            pass
            #compare product # to key
            
    print("Inkom Emporium")
    print()
    print(request_dict)
    print()
    print(f"Number of Items: {numb_items}")     
    print(f"Subtotal: {subtotal}")
    print(f"Sales Tax: {sales_tax}")
    print(f"Total: {total}")
    print()
    print("Thank you for shopping at the Inkom Emporium.")
    print(f"{current_date_and_time:%c}")


#IDEA BANK:
    # for element in periodic_table_dict():
    #         symbol = symbol_quantity_list[SYMBOL_INDEX]
    #         quantity = symbol_quantity_list[QUANTITY_INDEX]
    #         atomic_mass = periodic_table_dict[ATOMIC_MASS_INDEX]

            # key = row_list[key_column_index]
            # dictionary[key] = row_list
            # print(f"{}")



def read_products(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products = {}    
    with open(filename, "rt") as products_file:
        reader = csv.reader(products_file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            products[key] = row_list

    return products 


def read_request(filename, key_column_index):
    request = {}    
    with open(filename, "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            request[key] = row_list

    return request 



if __name__ == "__main__":
    main()