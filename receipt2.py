# 09 Prove Milestone: Text Files
'''
A local grocery store subscribes to an online service that enables its customers to order groceries online. 
After a customer completes an order, the online service sends a CSV file that contains the customer’s requests to the grocery store. 
The store needs you to write a program that reads the CSV file and prints to the terminal window a receipt 
that lists the purchased items and shows the subtotal, the sales tax amount, and the total.
'''

from datetime import datetime
import csv

# Indexes for products.csv
PRODUCTS_NUMB_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2

# Indexes for request.csv
ITEM_NUMB_INDEX = 0
QUANTITY_INDEX = 1


def main():
    current_date_and_time = datetime.now()
        
    products_file = "products.csv"
    read_products(products_file)

    print("Inkom Emporium")
    print()

    request_file = "request.csv"
    list_request(request_file, products_file)

    print()
    print("Thank you for shopping at the Inkom Emporium.")
    print(f"{current_date_and_time:%c}")
    print()
    print("COUPON ALERT")
    print("Check out this hot new deal on yogurt: ")
    print("2 for the price of 1!")
    print("Expires 03/27")


def read_products(products_file):  
    products = {}    

    try: 
        with open(products_file, "rt") as products_dict:
            reader = csv.reader(products_dict)
            next(reader)

            for row in reader:
                number_index = row[PRODUCTS_NUMB_INDEX]
                name = row[NAME_INDEX]
                price = row[PRICE_INDEX]
                products[number_index] = [name, price]


    except FileNotFoundError as not_found_err:
        print(f"Error: missing file")

    except PermissionError as perm_err:
        print(f"Error: access not allowed")
    
    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file '{key_err}'")

    return products 


def list_request(request_file, products_file):
    product_dict = read_products(products_file)

    with open(request_dict, "rt") as request_dict:
        reader = csv.reader(request_dict)
        next(reader)

        print("Requested items: ")

        numb_items = 0
        total = 0
        sub_total = 0

        for row in reader:
            numb_index = row[PRODUCTS_NUMB_INDEX]
            product_quantity = row[QUANTITY_INDEX]
            quantity = int(product_quantity)

            if numb_index in product_dict.keys():
                product = product_dict[numb_index]
                name = product[0]
                price = float(product[1])
                print(f"{name}: {product_quantity} @ {price}")

                sub_total = sub_total + quantity * price
            numb_items = sum[QUANTITY_INDEX]

        sales_tax = 0.06 * sub_total
        total = sales_tax + sub_total 

        print()
        print(f"Number of Items: {numb_items}")     
        print(f"Subtotal: {sub_total}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")



if __name__ == "__main__":
    main()