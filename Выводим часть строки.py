n = int(input())
s0 = []
s1 = []
for i in range(1, n + 1):
    for j in range(i):
        s0.append(i)
for i in range(n):
    s1.append(s0[i])
    print(s1[i], end=' ')
