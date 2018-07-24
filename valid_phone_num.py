"""
Write a function that accepts a string, and returns true if it is in 
the form of a phone number. 
Assume that any integer from 0-9 in any of the spots will produce a 
valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses) 

Examples:

validPhoneNumber("(123) 456-7890")  =>  returns true
validPhoneNumber("(1111)555 2345")  => returns false
validPhoneNumber("(098) 123 4567")  => returns false

"""
def validPhoneNumber(phone_number):
    phone_number_digit_count = 0
    for char in phone_number:
        if char.isdigit():
            phone_number_digit_count += 1
    #if the digit in phone number must be always 10
    if phone_number_digit_count == 10:
        #the length of the phone number is always 14
        if len(phone_number) == 14:
            if phone_number[0] == "(" and phone_number[4] == ")" and phone_number[5] == " " and phone_number[9] == "-":
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(validPhoneNumber("(133) 453-7890"))