"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal 
format. IPs should be considered valid if they consist of four octets, 
with values between 0..255 (included).

Input to the function is guaranteed to be a single string.

Examples
// valid inputs:
1.2.3.4
123.45.67.89

// invalid inputs:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Note: leading zeros (e.g. 01.02.03.04) are considered not valid in this kata!
"""
def is_valid_IP(the_string):
    the_string_list = []
    #splitting all the string using .
    for digit in the_string.split("."):
        the_string_list.append(digit)
    print(the_string_list)
    approved_num = []
    is_gone_through = True
    #if we have exatcly the 4 element in the list
    if len(the_string_list) == 4:
        for num in the_string_list:
            if num.isdigit():
                if len(num)==1:
                    if num in str(range(10)):
                        approved_num.append(True)
                elif len(num) == 2 or len(num) == 3:
                    if num[0] != "0":
                        if int(num) in range(256):
                            approved_num.append(True)
                        else:
                            approved_num.append(False)
                    else:
                        approved_num.append(False)
                else:
                    approved_num.append(False)
            else:
                is_gone_through = False
                return False

    else:
        is_gone_through = False
        return False

    if is_gone_through:
        #remove all the duplicate True and False
        non_dup = set(approved_num)
        non_dup = list(non_dup)
        non_dup_len = len(non_dup)
        #if there is no duplicated
        if non_dup_len == 1:
            return True
        else:
            return False


print(is_valid_IP('192.168.1.300'))


