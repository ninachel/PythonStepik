s = [i.lower() for i in input().split()]
d = {}
for i in s:
    d[i] = s.count(i)
for key, value in d.items():
    print(key, value)
