x = True
while x == True:
    a = int(input("Qual o primeiro número: "))  
    b = int(input("Qual o segundo número: "))  
    c = input("Qual a operação? (+ - * /): ") 

    if c == "/":
        if b != 0:  
            print(a / b)
        else:
            print("Não é possível dividir por zero.")
    elif c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    else:
        print("Operação inválida.")  

    v = input("Você quer continuar? (sim = s, não = n): ") 
    if v == "n":  
        x = False
