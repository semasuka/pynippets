"""
return 1 if num1 contain some K digit 3 consecutive time and num2 contain K digit 2 consecutive time
"""
def triple_double(num1, num2):
    num1_list = []
    #conveting to string
    for num in str(num1):
        num1_list.append(int(num))
    num2_list = []
    for num in str(num2):
        num2_list.append(int(num))
  

    #duplicate container
    num1_dup = {}
    num2_dup = {}

    #adding the dup to container dictonary
    for num in num1_list:
        if num not in num1_dup:
            num1_dup[num] = 0
        num1_dup[num] += 1

    num1_dup_3 = []

    for key,value in num1_dup.items():
        if value >= 3:
            num1_dup_3.append(key)

    for num in num2_list:
        if num not in num2_dup:
            num2_dup[num] = 0
        num2_dup[num] += 1

    num1_dup_2 = []

    for key,value in num2_dup.items():
        if value >= 2:
            num1_dup_2.append(key)

    #check if the digit is at the same time in num1_dup_3 and in num2_dup_2
    for digit in num1_dup_3:
        if digit in num1_dup_2:
            return 1
        else:
            return 0
    return 0

print(triple_double(666789, 12345667))