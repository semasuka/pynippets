
#memoize class
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

#normal fibonaci using recursion O(2^n)
def fibonacci_rec(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

cache = {}
#fibonaci using memoize O(n)
def fibonacci_mem(n):

    if n < 2:
        return 1
    else:
        if not n in cache:
            cache[n] =  fibonacci_mem(n-1) + fibonacci_mem(n-2)
    return cache[n]
#fibonacci using dynamic programing
def fibonacci_dp(n):
    if n < 2:
        return 2
    bottom_up = {}
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3,n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

for i in range(101):
    print(i," : ",fibonacci_dp(i))
    
#fibonacci using iteration
def fib_ite(n):
    a,b = 0,1
    
    for _ in range(n):
        a,b = b, b+a
    return a
print(fib_ite(5))
    
   
