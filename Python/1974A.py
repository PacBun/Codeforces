import math
case = int(input())

for i in range(case):
    amount = input().split(" ")
    amountTwo = int(amount[1])
    amountOne = int(amount[0])
    remainSpace = 15
    screenAmount = math.ceil(amountTwo/2)
    if(amountTwo > 0):
        remainSpace = (15*screenAmount) - (4*amountTwo)
    if(amountOne > remainSpace):
        screenAmount = screenAmount + math.ceil((amountOne - remainSpace) / 15)
    if(amountOne > amountTwo and amountTwo == 0):
        screenAmount = math.ceil(amountOne / 15)
    print(screenAmount)
