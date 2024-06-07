case = int(input())
for i in range(case):
    s = input()
    if(s[0] > s[2]):
        print(s[2] + " " + s[0])
    else: print(s)