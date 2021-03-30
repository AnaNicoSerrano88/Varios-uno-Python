from collections import namedtuple
import re

# lambda 1
b = lambda x, y : x + y

print(b(92,3))


# namedtuple
point = namedtuple('point', 'x, y')

target_pos = point(100,200)
print(target_pos.y)

# regular expresion
p = re.compile('r[aeiou]se')
result = p.search('A rose is a rose is a rose.')
print(result)

if result:
    print('Si esta')
else:
    print('No esta')

    