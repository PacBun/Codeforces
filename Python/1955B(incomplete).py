def isEven(i):
    if(i % 2 == 0):
        return True
    else: return False
def matrixCalculation(a, n, c, d, g):
    squareMatrix = []
    calLength = 0
    counter = 0
    for i in range(n):
        squareMatrix.append(a + (d*counter))
        counter+=1
    if(isEven(n)):
        calLength = pow(n,2)
    else: calLength = pow(n,2)-1
    for i in range(2,calLength):
        value = squareMatrix[i-2] + c
        squareMatrix.append(value)
    s1 = sorted(squareMatrix)
    s2 = sorted(g)
    if(s1 == s2):
        print("YES")
    else: print("NO")
        
# matrixCalculation(300,100,100,2)
#get input
amount = int(input())
for i in range(amount):
    #input n ,c, d at pos 0,1,2
    inputList = (input().split(" "))
    #then for each element at size n^2
    inputMatrix = input().split(" ")
    #convert to int list
    intMatrix = []
    for i in inputMatrix:
        intMatrix.append(int(i))
    minValue = min(inputMatrix)
    matrixCalculation(int(minValue),int(inputList[0]),int(inputList[1]),int(inputList[2]),intMatrix)




