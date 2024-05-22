num = int(input())
for i in range(num):
    coinAmount = int(input())
    coinStatus = str(input())
    if(coinAmount != 2 and coinStatus.count('U') % 2 == 1 and coinStatus.count('U') != 0):
        print("YES")
    elif (coinAmount == 2 and coinStatus[0] != coinStatus[1]): 
        print("YES")
    else: print("NO")