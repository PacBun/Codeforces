case = int(input())
for i in range(case):
    useless = input()
    s = input()
    ans = ""
    setOfAlphabet = sorted(set(s), reverse= True)
    setOfAlphabetReverse = sorted(set(s))
    pairSet = {}
    for i in range(len(setOfAlphabet)):
        pairSet[setOfAlphabet[i]] = setOfAlphabetReverse[i]
    for i in s:
        ans += i.replace(i,pairSet.get(i))
    print(ans)
    