n = int(input("Qual número natural? "))


for i in range(2, n):
    if n % i == 0:
        print(f"{n} não é primo.")
        for i in range(2, n):
            if n % i == 0:
                print(i)
        break
else:
    print(f"{n} é primo.")

