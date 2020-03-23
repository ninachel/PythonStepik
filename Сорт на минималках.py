a = sorted([int(n) for n in input().split(' ')])
for i in set(a):
    b = a.count(i)
    if b > 1:
        print(i, end=' ')
