produto = {
    'codigo' : 0,
    'descricao' : "",
    'preco': 0.0,
    'qtde': 0.0,
}

produto['codigo'] = int(input("Digite o código do produto: \n"))
produto['descricao'] = input("Digite a descrição do produto: \n")
produto['preco'] = float(input("Digit o preço do produto: \n"))
produto['qtde'] = float(input("Digite  quntidade em estoque do produto: \n"))

print("Código: ", produto["codigo"])
print("Descrição: ", produto["descricao"])
print("Preço: ", produto["preco"])
print("Quantidade estoque: ", produto["qtde"])