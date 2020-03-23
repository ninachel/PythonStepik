n = int(input())
sum1 = n // 100000 + (n // 10000) % 10 + (n // 1000) % 10
sum2 = (n // 100) % 10 + (n // 10) % 10 + n % 10
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')
