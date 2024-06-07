c = int(input())
d = []
for i in range(0,7):
    d.append(chr(65+i))
for i in range(c):
    b = input()
    b = b.split(" ")
    a = input()
    a = sorted(a)
    g = []
    for i in range(len(d)):
        g.append(a.count(d[i]))
    e = int(b[1])
    ans = 0
    for i in g:
        if i < e:
            ans += e-i
    print(ans)


