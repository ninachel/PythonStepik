lst = [int(n) for n in input().split(' ')]
x = int(input())
out = []
if lst.count(x) == 0:
    print('Отсутствует')
else:
    for i in range(len(lst)):
        if lst[i] == x:
            out.append(i)
    print(*out)
