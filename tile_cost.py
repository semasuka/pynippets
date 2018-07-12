"""
Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
"""

try:
    width = float(input("Enter the width:\n"))
    height = float(input("Enter the height:\n"))
    cost = float(input("Enter the cost:\n"))
except ValueError:
    print("Please enter a number")
else:
    result = lambda width,height,cost:width*height*cost
    print("the cost is {0:.2f}".format(result(width,height,cost)))
