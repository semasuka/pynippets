"""
A simple calculator to do basic operators. Scientific calculator to be added for more complexity
"""
def addition(num1,num2):
    #print("{0} Add {1}".format(num1,num2))
    return num1+num2
def substraction(num1,num2):
    #print("{0} substraction {1}".format(num1,num2))
    return num1-num2
def multiplication(num1,num2):
    #print("{0} multiplication {1}".format(num1,num2))
    return num1*num2
def division(num1,num2):
    #print("{0} division {1}".format(num1,num2))
    return num1/num2
def modulo(num1,num2):
    #print("{0} modulo {1}".format(num1,num2))
    return num1%num2


correct_input = False
while not correct_input:
    try:
        #first number input
        num1 = float(input("Enter the first number:\n"))
        #displaying the menu of operator
        correct_choice = False
        while not correct_choice:
            choice = int(input("\nEnter:\n1--For Addition\n2--For Substraction\n3--For Multiplication\n4--For Division\n5--For Modulo\n\n"))
            #if the choice is not between 1 and 5
            if choice in range(6):
                correct_choice = True
                num2 = float(input("\nEnter the second number:\n"))
            #loop back
            else:
                print("\nPlease enter a number between 1 and 5")
                continue
    except ValueError:
        print("\nPlease enter a number")
    else:
        
        correct_input = True
        def switch_choice(num1,choice,num2):
            switcher = {
                1:addition,
                2:substraction,
                3:multiplication,
                4:division,
                5:modulo
            }
            choice_fun = switcher.get(choice)
            return choice_fun(num1,num2)
        result = switch_choice(num1,choice,num2)
        print("\nThe result is {0:.2f}".format(result))
        #print("Choose between 1 and 5")
    