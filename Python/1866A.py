num = int(input())
numlist = input()
numlist = numlist.split(" ")
ans = abs(int(numlist[0]))
for i in numlist:
    if ans > abs(int(i)):
        ans = abs(int(i))
print(str(ans))
