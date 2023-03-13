numero = int(input("Digite um número inteiro: "))

soma = 0
while numero > 0:
    soma += numero % 10
    numero = numero // 10

print("A soma dos dígitos do número é:", soma)
