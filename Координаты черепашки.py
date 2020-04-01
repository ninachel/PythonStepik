dict = {'север': 0, 'юг': 0, 'запад': 0, 'восток': 0}

for i in range(int(input())):
    key, value = input().split()
    dict[key] += int(value)

print(dict['восток'] - dict['запад'], dict['север'] - dict['юг'])
