c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n = len(c)  # число строк полученной матрицы
m = len(c[0])  # число столбцов полученной матрицы
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()
