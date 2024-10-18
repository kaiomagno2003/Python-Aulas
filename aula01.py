saudacao = "Hello World"

nome = input('Qual o seu nome? ')
altura = input('Qual a sua altura? ')
idade = input("Qual a sua idade? ")
print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))

num1 = 62
num2 = 11
print("Adição: ", num1 + num2)
print("Subtração: ", num1 - num2)
print("Multiplicação: ", num1 * num2)
print("Divisão: ", num1 / num2)
print("Divisão Inteira: ", num1 // num2)
print("Módulo: ", num1 % num2)
print("Exponenciação: ", num1 ** num2)

bim1 = float(input("Qual a sua nota do primeiro bimestre? "))
bim2 = float(input("Qual a sua nota do segundo bimestre? "))
bim3 = float(input("Qual a sua nota do terceiro bimestre? "))
bim4 = float(input("Qual a sua nota do quarto bimestre? "))
media = (bim1 + bim2 + bim3 + bim4) / 4
print(f"Sua média geral é {media} ")

salario = float(input("Qual o seu salário mensal? "))
horasDia = float(input("Quantas horas você trabalha por dia? "))
horasMes = horasDia * 20
salarioHora = salario / horasMes
print(f"Seu salário/hora é R${salarioHora}")

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
cidade = input('Qual a sua Cidade Natal? ')
print(f"Olá {nome}! Você tem {idade} anos e nasceu em {cidade}")