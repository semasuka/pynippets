
"""
converter to convert a decimal number to binary or a binary number to its decimal equivalent.
"""

def correct_input_check():
    correct_input = False
    while not correct_input:
        try:
            the_input = int(input())
        except ValueError:
            print("\nError!,Please enter a number")
        else:
            if the_input > 0:
                correct_input = True
                return the_input
            else:
                print("\nPlease enter a number greater than 0")

def decimal_to_binary():
    print("\nEnter a decimal number:")
    num = correct_input_check()
    #printing in binary format 
    print("\nThe binary number is {0:b}".format(num))

def binary_check():
    correct_bi = False
    bi = 0
    while not correct_bi:
        print("\nEnter a binary number:")
        bi = correct_input_check()
        bi = str(bi)
        bi_list = []

        for digit in bi:
            bi_list.append(int(digit))

        for digit in bi_list:
            if digit != 0 and digit != 1:
                print("\nA binary number is written with 0 and 1")
                break
        else:
            correct_bi = True
    return bi
def binary_to_decimal():
    bi = binary_check()
    # codes of calculation bi to dec goes here
    print("\nThe binary number is {0}".format(int(str(bi),2)))

def choice_switch(choice):
    #switcher to choose between binary or decimal
    switcher = {
        1:decimal_to_binary,
        2:binary_to_decimal
    }
    dec_bi = switcher.get(choice)
    dec_bi()

correct_choice = False
while not correct_choice:
    try:
        choice = int(input("Enter 1 or 2:\n1.To convert a decimal to binary\n2.To convert a binary to decimal\n\n"))
    except ValueError:
        print("\nInvalid input\n")
    else:
        if choice == 1 or choice == 2:
            correct_choice = True
            choice_switch(choice)
        else:
            print("\nPlease enter 1 or 2\n")