"""
 Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
"""

def fib(lim_fib):
    a = 1
    b = 1

    for i in range(lim_fib):
        yield a
        #set a to be equal to be and set b to be equal to a+b
        a, b = b, a + b


lim_fib = int(input("Enter the limit of the fibonacci"))

for i in fib(lim_fib):
    print(i)
