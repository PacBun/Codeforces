#get number of case input
numberOfCase = int(input())
#loop amont of input
for i in range(numberOfCase):
    ip = input()
    #input of line 1
    ipList = ip.split(" ")
    numberOfShips = int(ipList[0])
    numberOfAttack = int(ipList[1])
    #input for each boat durability
    ip2 = input()
    #convert to int list
    shipList = ip2.split(" ")
    shipList = [int(i) for i in shipList]
    destroyShip = 0
    if(numberOfAttack <= 0):
        print(0)



    