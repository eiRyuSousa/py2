numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1
    for i in range(1, numero+1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}.")
