num = int(input())
for i in range(num):
    coinAmount = int(input())
    coinStatus = str(input())
    if(coinAmount % 2 != coinStatus.count('U') % 2):
        print("YES")
    else: print("NO")