"""Дана послідовність s, що складається з символів s1, s2,... Відомо, що символ
 s1 відмінний від знаку оклику і що серед s2, s3,... є хоча б один знак оклику.
 Припустимо s1,..., sn — символи даної послідовності, що передують першому
 знаку оклику (n заздалегідь не відомо). Визначити кількість пробілів серед
 послідовности s1,..., sn.
"""
s = 'Some text with spaces! And exclamations!!!!'

space_count = 0
for i in range(len(s)):
    if s[i] == ' ':
        space_count += 1
    elif s[i] == '!':
        break

# Інший спосіб розв'язання задачі за допомогою метода split()
# space_count = len(s.split('!')[0].split(' ')) - 1

print('Послідовність символів:')
print(s)
print(f'Кількість пробілів до першого символу "!": {space_count}')
