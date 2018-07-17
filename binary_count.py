def countBits(n):
    binary_rep = bin(n)[2:]
    count = 0
    for i in str(binary_rep):
        if i=="1":
            count+=1
    print(count)

countBits(10)