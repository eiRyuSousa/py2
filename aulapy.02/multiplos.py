numero = int(input("Digite um número inteiro: "))

print("Múltiplos de", numero, "menores que 100:")

for i in range(1, 100):
    if i % numero == 0:
        print(i)
