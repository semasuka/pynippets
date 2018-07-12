"""
Calculate the monthly payments of a fixed term mortgage 
over given Nth terms at a given interest rate. Also figure 
out how long it will take the user to pay back the loan.
"""

months = int(input("Please enter the mortgage term (in months):\n"))
interest_rate = float(input("Please enter the interest rate:\n"))
loan = float(input("Please enter the loan value:\n"))
payment = 0
def paymeny_cal(months,interest_rate,loan):
    global payment
    monthly_rate = interest_rate/100/12
    payment = (monthly_rate/(1-(1+monthly_rate)**(-months)))*loan
    print("\nMonthly payment is {0:.2f}".format(payment))

paymeny_cal(months,interest_rate,loan)