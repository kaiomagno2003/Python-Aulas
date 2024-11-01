print("Você precisa adivinhar qual número programei como correto. Para isso, você terá 3 chances.")
numero = int(input("Digite um numero inteiro: "))
contador = 1
while numero != 7:
    numero = int(input("Você errou. Digite novamente um numero inteiro: "))
    contador += 1
    if contador >= 3 and numero != 7:
        print("Que pena! Você não acertou.")
        break
else:
    print("Parabéns! Você acertou o numero que programei.")