a = int(input("Qual numero na sala de aula:"))
for i in range (a):
    print(" \nAluno:{}".format(i+1))
    
    p1 = float(input("Qual a nota da p1: "))
    p2 = float(input("Qual a nota da p2:"))
    m = (p1 * 3 + p2 * 5) / 8
    print(m)
    if m >= 7:
        print("passou")
    elif m >= 4:
        print("Prova Final")
    else:
        print("Nao passou")






   


    


