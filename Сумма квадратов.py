sum = 0
sq_sum = 0
n = 0
while True:
    n = int(input())
    sum += n
    sq_sum += n**2
    if sum == 0:
        break
print(sq_sum)
