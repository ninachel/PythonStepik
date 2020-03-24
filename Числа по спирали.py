num = int(input())
matrix = [[0] * num for j in range(num)]
i, j = 0, 0
for k in range(1, num ** 2 + 1):
    matrix[i][j] = k
    if i + j < num - 1 and i <= j + 1:
        j += 1
    elif i + j >= num - 1 and i < j:
        i += 1
    elif i + j > num - 1:
        j -= 1
    else:
        i -= 1
for i in range(num):
    print(*matrix[i])
