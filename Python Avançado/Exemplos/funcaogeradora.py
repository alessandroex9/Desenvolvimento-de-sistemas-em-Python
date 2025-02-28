def gera_AB():
    print('Start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

for c in gera_AB():
    print('-->', c)

#Nesse caso o StopIteration iria acontecer
g = gera_AB()

print(next(g))
print(next(g))
print(next(g))