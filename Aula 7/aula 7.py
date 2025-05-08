a = int(input("Escolha um número: "))

eh_primo = True
for i in range(a-1,1,-1):
    if a%i == 0:
        eh_primo = False
    else:
        print(eh_primo)    