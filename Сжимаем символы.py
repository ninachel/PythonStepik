s = input()
i = 0
count = 1
s_new = ''
while i < (len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        s_new = s_new + s[i] + str(count)
        count = 1
    i += 1
print(s_new + s[i] + str(count))
