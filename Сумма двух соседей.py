s = [int(i) for i in input().split()]
i = 0
if len(s) > 1:
    while i < (len(s) - 1):
        print(s[i - 1] + s[i + 1], end = ' ')
        i += 1
    print(s[i - 1] + s[0])
else:
    print(s[0])
