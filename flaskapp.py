from flask import Flask, render_template, request, redirect, url_for
import os
import sys
from random import choice
from string import ascii_letters, punctuation, digits

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    num_of_passwd = request.form['num_of_passwd'] # form data for pw num
    char_num = request.form['char_num'] # chars in pw
    type_of_chars = request.form['type_of_chars'] # what types of chars

    if not num_of_passwd.isdigit() or not char_num.isdigit(): # check point for if its nto a digit
        return "Error 406 - Not Acceptable", 406 # funny error idk why i put that there

    num_of_passwd = int(num_of_passwd)
    char_num = int(char_num)

    # complex logic on either using ascii, digits punc or all
    passwd_format_one = ascii_letters
    passwd_format_one = ascii_letters
    passwd_format_two = digits
    passwd_format_three = punctuation
    passwd_format_all = passwd_format_one + passwd_format_two + passwd_format_three
    passwd_format_onetwo = passwd_format_one + passwd_format_two
    passwd_format_twothree = passwd_format_two + passwd_format_three
    passwd_format_onethree = passwd_format_one + passwd_format_three

    passwords = []
    # the if else statements for checking all various combinations
    if type_of_chars in ["all", "123", "132", "213", "231", "321", "312"]:
        for _ in range(num_of_passwd):
            generated_passwd = "".join(choice(passwd_format_all) for _ in range(char_num))
            passwords.append(generated_passwd)
    elif type_of_chars == "1":
        for _ in range(num_of_passwd):
            generated_passwd = "".join(choice(passwd_format_one) for _ in range(char_num))
            passwords.append(generated_passwd)
    elif type_of_chars == "2":
        for _ in range(num_of_passwd):
            generated_passwd = "".join(choice(passwd_format_two) for _ in range(char_num))
            passwords.append(generated_passwd)
    elif type_of_chars == "3":
        for _ in range(num_of_passwd):
            generated_passwd = "".join(choice(passwd_format_three) for _ in range(char_num))
            passwords.append(generated_passwd)
    elif type_of_chars in ["12", "21"]:
        for _ in range(num_of_passwd):
            generated_passwd = "".join(choice(passwd_format_onetwo) for _ in range(char_num))
            passwords.append(generated_passwd)
    elif type_of_chars in ["23", "32"]:
        for _ in range(num_of_passwd):
            generated_passwd = "".join(choice(passwd_format_twothree) for _ in range(char_num))
            passwords.append(generated_passwd)
    elif type_of_chars in ["13", "31"]:
        for _ in range(num_of_passwd):
            generated_passwd = "".join(choice(passwd_format_onethree) for _ in range(char_num))
            passwords.append(generated_passwd)
    else:
        return "Error 406 - Not Acceptable", 406 # funny error again, i should prob change this soon

    return render_template('index.html', passwords=passwords)

if __name__ == '__main__':
    app.run(debug=True)
