#ATIVIDADE 01
# numero = 1
# while numero <= 10:
#     print(numero)
#     numero += 1

#ATIVIDADE 02
# numero = 1
# soma = 0
# while numero <= 100:
#     soma += numero
#     numero +=1
# print(soma)

#ATIVIDADE 03
# numero = int(input("Digite um número: "))
# tabuada = 1
# while tabuada <= 10:
#     print(f"{tabuada} x {numero} = {numero * tabuada}")
#     tabuada += 1

#ATIVIDADE 04
# numero = 10
# while numero >= 1:
#     print(numero)
#     numero -= 1
# print("Feliz Ano Novo!")

#ATIVIDADE 05
# numero = int(input("Digite um número: "))
# contagem = 1
# while contagem <= numero:
#     if contagem % 2 != 0:
#         print(contagem)
#     contagem += 1

#ATIVIDADE 06
# numero = int(input("Digite um número qualquer. Caso deseje sair, digite um numero negativo: "))
# soma = 0
# while numero > 0:
#     soma += numero
#     numero = int(input("Digite um número qualquer. Caso deseje sair, digite um numero negativo: "))
# print(f"A soma dos numeros digitados = {soma}")

#ATIVIDADE 07
# numero = int(input("Digite um número: "))
# tabuada = 1
# resultado = 0
# while tabuada <= 10:
#     resultado = tabuada * numero
#     if resultado % 3 == 0: 
#         print(f"{tabuada} x {numero} = {resultado}")
#     tabuada += 1

#ATIVIDADE 08
# nota = float(input("Digite uma nota. Caso deseje sair, digite -1: "))
# soma = 0
# media = 0
# contador = 0
# while nota > 0:
#     soma += nota
#     nota = float(input("Digite outra nota. Caso deseje sair, digite -1: "))
#     contador += 1
#     media = soma / contador
# print(f"A média das notas digitadas = {media}")

#ATIVIDADE 09
# numero = 1
# while numero <= 10:
#     print(numero)
#     numero += 1
#     if numero > 10:
#         break

#ATIVIDADE 10
# numero = 0
# soma = 0
# while numero <= 50:
#     soma += numero
#     numero += 1
#     if soma >= 50:
#         break
# print(soma)

#ATIVIDADE 11
numero = int(input("Digite um número: "))
while numero <= 0 and numero >= 11:
    numero = int(input("Digite um número: ")) 
else:
    print("Acesso Permitido")



#ATIVIDADE 12
# senha = None
# senhaCorreta = "12345"

# while senha != senhaCorreta:
#     senha = input("Digete a senha: ")
# print("Acesso permitido!")