words, text = set(), set()
for i in range(int(input())):
    words.add(input().lower())
for j in range(int(input())):
    text.update(input().lower().split(' '))
print('\n'.join(text - words))
