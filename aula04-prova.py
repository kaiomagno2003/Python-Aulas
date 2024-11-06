inicInt = int(input("Digite um número inteiro: "))
fimInt = int(input("Digite outro número inteiro: "))
total = 0
for num in range(inicInt, fimInt +1):
    if num % 2 == 0:
        total += num
else:
    if total == 0:
        print("Não há números pares")
    else:
        print(f"A soma dos números pares = {total}")