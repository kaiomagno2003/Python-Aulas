# Variável comum

nome = "Fulano"

# Variável de sequencia

# Lista de Strings, Inteiro e Flutuantes

# Tuple<str | int | float>

# sobrenome = "Sousa"
# nomes = ("João", "Pedro", "Lucas")

# # USANDO O WHILE
# index = 0
# while index <= 3:
#     print(f"{nomes[index]} {sobrenome}")
#     index += 1

# # USANDO O FOR
# for nome in nomes:
#     print(f"{nome} {sobrenome}")


# precosCarrinho = (10.50, 29.90, 51, 89, 100)

# # Usando o For e While, como posso obter a soma de
# # todos os produtos?

# # WHILE
# total = 0
# index = 0

# while index < len(precosCarrinho):
#     total += precosCarrinho[index]
#     index += 1

# print(total)


# # FOR

# total = 0
# for preco in precosCarrinho:
#     total += preco

# print(total)


# RANGE 

# for numero in range(5):
#     print(numero)


# nome = "Edson"

# print(nome[0])


# for n in range(4, 8, 2):
#     print(n)




# 1  -----------------------------------------------------------------

# numero = int(input("Digite um numero para ver sua tabuada: "))

# for i in range(1, 11):
#     resultado = i * numero
#     print(f"{numero} X {i} = {resultado}")

# 2  -----------------------------------------------------------------

# total = 0
# for i in range(1, 101):
#     total += i


# print(total)

# 3  -----------------------------------------------------------------

# palavra = input("Digite uma palavra: ")

# for letra in palavra:
#     print(letra)


# 4  -----------------------------------------------------------------

totalPos = 0
totalNeg = 0

for i in range(10):
    numero = int(input("Digite um numero: "))

    if numero > 0:
        totalPos += 1
    else: 
        totalNeg += 1

print(f"Total numero positivo: {totalPos}")
print(f"Total numero negativo: {totalNeg}")