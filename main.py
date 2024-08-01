import os
import sys
import time
from random import choice, randint
from string import ascii_letters, punctuation, digits

#os.system("clear")
#print("zlash")

#time.sleep(5)

os.system("clear") # terminal cmd  

print("Password Generator:\n\n") 

num_of_passwd = input("How many passwords would you like to generate?\n")
if not num_of_passwd.isdigit(): # checks if its digit or not
    sys.exit("Error 406 - Not Acceptable") # funny error idk why i put that there
num_of_passwd = int(num_of_passwd)

char_num = input("Please type in how many characters your password(s) should be: ")
if not char_num.isdigit(): # same check
    sys.exit("Error 406 - Not Acceptable")

# complex logic on either using ascii, digits punc or all
passwd_format_one = ascii_letters
passwd_format_two = digits
passwd_format_three = punctuation
passwd_format_all = passwd_format_one + passwd_format_two + passwd_format_three
passwd_format_onetwo = passwd_format_one + passwd_format_two
passwd_format_twothree = passwd_format_two + passwd_format_two
passwd_format_onethree = passwd_format_one + passwd_format_three

char_num = int(char_num)
type_of_chars = input("Do you want your password(s) to have letters, numbers and/or symbols?\n Please pick from the list below by selecting 1, 2, and/or 3.\n You can also say 'all' or combine numbers, 12.\n 1. Letters\n 2. Numbers\n 3. Symbols\n Please pick now: ")
if type_of_chars == "all" or "123" or "132" or "213" or "231" or "321" or "312": 
    for x in range (num_of_passwd):
        generated_passwd = "".join(choice(passwd_format_all) for x in range(char_num))
    print("Your Generated Password(s) are: " + generated_passwd)
elif type_of_chars == "1":
    for x in range (num_of_passwd):
        generated_passwd = "".join(choice(passwd_format_one) for x in range(char_num))
    print("Your Generated Password is: " + generated_passwd)
elif type_of_chars == "2":
    for x in range (num_of_passwd):
        generated_passwd = "".join(choice(passwd_format_two) for x in range(char_num))
    print("Your Generated Password is: " + generated_passwd)
elif type_of_chars == "3":
    for x in range (num_of_passwd):
        generated_passwd = "".join(choice(passwd_format_three) for x in range(char_num))
    print("Your Generated Password is: " + generated_passwd)
elif type_of_chars == "12" or "21":
    for x in range (num_of_passwd):
        generated_passwd = "".join(choice(passwd_format_onetwo) for x in range(char_num))
    print("Your Generated Password is: " + generated_passwd)
elif type_of_chars == "23" or "32":
    for x in range (num_of_passwd):
        generated_passwd = "".join(choice(passwd_format_twothree) for x in range(char_num))
    print("Your Generated Password is: " + generated_passwd)
elif type_of_chars == "13" + "31":
    for x in range (num_of_passwd):
        generated_passwd = "".join(choice(passwd_format_onethree) for x in range(char_num))
    print("Your Generated Password is: " + generated_passwd)
else:
    sys.exit("Error 406 - Not Acceptable")