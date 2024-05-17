#get number of case input
numberOfCase = int(input())
#loop amont of input
for i in range(numberOfCase):
    #get line of input
    ip = input()
    ipList = ip.split(" ")
    amount = int(ipList[0])
    normalPrice = int(ipList[1])
    promotionPrice = int(ipList[2])
    amountDivineByTwo = int(amount/2)
    if(normalPrice == 0 or promotionPrice == 0):
        print(str(0))
    elif(normalPrice * 2 < promotionPrice):
        ans = int(amount * normalPrice)
        print(str(ans))
    elif (amount % 2 == 0):
        ans = int(amountDivineByTwo * promotionPrice)
        print(str(ans))
    else:
        ans = int(amountDivineByTwo * promotionPrice)
        ans = ans + normalPrice
        print(str(ans))