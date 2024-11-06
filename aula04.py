# #ATIVIDADE 01
# numero = int(input("Digite um numero: "))
# for tabuada in range(1,11):
#     resultado = tabuada * numero
#     print(f"{tabuada} x {numero} = {resultado}")

# #ATIVIDADE 02
# total = 0
# for soma in range(1,101):
#     total += soma
# print(total)

# #ATIVIDADE 03
# palavra = input("Digite uma palavra: ")
# for letra in palavra:
#     print(letra)

# #ATIVIDADE 04
# for num in range(10,0,-1):
#     print(num)
# print("Feliz Ano Novo!")

# #ATIVIDADE 05
# totalPos = 0
# totalNeg = 0
# for i in range(10):
#     numero = int(input("Digite um número: "))
#     if numero > 0:
#         totalPos += 1
#     else:
#         totalNeg += 1
# print(f"O total de numeros positivos é {totalPos}")
# print(f"O total de numeros negativos é {totalNeg}")

# #ATIVIDADE 06
# total = 0
# for i in range(1,51):
#     if i % 2 == 0:
#         total += i
# print(total)

# #ATIVIDADE 07
# palavra = input("Digite uma palavra: ")
# contador = 0
# for letra in palavra:
#     if letra in "aeiou":
#         contador += 1
# print(f"O numero de vogais na palavra digitada é {contador}")

# #ATIVIDADE 08:
# soma = 0
# for nota in range(5):
#     nota = float(input("Digite uma nota: "))
#     soma += nota
#     media = soma / 5
# if media >= 6:
#     print(f"A sua média é {media}. Voce está APROVADO")
# else:
#     print(f"A sua média é {media}. Voce está REPROVADO")

# #ATIVIDADE 09
# for num in range(1,21):
#     if num % 2 == 0:
#         print(f"{num} é par")
#     else:
#         print(f"{num} é impar")
#     if num == 20:
#         break

#ATIVIDADE 10
# totalPos = 0
# totalNeg = 0
# for i in range(10):
#     numero = int(input("Digite um número: "))
#     if numero > 0:
#         totalPos += 1
#     elif numero < 0:
#         totalNeg += 1
#     if numero == 0:
#         break
# print(f"O total de numeros positivos é {totalPos}")
# print(f"O total de numeros negativos é {totalNeg}")

# #ATIVIDADE 11:
# for num in range(1,31):
#     if num % 5 == 0:
#         print(f"{num} é múltiplo de 5")
#     else:
#         print(num)
#     if num > 19:
#         break

# #ATIVIDADE 12
# soma = 0
# for preco in range(5):
#     preco = float(input("Digite o preço do item: "))
#     soma += preco
#     if soma > 100:
#         print(f"O valor total é {soma}. Voce tem 10% de desconto. O valor final a pagar = {soma - (soma * 0.1)}")
#         break
# else:
#     print(f"O valor total = {soma}")
    