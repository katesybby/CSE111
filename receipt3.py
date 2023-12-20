#LUCY'S VERSION OF RECEIPT.PY

import csv
from datetime import datetime


def main():
    products_file = "products.csv"
    products = read_dictionary(products_file)

    print ("\nInkom Emporium\n")

    requests_file = "request.csv"
    process_request(requests_file, products_file)

def read_dictionary(filename):
    products = {}

    try:
        with open(filename, "rt") as infile:
            reader = csv.reader(infile)
            next(reader)

            for line in reader:
                product_number = line[0]
                product_name = line[1]
                product_price = line [2]
                products[product_number] = [product_name, product_price]
        
    except KeyError as key_error:
        print(
            f"Error: line {reader.line_num} of {filename.name} is formatted incorrectly. ")
        print(key_error)

    except FileNotFoundError as file_not_found_error:
        print(f"Error: cannot open {filename} because it doesn't exist.")
        print(file_not_found_error)
        exit()

    except PermissionError as permission_error:
        print(
            f"Error: cannot read from {filename} because you don't have permission.")
        print(permission_error)
        exit()
    return products

def process_request(requests_file, products_file):
    product_dic = read_dictionary(products_file)
    current_date_and_time = datetime.now()

    with open(requests_file, "rt") as infile:
        reader = csv.reader(infile)
        next(reader)

        print("Requested items:")

        number_items = 0
        total = 0
        sub_total = 0
        sales_tax_rate = 0.06

        for line in reader:
            product_number = line[0]
            product_quantity = line[1]
            quantity = int(product_quantity)

            if product_number in product_dic.keys():
                product = product_dic[product_number]
                name = product[O]
                price = float(product[1])
                print(f"{name}: {product_quantity} @ {price}")

                sub_total = sub_total + quantity * price
            number_items = number_items + quantity

        print (f"\nNumber of Items: {number_items}")
        print(f"Subtotal: {sub_total}")

        sales_tax = sales_tax_rate * sub_total
        print(f"Sales Tax: {sales_tax:.2f}")

        total = sub_total + sales_tax

        print(f"Total: {total:.2f}")
        print("\nThank you for shopping at the Inkom Emporium!")
        print(f"{current_date_and_time:%c}")


if __name__ == "__main__":
    main()