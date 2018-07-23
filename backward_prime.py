"""
Backwards Read Primes are primes that when read backwards in base 
10 (from right to left) are a different prime. 
(This rules out primes which are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes
13 is such because it's prime and read from right to left writes 
31 which is prime too. Same for the others.

Task
Find all Backwards Read Primes between two positive given numbers 
(both inclusive), the second one being greater than the first one. 
The resulting array or the resulting string will be ordered 
following the natural order of the prime numbers.

Example
backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] 
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]

backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] 
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]

"""
def backwardsPrime(start, stop):
    prime_list = []
    for possibly_prime in range(start,stop+1):
        for i in range(2,possibly_prime):
            if possibly_prime%i == 0:
                break
        else:
            prime_list.append(possibly_prime)
    print(prime_list)

    big_prime = []
    for prime in prime_list:
        if len(str(prime)) >=2:
            big_prime.append(prime)

    rev_big_prime = []
    for digit in big_prime:
        rev_big_prime.append(int(str(digit)[::-1]))
    dup = list(set(rev_big_prime) & set(big_prime))

    for num in dup:
        if len(set(str(num))) == 1:
            del dup[dup.index(num)]
    return dup


print(backwardsPrime(9900, 10000))