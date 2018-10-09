"""
##The Brief Microsoft Excel provides a number of useful
functions for counting, summing, and averaging values
if they meet a certain criteria. Your task is to write
three functions that work similarly to Excel's COUNTIF,
SUMIF and AVERAGEIF functions.

##Specifications Each function will take the same two
arguments:

A list object containing values to be counted, summed,
or averaged.
A criteria in either an integer, float, or string
Integer or float indicates equality
Strings can indicate >, >=, <, <= or <>
(use the Excel-style "Not equal to" operator) to a
number (ex. ">=3"). In the count_if function, a string
without an operater indicates equality to this string.


The tests will all include properly formatted inputs.
The test cases all avoid rounding issues associated
with floats.

##Examples

count_if([1,3,5,7,9], 3)
1

count_if(["John","Steve","John"], "John")
2

sum_if([2,4,6,-1,3,1.5],">0")
16.5

average_if([99,95.5,0,83],"<>0")
92.5
##Excel Function Documentation:

COUNTIF
SUMIF
AVERAGEIF
"""
from __future__ import division


def count_if(values,criteria):
    special_char_found = ""
    special_char = [">","<","="]
    index_count = 0
    final_count_no_sign = 0
    final_count_with_sign = 0

    for char in str(criteria):
        if char in special_char:
            index_count +=1
            special_char_found += char
    else:
        for word in values:
            if word == criteria:
                final_count_no_sign += 1
    if final_count_no_sign != 0:
        return final_count_no_sign
    else:

        if special_char_found == ">":
            for i in values:
                if i > float(criteria[index_count:]):
                    final_count_with_sign +=1
            return final_count_with_sign
        elif special_char_found == ">=":
            for i in values:
                if i >= float(criteria[index_count:]):
                    final_count_with_sign += 1
            return final_count_with_sign
        elif special_char_found == "<":
            for i in values:
                if i < float(criteria[index_count:]):
                    final_count_with_sign += 1
            return final_count_with_sign
        elif special_char_found == "<=":
            for i in values:
                if i <= float(criteria[index_count:]):
                    final_count_with_sign += 1
            return final_count_with_sign
        else:
            for i in values:
                if i != float(criteria[index_count:]):
                    final_count_with_sign += 1
            return final_count_with_sign


def sum_if(values,criteria):
    special_char_found = ""
    special_char = [">","<","="]
    index_count = 0
    sum_no_sign = 0
    sum_with_sign = 0

    for char in str(criteria):
        if char in special_char:
            index_count +=1
            special_char_found += char
    else:
        for num in values:
            if num == criteria:
                sum_no_sign += num
    if sum_no_sign != 0:
        return sum_no_sign
    else:
        if special_char_found == ">":
            for i in values:
                if i > float(criteria[index_count:]):
                    sum_with_sign += i
            return sum_with_sign
        elif special_char_found == ">=":
            for i in values:
                if i >= float(criteria[index_count:]):
                    sum_with_sign += i
            return sum_with_sign
        elif special_char_found == "<":
            for i in values:
                if i < float(criteria[index_count:]):
                    sum_with_sign += i
            return sum_with_sign
        elif special_char_found == "<=":
            for i in values:
                if i <= float(criteria[index_count:]):
                    sum_with_sign += i
            return sum_with_sign
        else:
            for i in values:
                if i != float(criteria[index_count:]):
                    sum_with_sign += i
            return sum_with_sign

def average_if(values,criteria):
    special_char_found = ""
    special_char = [">","<","="]
    index_count = 0
    sum_no_sign = 0
    num_count = 0
    sum_with_sign = 0

    for char in str(criteria):
        if char in special_char:
            index_count +=1
            special_char_found += char
    else:
        for num in values:
            if num == criteria:
                num_count += 1
                sum_no_sign += num
    if sum_no_sign != 0:
        return sum_no_sign//num_count
    else:

        if special_char_found == ">":
            for i in values:
                if i > float(criteria[index_count:]):
                    num_count += 1
                    sum_with_sign += i
            result = sum_with_sign/num_count
            if str(result-int(result))[1:] == ".0":
                return int(result)
            else:
                return result

        elif special_char_found == ">=":
            for i in values:
                if i >= float(criteria[index_count:]):
                    num_count += 1
                    sum_with_sign += i
            result = sum_with_sign/num_count
            if str(result-int(result))[1:] == ".0":
                return int(result)
            else:
                return result

        elif special_char_found == "<":
            for i in values:
                if i < float(criteria[index_count:]):
                    num_count += 1
                    sum_with_sign += i
            result = sum_with_sign/num_count
            if str(result-int(result))[1:] == ".0":
                return int(result)
            else:
                return result

        elif special_char_found == "<=":
            for i in values:
                if i <= float(criteria[index_count:]):
                    num_count += 1
                    sum_with_sign += i
            result = sum_with_sign/num_count
            if str(result-int(result))[1:] == ".0":
                return int(result)
            else:
                return result
        else:
            for i in values:
                if i != float(criteria[index_count:]):
                    num_count += 1
                    sum_with_sign += i
            result = sum_with_sign/num_count
            if str(result-int(result))[1:] == ".0":
                return int(result)
            else:
                return result

# print(count_if([1,3,5,3,0,-1,-5],'<>1'))
# print(sum_if([1,3,5,3,0,-1,-5],'<>1'))
print(average_if([1,3,5,3,0,-1,-5],'<>1'))
# print(type(average_if([1,3,5,3,0,-1,-5],'<1')))