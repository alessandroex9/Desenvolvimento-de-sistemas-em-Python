lista = [10, 20, 30]
print("Lista original:", lista)

lista.append(99)
print("Adicionando o 99:", lista)

aux = lista.pop()
print("Elemento removido:", lista)

print("Resultado final:", lista)

lista1 = []

for i in range(10):
    print("Digite o elemento da posição", i)
    dado = int(input())
    lista1.append(dado)

print("Lista preenchida:")

for i in range(10):
    print("O elemento da posição", i,"é", lista1[i])