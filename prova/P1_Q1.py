def m (n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        sequence.append(n)
    return sequence


n = int(input("Escreva um numero inteiro: "))
sequence = m (n)
print(sequence)



