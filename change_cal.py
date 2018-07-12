"""
The user enters a cost and then the amount of money given. The program will figure out the change in Kenyan Shillings
"""
import math

can_continue = False

#while loop to make sure that money given is less than the product cost
while not can_continue:
    money_given = float(input("Enter the amount of money given\n"))
    cost_product = float(input("Enter the cost of the product\n"))
    if money_given >= cost_product:
        can_continue = True
        break
    else:
        print("Money given less than the cost of the product")
        continue

return_change = money_given-cost_product
original_change = return_change
def slipted_change(return_change,original_change):
    #setting the value of the bill note and count
    bill_1000 = 1000
    bill_1000_count = 0
    bill_500 = 500
    bill_500_count = 0
    bill_200 = 200
    bill_200_count = 0
    bill_100 = 100
    bill_100_count = 0
    bill_50 = 50
    bill_50_count = 0
    coin_40 = 40
    coin_40_count = 0
    coin_20 = 20
    coin_20_count = 0
    coin_10 = 10
    coin_10_count = 0
    coin_5 = 5
    coin_5_count = 0
    coin_1 = 1
    coin_1_count = 0

    if return_change >= 1000:
        bill_1000_count = return_change/bill_1000 #get how many 1000 notes are there
        bill_1000_count = math.floor(bill_1000_count) 
        return_change = return_change - (1000*bill_1000_count)#count the rest after substraction the 1000 notes previous found
    if return_change >= 500:
        bill_500_count = return_change/bill_500
        bill_500_count = math.floor(bill_500_count) 
        return_change = return_change - (500*bill_500_count)
    if return_change >= 200:
        bill_200_count = return_change/bill_200
        bill_200_count = math.floor(bill_200_count) 
        return_change = return_change - (200*bill_200_count)
    if return_change >= 100:
        bill_100_count = return_change/bill_100
        bill_100_count = math.floor(bill_100_count) 
        return_change = return_change - (100*bill_100_count)
    if return_change >= 50:
        bill_50_count = return_change/bill_50
        bill_50_count = math.floor(bill_50_count) 
        return_change = return_change - (50*bill_50_count)
    if return_change >=40:
        coin_40_count = return_change/coin_40
        coin_40_count = math.floor(coin_40_count) 
        return_change = return_change - (40*coin_40_count)
    if return_change >=20:
        coin_20_count = return_change/coin_20
        coin_20_count = math.floor(coin_20_count) 
        return_change = return_change - (20*coin_20_count)
    if return_change >=10:
        coin_10_count = return_change/coin_10
        coin_10_count = math.floor(coin_10_count) 
        return_change = return_change - (10*coin_10_count)
    if return_change >= 5:
        coin_5_count = return_change/coin_5
        coin_5_count = math.floor(coin_5_count) 
        return_change = return_change - (5*coin_5_count)
    if return_change >=1:
        coin_1_count = return_change
    print("\nYour total change is {0} Ksh which is: {1} x 1000 Ksh,{2} x 500 Ksh,{3} x 200 Ksh,{4} x 100 Ksh,{5} x 50 Ksh,{6} x 40 Ksh,{7} x 20 Ksh,{8} x 10 Ksh,{9} x 5 Ksh,{10} x 1 Ksh".format(original_change,bill_1000_count,bill_500_count,bill_200_count,bill_100_count,bill_50_count,coin_40_count,coin_20_count,coin_10_count,coin_5_count,coin_1_count))

slipted_change(return_change,original_change)

