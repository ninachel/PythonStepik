alphabet0 = input()
alphabet1 = input()

encode = input()
decode = input()

code = {}
decrypt = {}
for i in range(len(alphabet0)):
    code.update([(alphabet0[i], alphabet1[i])])
    decrypt.update([(alphabet1[i], alphabet0[i])])

res_encode = []
for x in encode:
    res_encode.append(code[x])
print(''.join(res_encode))

res_decode = [decrypt[x] for x in decode]
print(''.join(res_decode))
