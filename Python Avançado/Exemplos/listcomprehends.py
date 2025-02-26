cores  =['black', 'white']
tamanhos = ['S', 'M', 'L']

#plano cartesiano

tshirts = []

for color in cores:
    for size in tamanhos:
        tshirts.append((color, size))
tshirts

#list comprehends
tshirts = [(color, size) for color in cores for size in tamanhos]
tshirts