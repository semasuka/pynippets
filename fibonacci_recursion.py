"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    if position >= 2:
        return get_fib(position-1)+get_fib(position-2)
    elif position == 1 or position == 0:
        return position
    else:
        raise Exception("Enter a positive number for the position")


# Test cases

print(get_fib(0))
print(get_fib(1))
print(get_fib(2))
print(get_fib(3))
print(get_fib(4))
print(get_fib(5))
print(get_fib(6))
print(get_fib(7))
print(get_fib(8))
print(get_fib(9))
print(get_fib(10))
print(get_fib(-11))
print(get_fib(-242))
