"""
There is a common problem given to interviewees in software. 
It is called FizzBuzz. It works as follows: For the numbers 
between 1 and 100, print fizz if it is a multiple of 3 and 
buzz if it is a mutiple of 5, else print the number itself.

You are in an interview and they ask you to complete fizzbuzz 
(which can be done in a one-liner in a few langs) and you knock 
it out of the park.

Surprised by your ability, the interviewer gives you a harder 
problem. Given a list of coprime numbers, (that is that the g.c.d. 
of all the numbers == 1) and an equally sized list of words. 
compute its fizzbuzz representation up until the pattern of 
strings repeats itself.

Here's an example

fizzbuzz_plusplus([2, 3, 5], ['fizz', 'buzz', 'bazz']); 
// => [1, 'fizz', 'buzz', 'fizz', 'bazz', 'fizzbuzz', 7, 
'fizz', 'buzz', 'fizzbazz', 11, 'fizzbuzz', 13, 'fizz', 
'buzzbazz', 'fizz', 17, 'fizzbuzz', 19, 'fizzbazz', 'buzz', 
'fizz', 23, 'fizzbuzz', 'bazz', 'fizz', 'buzz', 'fizz', 29 ,
 'fizzbuzzbazz']
Things to note:

Your function should return an Array of the output for each index, not print it.
If elements are 1-indexed, the 10th item is fizz + bazz as 10 == 0 (mod 2) and 10 == 0 (mod 5).
The strings are always concatenated from left to right in appearance of array.
The number array may not always be sorted - just use the given order of the numbers
All numbers in the first array will always be coprime. This is a safe assumption for your program.
The list stops where it does because if you were to filter the numbers out, the remaining strings would repeat after this point.
Hint: What is the relation to the numbers given in the list and the length of the list?
"""

def fizzbuzz_plusplus(nums, words):
    nums_words = dict(zip(nums,words))
    #print(nums_words)
    max_range = 1
    for num in nums:
        max_range *=num
    #print(max_range)
    words_for_multip = ""
    for values in nums_words.values():
        words_for_multip+=values
    #print(words_for_multip)
    nums_words.update({max_range:words_for_multip})
    #print(nums_words)

    the_list_origin = []
    for num in range(1,max_range+1):
        the_list_origin.append(num)
    #print(the_list_origin)

    the_list_final = []
    for num in the_list_origin:
        for keys,value in nums_words.items():
            if num%keys == 0 and num%max_range == 0:
                the_list_final.append(words_for_multip)
                break
            # elif num%int(str(keys)[0]) == 0 and num%int(str(keys)[1]) == 0:
            #     the_list_final.append(value[0]+value[1])
            #     break
            elif num%keys == 0:
                the_list_final.append(value)
                break
        else:
            the_list_final.append(num)
    return the_list_final



print(fizzbuzz_plusplus([2,3],["fizz","buzz"]))