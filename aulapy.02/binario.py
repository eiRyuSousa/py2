numero = int(input("Digite um número inteiro: "))

binario = ""

while numero > 0:
    resto = numero % 2
    binario = str(resto) + binario
    numero //= 2

print("O número em binário é:", binario)
