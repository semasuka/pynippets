"""
We have a string s

We have a number n

Here is a function that takes your string, 
concatenates the even-indexed chars to the front, 
odd-indexed chars to the back.

n is the number of iteration
"""
def jumbled_string(s, n):
    def change_string(s):
        even_char = []
        odd_char = []
        #even chracter
        for char in s[::2]:
            even_char.append(char)
        #odd character
        for char in s[1::2]:
            odd_char.append(char)
        even_char_str = ""
        odd_char_str = ""
        for i in even_char:
            even_char_str+=i
        for i in odd_char:
            odd_char_str+=i

        return even_char_str+odd_char_str

    first_it = change_string(s)
    if n == 1:
        return first_it
    else:
        for i in range(n):
            nxt_it = change_string(first_it)
            return nxt_it




print(jumbled_string("Greetings",8))