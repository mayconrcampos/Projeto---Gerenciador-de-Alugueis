def valida_valor(numero):
    numero = numero.strip()
    if numero.isnumeric():
        print("Print Inteiro: ", int(numero))
    else:
        c = 0
        for i in numero:
            if i in ",.":
                c += 1
        if c:
            numero = numero.replace(",", ".")
            print("Print Float: ", float(numero))
        else:
            print("Burp!")

    
cont = " "
while True:
    if cont:
        n = input("Valor: ")
        valida_valor(n)

        cont = input("Continua ... ")
    else:
        break