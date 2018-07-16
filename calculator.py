A simple calculator to do basic operators. Scientific calculator to be added for more complexity
"""
import math


def addition(num1,num2):
    return num1+num2
def substraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def modulo(num1,num2):
    return num1%num2
def power(num1,num2):
    return num1**num2
def factorial(num1):
    if num1 == 0:
        return 1
    else:
        return num1 * factorial(num1-1)
    
def power_2(num1):
    return num1**2
def power_3(num1):
    return num1**3
def sqr_root(num1):
    return math.sqrt(num1)
def cube_root(num1):
    return num1 ** (1/3)
def log_fun(num1):
    return math.log10(num1)
def ln_fun(num1):
    return math.log(num1,math.e)
def e_power(num1):
    return math.e**num1
def cos_fun(num1):
    return math.cos(num1)
def sin_fun(num1):
    return math.sin(num1)
def tan_fun(num1):
    return math.tan(num1)
def acos_fun(num1):
    return math.acos(num1)
def asin_fun(num1):
    return math.asin(num1)
def atan_fun(num1):
    return math.atan(num1)




correct_input = False
while not correct_input:
    try:
        #first number input
        num1 = float(input("Enter the first number:\n"))
        #displaying the menu of operator
        correct_choice = False
        while not correct_choice:
            choice = int(input("\nEnter:\n1--For Addition(+)\n2--For Substraction(-)\n3--For Multiplication(X)\n4--For Division(/)\n5--For Modulo(%)\n6--For Power(**)\n7--For Factorial(x!)\n8--For Power 2(x^2)\n9--For Power 3(x^3)\n10--For Square Root(x^(1/2))\n11--For Cube Root(x^(1/3))\n12--For Log(log(x))\n13--For Ln(ln(x))\n14--For Euler Power(e^x)\n15--For Cos(cos(x))\n16--For Sin(sin(x))\n17--For Tan(tan(x))\n18--For Acos(acos(x))\n19--For Asin(asin(x))\n20--For Atan(atan(x))\n\n"))
            #if the choice is not between 1 and 5
            if choice in range(1,7):
                correct_choice = True
                num2 = float(input("\nEnter the second number:\n"))
            #if the choice is betwen 6 and 20
            elif choice in range(6,21):
                correct_choice = True

            #loop back
            else:
                print("\nPlease enter a number between 1 and 20")
                continue
    except ValueError:
        print("\nPlease enter a number")
    else:
        
        correct_input = True
        def switch_choice(*args):
            switcher = {
                1:addition,
                2:substraction,
                3:multiplication,
                4:division,
                5:modulo,
                6:power,
                7:factorial,
                8:power_2,
                9:power_3,
                10:sqr_root,
                11:cube_root,
                12:log_fun,
                13:ln_fun,
                14:e_power,
                15:cos_fun,
                16:sin_fun,
                17:tan_fun,
                18:acos_fun,
                19:asin_fun,
                20:atan_fun
            }
            #for num1,choice,num2 in args:  
            choice_fun = switcher.get(choice)
            try:
                return choice_fun(num1,num2)
            #if num2 does not exist
            except TypeError:
                return choice_fun(num1)
    try:
        result = switch_choice(num1,choice,num2)
    except NameError:
        #if num2 does not exist
        result = switch_choice(num1,choice)
    else:
        print("\nThe result is {0:.2f}".format(result))