#get input number of test case
tc = int(input())
#define answer list
ansList = ["abc", "acb", "bac", "cba"]

for i in range(tc) :
    #get str to check
    ch = input();
    #check length
    if len(ch) != 3 :
        print("NO")
    else :
        ans = "NO"
    #define test case and response
        for j in ansList :
            if ch == j :
                ans = "YES"
                break
        print(ans)
        