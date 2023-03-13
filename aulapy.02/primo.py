# Função para checar se um número é primo
def eh_primo(num):
    # Números menores ou iguais a 1 não são primos
    if num <= 1:
        return False
    
    # 2 é primo
    if num == 2:
        return True
    
    # Números pares não são primos
    if num % 2 == 0:
        return False
    
    # Verifica se o número é divisível por algum ímpar menor que ele
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    
    return True


# Lê um número inteiro do usuário
n = int(input("Digite um número inteiro: "))

# Exibe todos os números primos menores ou iguais a n
print("Números primos menores ou iguais a", n, ":")
for i in range(2, n+1):
    if eh_primo(i):
        print(i)
