"""
Complete the function/method so that it takes CamelCase string and returns the string in 
snake_case notation. Lowercase characters can be numbers. If method gets number,
 it should return string.

Examples:

# returns test_controller
to_underscore('TestController')

# returns movies_and_books
to_underscore('MoviesAndBooks')

# returns app7_test
to_underscore('App7Test')

# returns "1"
to_underscore(1)
"""
def to_underscore(the_string):
    # your code here
    the_string_final = ""
    for char in str(the_string):
        if char.isalpha():
            if char.istitle():
                if char is not the_string[0]:
                    the_string_final += "_"+char.lower()
                else:
                    the_string_final += char.lower()
            else:
                the_string_final += char
        else:
            the_string_final += char
    return the_string_final



print(to_underscore("App7Test"))