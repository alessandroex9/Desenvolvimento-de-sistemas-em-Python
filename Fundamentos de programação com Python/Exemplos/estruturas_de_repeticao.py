#Exemplo do for
for i in range (0,10,1):
    print("Aguarde...")

#Exemplo de While
conta = 0
while conta < 10:
    conta = conta +1  
    print("Contagem ", conta)

#Desafio dos lanços de repetição
print("Desafio dos lanços de repetição!")
numero = int(input("Digite um numero: "))

if numero > 0:
    for i in range (numero, 0, -2):
        if i == 0:
            print("Seu numero pode ser sublitaido por 2 em ",i-1 ,"vezes")

elif numero == 0:
    print("Seu numero é igual a zero")
    
elif numero < 0:    
    print("Seu numero é negativo")