
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def acheioprimo(n):
    pares = []
    for x in range(2, n):
        if primo(x):
            y = n - x
            if primo(y) and x != y:
                pares.append((x, y))
    return pares

m = int(input("Escreva um numero inteiro:"))
pares = acheioprimo(m)
print(pares)

