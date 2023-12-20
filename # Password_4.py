# Password_4

import string, random

def main(): 
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)
    
    length = input("How many characters do you want in your password? ")
    
    while True:
        try:
            characters_number = int(length)
            if characters_number < 8:
                print("Your number should be at least 8.")
                length = input("Please, Enter your number again: ")
            else:
                break
        except:
            print("Please, Enter numbers only.")
            length = input("How many characters do you want in your password? ")
    
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)
    
    part1 = round(characters_number * (30/100))
    part2 = round(characters_number * (20/100))
    
    result = []
    
    for i in range(part1):
        result.append(s1[i])
        result.append(s2[i])
    
    for i in range(part2):
        result.append(s3[i])
        result.append(s4[i])
    
    random.shuffle(result)
    
    password = "".join(result)
    print("Strong Password: ", password)




    # except KeyError as key_error:
    #     print(
    #         f"Error: line {reader.line_num} of {filename.name} is formatted incorrectly. ")
    #     print(key_error)

    # except FileNotFoundError as file_not_found_error:
    #     print(f"Error: cannot open {filename} because it doesn't exist.")
    #     print(file_not_found_error)
    #     exit()

    # except PermissionError as permission_error:
    #     print(
    #         f"Error: cannot read from {filename} because you don't have permission.")
    #     print(permission_error)
    #     exit()


if __name__ == "__main__":
    main()