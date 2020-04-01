key1, key2, encode, decode = input(), input(), input(), input()
print(''.join(key2[key1.index(i)] for i in encode))
print(''.join(key1[key2.index(i)] for i in decode))
