"""
Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.
"""

import math


def pi_nth(decimal):
    PI = math.pi

    return "{0:.{1}f}".format(PI, decimal)


while True:
    try:
        input_num = int(input("Enter the number of decimal of PI\n"))
    except ValueError:
        print("enter a number")
        continue
    else:
        print(pi_nth(input_num))
