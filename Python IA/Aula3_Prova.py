produtos = {}
soma = 0

for itens in range(4):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos[nome] = preco
    soma += preco
print(f'O valot total do produtos é {soma}')