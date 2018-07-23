"""
Write a function that accepts an array of 10 integers 
(between 0 and 9), that returns a string of those numbers 
in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => 
returns "(123) 456-7890"
The returned format must be correct in order to complete 
this challenge. 
Don't forget the space after the closing parentheses!
"""

def create_phone_number(nums):
    if len(nums) !=0:
        num_string = ""
        ite_count = 0
        for num in nums:
            ite_count += 1
            if ite_count == 1:
                num_string += "("+str(num)
            elif ite_count == 2:
                num_string += str(num)
            elif ite_count == 3:
                num_string += str(num)+") "
            elif ite_count >= 4 and ite_count <= 6:
                num_string += str(num)
            elif ite_count == 7:
                num_string += "-"+str(num)
            else:
                num_string += str(num)

        return num_string
    else:
        return ""

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))