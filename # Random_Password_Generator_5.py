# Random_Password_Generator_5

import secrets, string, random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation
all_characters = lower + upper + digits + special

password = ""

length = int(input("How many characters do you want in your password? "))
minimum_upper = int(input("Minimum upper case: "))
minimum_lower = int(input("Minimum lower case: "))
minimum_digits = int(input("Minimum numbers: "))
minimum_special = int(input("Minimum special: "))

for i in range(minimum_upper):
    password += "".join(random.choice(secrets.choice(upper)))

for i in range(minimum_lower):
    password += "".join(random.choice(secrets.choice(lower)))   

for i in range(minimum_digits):
    password += "".join(random.choice(secrets.choice(digits)))

for i in range(minimum_special):
    password += "".join(random.choice(secrets.choice(special)))  

remaining = length - minimum_lower - minimum_upper - minimum_digits - minimum_special

for i in range(remaining): 
    password += "".join(random.choice(secrets.choice(all_characters))) 

password = list(password)
random.shuffle(password)
print("".join(password))