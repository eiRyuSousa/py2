# função para verificar se um número é primo
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# função para encontrar os fatores primos de um número
def prime_factors(n):
    factors = []
    i = 2
    while n > 1:
        if n % i == 0 and is_prime(i):
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors

# leitura do número inteiro
n = int(input("Digite um número inteiro: "))

# exibição dos fatores primos
print("Fatores primos de", n, ": ", prime_factors(n))
