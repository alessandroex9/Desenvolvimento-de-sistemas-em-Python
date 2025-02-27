# 'ABC' é uma iterable
s = 'ABC'

for char in s:
    print(char)


# 'ABC' é uma iterators
s = 'ABC'

it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
