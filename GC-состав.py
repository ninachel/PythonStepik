s = input()
sum = len(s)
n = s.lower().count('c') + s.lower().count('g')
print(n / sum * 100)
