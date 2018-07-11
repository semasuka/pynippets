"""
A program that ask for the limit of n prime number and ask if the user want to keep reveiling the sequence of prime number
"""


def next_prime(limit_num):
    #prime number start from 2
    for num in range(2,limit_num+1):
        isPrime = True
        for i in range(2,num):
            #if divisible by one of its multiply, then not a prime number 
            if num % i == 0:
                isPrime = False
        #if not, then it is a prime number
        if isPrime:
            yield num
                


try:
    limit_num = int(input("Please enter the prime numbers limit:\n"))
#trow an exception when the value input is not a number
except ValueError:
    print("Please enter a number as a limit")
else:
    the_prime = next_prime(limit_num)
    #print the first prime number
    print("The first prime number is: ",next(the_prime))
    
    choice=" "
    #keep on looping if the input is not n or y
    while choice[0] != "y" or choice[0] != "n":
        choice = input("Do you want to display the next prime?[y/n]:\n").lower()
        if choice[0] == "y":
            try:
                #using generator to display the next prime
                print("\nThe next prime number is ",next(the_prime))
            except StopIteration:
                print("\nLimit of the numbers reached")
                
        elif choice[0] == "n":
            break
        else:
            print("Please enter yes or no")
            continue
        
    
